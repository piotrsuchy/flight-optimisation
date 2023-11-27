import copy
import random
import numpy as np
import json

from .schedule import Schedule
from .solution import Solution
from .passenger_demand import generate_demand_array# , visualize_demand

# from .decorators import timing_decorator
with open('parameters.json') as parameters_file:
    config = json.load(parameters_file)


class EvolutionaryAlgorithm:
    # s@timing_decorator
    def __init__(self, initial_structures, population_size=config["POPULATION_SIZE"]):
        self.population_size = population_size
        self.population = []
        self.initial_structures = initial_structures
        self.passenger_demand = generate_demand_array(
            self.initial_structures.airports, config["SIM_LEN"]//24)

    # @timing_decorator
    def initialize_population(self):
        for sol_id in range(self.population_size):
            initial_structures = copy.deepcopy(self.initial_structures)
            sol = Solution(
                sol_id + 1,
                self.passenger_demand,
                initial_structures,
                config['SIM_LEN'])
            sol.set_sol_ids(sol_id + 1)
            # population is a list of [sol, [revenue, op_costs, penalties]]
            self.population.append([sol, -1])

    # @timing_decorator
    def print_population(self):
        for sol_list in self.population:
            sol = sol_list[0]
            for airport in sol.structures.airports:
                airport.show_fleet_and_crew()

    # @timing_decorator
    def print_schedules(self):
        print(f"Printing the SCHEDULES")
        for sol_list in self.population:
            print(f"Schedule for solution {sol_list[0].id}")
            print(sol_list[0].schedule)

    # @timing_decorator
    def assign_schedules_for_all_sols(self):
        for sol_list in self.population:
            sol_list[0].schedule = Schedule()
            sol_list[0].schedule.create_random_schedule(
                sol_list[0], config['N_OF_FLIGHTS'], config['SIM_LEN'], config['SEED_1'])

    def reset_schedulers(self, time):
        for sol_list in self.population:
            sol_list[0].scheduler.set_time(time)

    # @timing_decorator
    def run_schedules(self):
        for sol_list in self.population:
            sol_list[0]._schedule_flights()

    # @timing_decorator
    def save_events_for_all_sols(self):
        for sol_list in self.population:
            sol_list[0].get_scheduler_events()

    # @timing_decorator
    def save_events_for_sol_by_id(self, sol_id):
        sol_list = self.population[sol_id]
        print(f"sol_list {sol_list}")
        sol_list[0].get_scheduler_events()

    # @timing_decorator
    def run_events(self):
        for sol_list in self.population:
            sol_list[0].run_events()

    # @timing_decorator
    def fitness_function(self, sol):
        '''
        This function calculates revenue, operational costs and penalties of a single solution
        If the flight is cancelled it
        It returns a list of [revenue, op_costs, penalties]
        '''
        # Initializing metrics
        revenue = 0
        operational_costs = 0
        penalties = 0
        delay_penalty = 0

        # 1. Calculate Revenue
        # for flight in sol.flights:
        #     if flight.status == "cancelled":
        #         continue

        #     revenue += flight.passengers * config['TICKET_PRICE']

        # 2. Calculate Operational Costs
        for flight in sol.flights:
            if flight.status == "cancelled":
                continue
            flight_duration = flight.duration
            plane_cost = config['PLANE_OPERATIONAL_COST_PER_HOUR'] * flight_duration
            pilot_cost = config['PILOT_COST_PER_HOUR'] * flight_duration
            attendant_cost = config['ATTENDANT_COST_PER_HOUR'] * flight_duration
            operational_costs += plane_cost + 2 * pilot_cost + 4 * \
                attendant_cost  # Assuming 2 pilots and 4 attendants

        # 3. Calculate Penalties
        for flight in sol.flights:
            if flight.delay != 0:
                print(
                    f"Sol: {flight.sol.id} Calculating extra penalties for the delay of flight {flight.id}, {flight.delay}h")
                delay_penalty = flight.delay * 2 * config['PLANE_OPERATIONAL_COST_PER_HOUR']
                penalties += delay_penalty

            if flight.status == "cancelled":
                from_airport_idx = flight.base_airport.id - 1
                to_airport_idx = flight.destination_airport.id - 1
                day_of_flight = flight.day  # Assuming the Flight class has a day attribute
                demand = self.passenger_demand[from_airport_idx][to_airport_idx][day_of_flight]

                # You can also add an upper limit based on a default plane
                # capacity if required
                filled_seats = min(demand, config['DEFAULT_PLANE_CAPACITY'])

                penalties += config['FLIGHT_CANCELLATION_COST_PER_PERSON'] * filled_seats
                continue

            try:
                for pilot in flight.pilots:
                    if pilot.week_worked_hs > config['MAX_WEEKLY_HOURS']:
                        penalties += config['OVERWORK_PENALTY_PER_HOUR'] * \
                            (pilot.week_worked_hs - config['MAX_WEEKLY_HOURS'])

                for attendant in flight.attendants:
                    if attendant.week_worked_hs > config['MAX_WEEKLY_HOURS']:
                        penalties += config['OVERWORK_PENALTY_PER_HOUR'] * \
                            (attendant.week_worked_hs - config['MAX_WEEKLY_HOURS'])
            except TypeError:
                print(
                    f"In sol: {sol.id} in flight: {flight.id} pilots or attendants are None")

        return [revenue, operational_costs, penalties, delay_penalty]

    def roulette_selection(self):
        '''This function selects a solution using roulette wheel selection'''
        total_fitness = sum(sol[0].fitness_score for sol in self.population)
        selection_probabilities = [
            sol[0].fitness_score / total_fitness for sol in self.population]
        selected_index = np.random.choice(
            len(self.population), p=selection_probabilities)
        return self.population[selected_index]

    def tournament_selection(self, tournament_size=5):
        '''This function selects a solution using tournament selection'''
        if len(self.population) <= tournament_size:
            selected_tournament = self.population
        else:
            selected_tournament = random.sample(
                self.population, tournament_size)
        best_in_tournament = max(
            selected_tournament, key=lambda sol: sol[0].fitness_score)
        return best_in_tournament

    def rank_selection(self):
        '''This function selects a solution using rank selection'''
        sorted_population = sorted(
            self.population, key=lambda sol: sol[0].fitness_score)
        rank_sum = len(sorted_population) * (len(sorted_population) + 1) / 2
        rank_probabilities = [
            (i + 1) / rank_sum for i in range(len(sorted_population))]
        selected_index = np.random.choice(
            len(sorted_population), p=rank_probabilities)
        return sorted_population[selected_index]

    # @timing_decorator
    def roulette_sort(self):
        '''This function sorts the population using repeated roulette wheel selection'''
        sorted_population = []
        while len(sorted_population) < self.population_size - 1:
            selected = self.roulette_selection()
            sorted_population.append(selected)
            self.population.remove(selected)
        self.population = sorted_population

    # @timing_decorator
    def tournament_sort(self, tournament_size=5):
        '''This function sorts the population using repeated tournament selection'''
        sorted_population = []
        while len(sorted_population) < self.population_size - 1:
            best_in_tournament = self.tournament_selection(tournament_size)
            sorted_population.append(best_in_tournament)
            self.population.remove(best_in_tournament)
        self.population = sorted_population

    # @timing_decorator
    def rank_sort(self):
        '''This function sorts the population using rank selection (simply by fitness value)'''
        sorted_population = []
        while len(sorted_population) < self.population_size - 1:
            selected = self.rank_selection()
            sorted_population.append(selected)
            self.population.remove(selected)
        self.population = sorted_population

    # @timing_decorator
    def update_all_fitness_scores(self):
        '''
        This function uses the fitness_function() method to calculate the fitness score
        of all solutions in the population
        '''
        for sol_id, sol in enumerate(self.population):
            revenue, operation_costs, penalties, delay_penalty = self.fitness_function(
                sol[0])
            self.population[sol_id][1] = [
                revenue, operation_costs, penalties, delay_penalty]
            self.population[sol_id][0].fitness_score = revenue - \
                operation_costs - penalties

    # @timing_decorator
    def print_revenue_and_costs(self, iteration):
        for sol in self.population:
            print(
                f"Iter: {iteration}, {sol[0]}, rev: {sol[1][0]:.2e}, op_costs: {sol[1][1]:.2e}, penalties: {sol[1][2]:.2e}, delay_penalties: {sol[1][2]:.2e}")

    def mutation_attendants(self):
        '''Make a random flight change the attendant / or attendants'''
        try:
            # random.seed(config['SEED_2'])
            random_sol_list = random.choice(self.population)
            # random.seed(config['SEED_1'])
            random_flight = random.choice(random_sol_list[0].flights)
            while random_flight.status == "cancelled":
                print(f"The chosen flight was cancelled!!!!!!!!!!!!!")
                random_flight = random.choice(random_sol_list[0].flights)
            print(f"Flight chosen: {random_flight}")
            simulation_time = random_flight.simulation_time
            print(f"Simulation time: {simulation_time}")
            old_attendants = random_flight.attendants
            base_airport = random_flight.base_airport
            log = base_airport.availability_log
            availability = log.get_availability(random_flight.simulation_time)
            new_attendants = random.sample(list(availability.attendants), config['ATTENDANTS_PER_PLANE'])
            random_flight.attendants = new_attendants
            # print(f"New pilots: {new_attendants}")
            # print(f"Old piltos: {old_attendants}")

            if old_attendants:
                for attendant in old_attendants:
                    availability.attendants.add(attendant)
            for attendant in old_attendants:
                availability.attendants.remove(attendant)

            return random_sol_list[0], simulation_time
        except ValueError as e:
            return f"An error occurred during attendants mutation: {e}"

    def mutation_pilots(self, sol):
        '''Make a random flight change the pilot / or pilots'''
        # random.seed(config['SEED_1'])
        random_flight = random.choice(sol.flights)
        while random_flight.status == "cancelled":
            print(f"The chosen flight was cancelled!!!!!!!!!!!!!")
            random_flight = random.choice(sol.flights)
        print(f"Flight chosen: {random_flight}")
        simulation_time = random_flight.simulation_time
        print(f"Simulation time: {simulation_time}")
        old_pilots = random_flight.pilots
        base_airport = random_flight.base_airport
        log = base_airport.availability_log
        availability = log.get_availability(random_flight.simulation_time)
        new_pilots = random.sample(list(availability.pilots), config['PILOTS_PER_PLANE'])
        random_flight.pilots = new_pilots
        print(f"New pilots: {new_pilots}")
        print(f"Old piltos: {old_pilots}")

        if old_pilots:
            for pilot in old_pilots:
                availability.pilots.add(pilot)
        for pilot in new_pilots:
            availability.pilots.remove(pilot)

        return simulation_time

    def crossover(self, sol1, sol2):
        '''Take two solutions and perform swap of crews?'''
        sol1.print_flights()
        sol2.print_flights()

    def reschedule_flights(self, sol, mutation_time):
        # reschedule flights only after the mutation_time
        flights_to_reschedule = [f for f in sol.flights if f.simulation_time > mutation_time]

        for airport in sol.structures.airports:
            airport.check_consistency()

        # remove the affected flights from the original schedule
        for flight in flights_to_reschedule[::-1]:
            flight.reset_state_after_mutation(sol)

        # Add back the flights to the schedule, which will now use the updated availablitity
        for flight in flights_to_reschedule:
            print(f"Adding back the flight: {flight.id} to the schedule")
            scheduled_time = flight.simulation_time
            print(f"Scheduled time is: {scheduled_time} and the mutation time is: {mutation_time}")
            sol.scheduler.schedule_event(scheduled_time, flight.start_flight)

    def reset_logs(self, sol, mutation_time):
        for airport in sol.structures.airports:
            airport.availability_log.clear_logs_after_timestamp(mutation_time)

    def evol_algo_loop(self, iterations_n, sol):
        for i in range(iterations_n):
            mutation_successful = False
            while not mutation_successful:
                try:
                    time = self.mutation_pilots(sol)
                    mutation_successful = True
                except ValueError:
                    print("Error during mutation. Retrying with a different flight.")

            for airport in sol.structures.airports:
                airport.check_consistency()

            self.reset_schedulers(0)
            self.reset_logs(sol, time)
            self.reschedule_flights(sol, time)
            self.run_events()
            self.update_all_fitness_scores()
            self.print_revenue_and_costs(i)