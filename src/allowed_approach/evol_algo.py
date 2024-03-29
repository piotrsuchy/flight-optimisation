import copy
import random
import numpy as np
import json
import logging
import statistics
import time
from pympler import asizeof

from src.allowed_approach.schedule import Schedule
from src.allowed_approach.solution import Solution

# from .decorators import timing_decorator
with open('parameters.json') as parameters_file:
    config = json.load(parameters_file)


class EvolutionaryAlgorithm:
    # @timing_decorator
    def __init__(self, initial_structures, population_size=config['algo']['POPULATION_SIZE']):
        self.population_size = population_size
        self.population = []
        self.initial_structures = initial_structures
        self.iteration_scores = []
        self.iteration_penalties = []

    def print_population(self):
        print(f"---Printing the population---")
        for sol_list in self.population:
            sol = sol_list[0]
            for airport in sol.structures.airports:
                airport.show_fleet_and_crew()

    def print_fitness_scores(self, iter):
        print(f"---ITER: {iter} ---Printing fitness scores---")
        for sol_list in self.population:
            sol = sol_list[0]
            print(f"Sol ID: {sol.id} Fit: {sol.fitness_score} Status: {sol.initialized} Canc: {sol.get_cancelled_flights_num()}, training_pen: {sol.get_training_penal_num()}, days_off_pen: {sol.get_dayoff_penal_num()}")

    def print_schedules(self):
        print(f"---Printing the schedules---")
        for sol_list in self.population:
            print(f"Schedule for solution {sol_list[0].id}")
            print(sol_list[0].schedule)

    def print_costs(self, iteration):
        for sol_list in self.population:
            print(
                f"Iter: {iteration}, {sol_list[0]} fit. score: {sol_list[0].fitness_score}")

    def print_all_info(self):
        self.population = sorted(
            self.population, key=lambda sol: sol[0].fitness_score, reverse=False)
        for sol_list in self.population:
            print(
                f"{sol_list[0]}, pil: {sol_list[0].pilot_cancel}, att: {sol_list[0].atten_cancel}, train_pen: {sol_list[0].get_training_penal_num()}")

    def initialize_population(self):
        for sol_id in range(len(self.population), self.population_size):
            initial_structures = copy.deepcopy(self.initial_structures)
            sol = Solution(
                sol_id + 1,
                initial_structures,
                config['sim']['SIM_LEN'])
            sol.set_sol_ids(sol_id + 1)
            # population is a list of [sol, [op_costs, penalties]]
            self.population.append([sol, -1])

    # @timing_decorator
    def assign_schedules_for_initialized_sols(self):
        for sol_list in self.population:
            if sol_list[0].initialized == "Initialized":
                sol_list[0].schedule = Schedule()
                sol_list[0].schedule.create_random_schedule(
                    sol_list[0], config['sim']['N_FLIGHTS'], config['sim']['SIM_LEN'], config['structs']['SEED_1'])
    
    def assign_schedules_for_initialized_sols_from_json(self, filename):
        for sol_list in self.population:
            if sol_list[0].initialized == "Initialized":
                sol_list[0].schedule = Schedule()
                sol_list[0].schedule.create_schedule_from_json(sol_list[0], filename)

    def reset_scheduler(self, time):
        for sol_list in self.population:
            sol_list[0].scheduler.set_time(time)

    # @timing_decorator
    def run_schedules(self):
        for sol_list in self.population:
            sol = sol_list[0]
            sol.flights = []
            sol.scheduler.set_time(0)
            sol._schedule_flights(config['algo']['ALLOWED_HEURISTIC'])

    # @timing_decorator
    def save_events_for_all_sols(self):
        for sol_list in self.population:
            sol_list[0].get_scheduler_events()

    # @timing_decorator
    def save_events_for_sol_by_id(self, sol_id):
        sol_list = self.population[sol_id]
        print(f"sol_list {sol_list}")
        sol_list[0].get_scheduler_events()

    def save_initial_scores_and_penalties(self):
        self.store_iteration_penalties(0)
        self.store_iteration_scores(0)

    # @timing_decorator
    def run_events(self):
        for sol_list in self.population:
            sol_list[0].run_events()

    # @timing_decorator
    def fitness_function(self, sol):
        '''
        This function calculates operational costs and penalties of a single solution
        If the flight is cancelled it applies a penalty
        It returns a list of penalties
        '''
        penalties = 0
        training_penalties = 0
        days_off_penalties = 0

        # Penalties 
        for flight in sol.flights:
            if flight.status[-1] == "cancelled":
                penalties += flight.duration * config['pen']['CANCEL_PENALTY_PER_HOUR']
                continue

            # try:
            for pilot in flight.pilots:
                if flight.simulation_time <= pilot.training_hours[1] and flight.simulation_time + flight.duration >= pilot.training_hours[0]:
                    training_penalties += config['pen']['TRAINING_OVERLAP_PENALTY']

                if flight.simulation_time // 24 in pilot.days_off:
                    days_off_penalties += config['pen']['DAYOFF_PENALTY']

            for attendant in flight.attendants:
                if flight.simulation_time <= attendant.training_hours[1] and flight.simulation_time + flight.duration >= attendant.training_hours[0]:
                    training_penalties += config['pen']['TRAINING_OVERLAP_PENALTY']

                if flight.simulation_time // 24 in attendant.days_off:
                    days_off_penalties += config['pen']['DAYOFF_PENALTY']

            # except TypeError as te:
            #     print(f"Status of the flight is: {flight.status}, but crew has None: pil: {flight.pilots} att: {flight.attendants}", te)

        return [int(penalties), int(training_penalties), int(days_off_penalties)]

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
        best_in_tournament = min(
            selected_tournament, key=lambda sol: sol[0].fitness_score)
        return best_in_tournament

    def rank_selection(self):
        '''This function selects a solution using rank selection for minimization problems'''
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
            penalties, training_penalties, dayoff_penalties = self.fitness_function(
                sol[0])
            self.population[sol_id][1] = [
                penalties, training_penalties, dayoff_penalties]
            self.population[sol_id][0].fitness_score = penalties + training_penalties + dayoff_penalties
            self.population[sol_id][0].training_penalty = training_penalties
            self.population[sol_id][0].dayoff_penalty = dayoff_penalties

    def mutation_attendants(self, sol):
        '''Make a random flight change the attendants'''
        random_flight = random.choice(sol.flights)

        simulation_time = random_flight.simulation_time

        old_attendants = random_flight.attendants
        base_airport = random_flight.base_airport
        log = base_airport.availability_log
        availability = log.get_availability(random_flight.simulation_time)
        new_pilots = random.sample(list(availability.pilots), config['structs']['PILOTS_PER_PLANE'])
        random_flight.pilots = new_pilots

        if old_attendants:
            for pilot in old_attendants:
                availability.pilots.add(pilot)
        for pilot in new_pilots:
            availability.pilots.remove(pilot)

        return simulation_time

    def mutation_pilots(self, sol):
        '''Make a random flight change the pilot / or pilots'''
        random_flight = random.choice(sol.flights)

        simulation_time = random_flight.simulation_time

        old_pilots = random_flight.pilots
        base_airport = random_flight.base_airport
        log = base_airport.availability_log
        availability = log.get_availability(random_flight.simulation_time)
        new_pilots = random.sample(list(availability.pilots), config['structs']['PILOTS_PER_PLANE'])
        random_flight.pilots = new_pilots

        if old_pilots:
            for pilot in old_pilots:
                availability.pilots.add(pilot)
        for pilot in new_pilots:
            availability.pilots.remove(pilot)

        return simulation_time

    def mutation_whole_crew(self, sol):
        '''Make a random flight change the pilot / or pilots'''
        random_flight = random.choice(sol.flights)

        simulation_time = random_flight.simulation_time

        old_pilots = random_flight.pilots
        old_attendants = random_flight.attendants
        base_airport = random_flight.base_airport
        log = base_airport.availability_log
        availability = log.get_availability(random_flight.simulation_time)
        new_pilots = random.sample(list(availability.pilots), config['structs']['PILOTS_PER_PLANE'])
        new_attendants = random.sample(list(availability.attendants), config['structs']['ATTEND_PER_PLANE'])
        random_flight.pilots = new_pilots
        random_flight.attendants = new_attendants

        if old_pilots:
            for pilot in old_pilots:
                availability.pilots.add(pilot)
        if old_attendants:
            for attendant in old_attendants:
                availability.attendants.add(attendant)
        for pilot in new_pilots:
            availability.pilots.remove(pilot)
        for attendant in new_attendants:
            availability.attendants.remove(attendant)

        random_flight.status.append("Mutated    ")
            
        return simulation_time

    def crossover(self, sol1, sol2):
        '''Take two solutions and perform swap of crews?'''
        sol1.print_flights()
        sol2.print_flights()

    def reschedule_flights(self, sol, mutation_time, iteration_number, heuristic):
        # reschedule flights only after the mutation_time
        self.reset_scheduler(0)
        flights_to_reschedule = [f for f in sol.flights if f.simulation_time > mutation_time]

        for airport in sol.structures.airports:
            airport.check_consistency()

        # remove the affected flights from the original schedule
        for flight in flights_to_reschedule[::-1]:
            flight.reset_state_after_mutation(sol)

        # Add back the flights to the schedule, which will now use the updated availablitity
        for flight in flights_to_reschedule:
            scheduled_time = flight.simulation_time
            sol.scheduler.schedule_event(scheduled_time, flight.start_flight, heuristic)

        self.reset_logs(sol, mutation_time)

    def reset_logs(self, sol, mutation_time):
        for airport in sol.structures.airports:
            airport.availability_log.clear_logs_after_timestamp(mutation_time)

    def sort_population(self):
        self.population = sorted(
            self.population, key=lambda sol: sol[0].fitness_score, reverse=False)
        
    def store_iteration_scores(self, iteration):
        scores = [sol_list[0].fitness_score for sol_list in self.population]
        best_score = min(scores)
        median_score = statistics.median(scores)
        top_half_median = statistics.median(sorted(scores)[:len(scores)//2])
        bottom_half_median = statistics.median(sorted(scores)[len(scores)//2:])

        self.iteration_scores.append({
            'iteration': iteration,
            'best_score': best_score,
            'median_score': median_score,
            'top_half_median': top_half_median,
            'bottom_half_median': bottom_half_median
        })

    def store_iteration_penalties(self, iteration):
        best_sol = self.population[0][0]
        cancelled_pen_num = best_sol.get_cancelled_flights_num()
        training_pen_num = best_sol.get_training_penal_num()
        dayoff_pen_num = best_sol.get_dayoff_penal_num()

        self.iteration_penalties.append({
            'iteration': iteration,
            'cancelled_num': cancelled_pen_num,
            'training_num': training_pen_num,
            'dayoff_num': dayoff_pen_num,
            'location_num': 0,
            'rest_num': 0,
            'overwork_num': 0,
        })

    def evol_algo_loop_with_init(self, iterations_n, filename=None):
        '''
        This evolutionary algorithm loop takes the 50% best solutions from the
        population and mutates them in-place. Afterwards to fill the rest of the 
        population we call add_new_solutions(), which initializes the remaining
        solutions adding them to self.population
        '''
        for i in range(iterations_n):
            self.reset_crew()
            start_time = time.time()
            elite_population = copy.deepcopy(self.population[:len(self.population)//4])
            self.population = self.population[:len(self.population)//2]
            # add new solutions and run them
            self.add_new_solutions(filename)
            for sol_list in self.population:
                sol = sol_list[0]
                sol.scheduler.set_time(0)
                mutation_successful = False
                while not mutation_successful:
                    try:
                        mut_time = self.mutation_whole_crew(sol)
                        mutation_successful = True
                    except ValueError:
                        logging.error(f"Error during mutation. Retrying with a different flight.")
                        print(f"Error during mutation. Retrying with a different flight.")
                sol.initialized = "Mutated    "
                self.reschedule_flights(sol, mut_time, i, config['algo']['ALLOWED_HEURISTIC'])

            self.run_events()
            self.update_all_fitness_scores()
            self.population += elite_population
            self.sort_population()
            self.population = self.population[:len(elite_population) * 4]
            self.print_fitness_scores(i)
            self.store_iteration_scores(i+1)
            self.store_iteration_penalties(i+1)
            end_time = time.time()
            print(f"-----------ITERATION {i} DURATION: {end_time - start_time:.2f}")

    def evol_algo_loop_two_pop(self, iterations_n, filename):
        for i in range(iterations_n):
            start_time = time.time()
            elite_population = copy.deepcopy(self.population[:self.population_size//8])
            self.population = self.population[:self.population_size//2]
            end_time = time.time()
            self.add_new_solutions(filename)
            print(f"-----------ITERATION {i} DURATION: {end_time - start_time:.2f}")
            for sol_list in self.population:
                sol = sol_list[0]
                sol.scheduler.set_time(0)
                mutation_successful = False
                while not mutation_successful:
                    try:
                        mut_time = self.mutation_whole_crew(sol)
                        mutation_successful = True
                    except ValueError:
                        # logging.erorr
                        print("Error during mutation. Retrying with a different flight.")
                sol.initialized = "Mutated    "
                self.reschedule_flights(sol, mut_time, i, config['algo']['ALLOWED_HEURISTIC'])

            for sol_list in self.population:
                sol_list[0].run_events()

            self.population = self.population + elite_population 
            # Update fitness scores of the combined population
            self.update_all_fitness_scores()

            # # Different selection mechanism before and after halfway point
            if i < iterations_n // 2:
                # Ensure at least one solution for each ID is selected
                self.population = self.select_diverse_population(self.population)
            else:
                # Select based on fitness score
                self.population.sort(key=lambda sol: sol[0].fitness_score)
                self.population = self.population[:self.population_size]

            self.sort_population()
            self.print_fitness_scores(i)
            self.store_iteration_scores(i)
            self.store_iteration_penalties(i)

    def reset_crew(self):
        for sol_list in self.population:
            # sol_list[0].flights = []
            for airport in sol_list[0].structures.airports:
                # airport.clear_logs()
                for pilot in airport.pilots:
                    pilot.status = []
                    pilot.flights_taken = 0
                for attendant in airport.attendants:
                    attendant.status = []
                    attendant.flights_taken = 0

    def select_diverse_population(self, population):
        unique_ids = set(sol[0].id for sol in population)
        selected_population = []

        for unique_id in unique_ids:
            # Find the best solution for each ID
            best_sol_for_id = min(
                (sol for sol in population if sol[0].id == unique_id),
                key=lambda sol: sol[0].fitness_score
            )
            selected_population.append(best_sol_for_id)

        # Fill the rest of the population based on fitness score
        remaining_slots = self.population_size - len(selected_population)
        population.sort(key=lambda sol: sol[0].fitness_score)
        selected_population.extend(population[:remaining_slots])

        return selected_population[:self.population_size]

    def reschedule_flights_in_pop(self, sol, mutation_time, population, heuristic):
        # reschedule flights only after the mutation_time
        for sol_list in population:
            sol_list[0].scheduler.set_time(0)
        flights_to_reschedule = [f for f in sol.flights if f.simulation_time > mutation_time]

        for airport in sol.structures.airports:
            airport.check_consistency()

        # remove the affected flights from the original schedule
        for flight in flights_to_reschedule[::-1]:
            flight.reset_state_after_mutation(sol)

        # Add back the flights to the schedule, which will now use the updated availablitity
        for flight in flights_to_reschedule:
            scheduled_time = flight.simulation_time
            sol.scheduler.schedule_event(scheduled_time, flight.start_flight, heuristic)

        self.reset_logs(sol, mutation_time)

    def update_all_fitness_scores_in_pop(self, population):
        '''
        This function uses the fitness_function() method to calculate the fitness score
        of all solutions in the population
        '''
        for sol in population:
            penalties, training_penalties, day_off_penalties = self.fitness_function(
                sol[0])
            sol[1] = [
                penalties, training_penalties, day_off_penalties]
            sol[0].fitness_score = penalties + training_penalties + day_off_penalties
            sol[0].training_penalty = training_penalties
            sol[0].day_off_penalties = day_off_penalties

    def add_new_solutions(self, filename):
        '''This function '''
        self.initialize_population()
        if filename is not None:
            self.assign_schedules_for_initialized_sols_from_json(filename)
        else:
            self.assign_schedules_for_initialized_sols()
        self.run_schedules()
        self.run_events()

    def save_iteration_scores_to_file(self, file_name):
        with open(f'{file_name}_scores.json', 'a') as results_file, open('parameters.json') as params_file:
            results = {'fitness_scores': self.iteration_scores, 'parameters': json.load(params_file)}
            json.dump(results, results_file)

    def save_iteration_penalties_to_file(self, file_name):
        with open(f'{file_name}_penalties.json', 'a') as results_file, open('parameters.json') as params_file:
            results = {'penalties': self.iteration_penalties, 'parameters': json.load(params_file)}
            json.dump(results, results_file)