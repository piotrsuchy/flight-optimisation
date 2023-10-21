import copy
import random
import numpy as np
from .solution import Solution
from .passenger_demand import generate_demand_array, visualize_demand

# parameters
TICKET_PRICE = 1000
PLANE_OPERATIONAL_COST_PER_HOUR = 2000
PILOT_COST_PER_HOUR = 120
ATTENDANT_COST_PER_HOUR = 80
FLIGHT_CANCELLATION_COST_PER_PERSON = TICKET_PRICE*1.5
MAX_WEEKLY_HOURS = 60
OVERWORK_PENALTY_PER_HOUR = PILOT_COST_PER_HOUR*2
DEFAULT_PLANE_CAPACITY = 500

class EvolutionaryAlgorithm:
    def __init__(self, initial_structures, population_size=100):
        self.population_size = population_size
        self.population = []
        self.initial_structures = initial_structures
        self.passenger_demand = generate_demand_array(self.initial_structures.airports, 30)


    def initialize_population_and_run_events(self):
        for sol_id in range(self.population_size):
            initial_structures = copy.deepcopy(self.initial_structures)
            sol = Solution(sol_id+1, self.passenger_demand, initial_structures, 720)
            sol.set_sol_ids(sol_id+1)
            sol._schedule_flights(150)
            sol.run_events()
            # population is a list of [sol, [revenue, op_costs, penalties]]
            self.population.append([sol, -1])


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
        for flight in sol.flights:
            if flight.status == "cancelled":
                continue
            
            revenue += flight.passengers * TICKET_PRICE
            
        # 2. Calculate Operational Costs
        for flight in sol.flights:
            if flight.status == "cancelled":
                continue
            flight_duration = flight.duration
            plane_cost = PLANE_OPERATIONAL_COST_PER_HOUR * flight_duration
            pilot_cost = PILOT_COST_PER_HOUR * flight_duration
            attendant_cost = ATTENDANT_COST_PER_HOUR * flight_duration
            operational_costs += plane_cost + 2 * pilot_cost + 4 * attendant_cost  # Assuming 2 pilots and 4 attendants
            
        # 3. Calculate Penalties
        for flight in sol.flights:
            if flight.delay != 0:
                print(f"Sol: {flight.sol.id} Calculating extra penalties for the delay of flight {flight.id}, {flight.delay}h")
                delay_penalty = flight.delay * 2 * PLANE_OPERATIONAL_COST_PER_HOUR
                penalties += delay_penalty
                
            if flight.status == "cancelled":
                from_airport_idx = flight.base_airport.id - 1
                to_airport_idx = flight.destination_airport.id - 1
                day_of_flight = flight.day  # Assuming the Flight class has a day attribute
                demand = self.passenger_demand[from_airport_idx][to_airport_idx][day_of_flight]

                # You can also add an upper limit based on a default plane capacity if required
                filled_seats = min(demand, DEFAULT_PLANE_CAPACITY)

                penalties += FLIGHT_CANCELLATION_COST_PER_PERSON * filled_seats

            try:
                for pilot in flight.pilots:
                    if pilot.week_worked_hs > MAX_WEEKLY_HOURS:
                        penalties += OVERWORK_PENALTY_PER_HOUR * (pilot.week_worked_hs - MAX_WEEKLY_HOURS)
            
                for attendant in flight.attendants:
                    if attendant.week_worked_hs > MAX_WEEKLY_HOURS:
                        penalties += OVERWORK_PENALTY_PER_HOUR * (attendant.week_worked_hs - MAX_WEEKLY_HOURS)
            except TypeError:
                print(f"In sol: {sol.id} in flight: {flight.id} pilots or attendants are None")

        return [revenue, operational_costs, penalties, delay_penalty]


    def roulette_selection(self):
        '''This function selects a solution using roulette wheel selection'''
        total_fitness = sum(sol[0].fitness_score for sol in self.population)
        selection_probabilities = [sol[0].fitness_score / total_fitness for sol in self.population]
        selected_index = np.random.choice(len(self.population), p=selection_probabilities)
        return self.population[selected_index]


    def tournament_selection(self, tournament_size=5):
        '''This function selects a solution using tournament selection'''
        selected_tournament = random.sample(self.population, tournament_size)
        best_in_tournament = max(selected_tournament, key=lambda sol: sol[0].fitness_score)
        return best_in_tournament


    def rank_selection(self):
        '''This function selects a solution using rank selection'''
        sorted_population = sorted(self.population, key=lambda sol: sol[0].fitness_score)
        rank_sum = len(sorted_population) * (len(sorted_population) + 1) / 2
        rank_probabilities = [(i + 1) / rank_sum for i in range(len(sorted_population))]
        selected_index = np.random.choice(len(sorted_population), p=rank_probabilities)
        return sorted_population[selected_index]


    def roulette_sort(self):
        '''This function sorts the population using repeated roulette wheel selection'''
        sorted_population = []
        while len(sorted_population) < len(self.population):
            selected = self.roulette_selection()
            sorted_population.append(selected)
            self.population.remove(selected)
        self.population = sorted_population


    def tournament_sort(self, tournament_size=5):
        '''This function sorts the population using repeated tournament selection'''
        sorted_population = []
        while len(sorted_population) < len(self.population):
            best_in_tournament = self.tournament_selection(tournament_size)
            sorted_population.append(best_in_tournament)
            self.population.remove(best_in_tournament)
        self.population = sorted_population


    def rank_sort(self):
        '''This function sorts the population using rank selection (simply by fitness value)'''
        self.population = sorted(self.population, key=lambda sol: sol[0].fitness_score, reverse=True)


    def update_all_fitness_scores(self):
        '''
        This function uses the fitness_function() method to calculate the fitness score
        of all solutions in the population
        '''
        for sol_id, sol in enumerate(self.population):
            revenue, operation_costs, penalties, delay_penalty = self.fitness_function(sol[0])
            self.population[sol_id][1] = [revenue, operation_costs, penalties, delay_penalty]
            self.population[sol_id][0].fitness_score = revenue - operation_costs - penalties

            
    def print_revenue_and_costs(self):
        for sol in self.population:
            print(f"Sol: {sol[0]}, rev: {sol[1][0]:.2e}, op_costs: {sol[1][1]:.2e}, penalties: {sol[1][2]:.2e}, delay_penalties: {sol[1][2]:.2e}")