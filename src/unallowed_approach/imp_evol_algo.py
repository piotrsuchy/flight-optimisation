import json
import random
import numpy as np
import copy
import math
from src.unallowed_approach.imp_solution import ImpossibleSolution

with open('parameters.json') as parameters_file:
    config = json.load(parameters_file)

location_penalty = config['pen']['LOCATION_PENALTY']
rest_penalty = config['pen']['REST_PENALTY']
cancellation_penalty = config['pen']['CANCEL_PENALTY']
training_overlap_penalty = config['pen']['TRAINING_OVERLAP_PENALTY']
plane_speed = config['structs']['PLANE_SPEED']
    
class ImpossibleEvolutionaryAlgorithm:

    def __init__(self):
        self.pop_size = config['algo']['POPULATION_SIZE']
        self.pilots_per_sol = config['structs']['N_PILOTS_F_A'] * config['structs']['N_AIRPORTS'] 
        self.attend_per_sol = config['structs']['N_ATTENDANTS_F_A'] * config['structs']['N_AIRPORTS']
        self.n_airports = config['structs']['N_AIRPORTS']
        self.mutation_rate = config['algo']['MUTATION_RATE']
        self.crossover_rate = config['algo']['CROSSOVER_RATE']
        self.selection_rate = config['algo']['SELECTION_RATE']

        self.distance_matrix = [[None for _ in range(self.n_airports)] for _ in range(self.n_airports)]
        self.population = [None for _ in range(self.pop_size)]
        self.pilots_status_pop = [[{'location': None, 'time': 0, 'train_hs': []} 
                                for _ in range(self.pilots_per_sol)]
                                for _ in range(self.pop_size)]
        self.attend_status_pop = [[{'location': None, 'time': 0, 'train_hs': []} 
                                for _ in range(self.attend_per_sol)]
                                for _ in range(self.pop_size)]
        self.fitness_scores = [None for _ in range(self.pop_size)]

        self.loc_penalty_count = 0
        self.canc_penalty_count = 0
        self.rest_penalty_count = 0
        self.overlap_penalty_count = 0
        self.loc_proper_allocation = 0
        self.all_sols_penalty_count = []

    def print_distance_matrix(self):
        for row in self.distance_matrix:
            print(row)

    def print_population(self):
        print(f"--- PRINTING THE POPULATION ---")
        for id, sol in enumerate(self.population):
            print(f"Sol: {id}: ")
            for flight in sol:
                print(flight)

    def print_fitness_scores(self, iter):
        print(f"--- PRINTING FITNESS SCORES FOR ITER: {iter} ---")
        for sol_id, fit_score in enumerate(self.fitness_scores):
            print(f"Sol: {sol_id}, fit_score: {fit_score}")

    def print_best_score(self):
        max_fit_score = math.inf
        for fit_score in self.fitness_scores:
            max_fit_score = min(fit_score, max_fit_score)
        print(f"---PRINTING BEST FITNESS SCORE: {max_fit_score}")

    def print_average_fit_score(self, iter):
        avg_fit_score = np.average(self.fitness_scores)
        print(f"Iteration: {iter}", avg_fit_score)

    def print_penalty_counts(self):
        print("Printing penalty counts:")
        print("Location pen.: ", self.loc_penalty_count)
        print("Cancellation pen.: ", self.canc_penalty_count)
        print("Rest pen.: ", self.rest_penalty_count)
        print("Training overlap pen.: ", self.overlap_penalty_count)

    def print_penalties_for_sols(self, iter, sol_id):
        print(f"Sol: {sol_id}, Fit: {self.fitness_scores[sol_id]} Loc: {self.all_sols_penalty_count[sol_id][0]}, Rest: {self.all_sols_penalty_count[sol_id][1]}, Canc: {self.all_sols_penalty_count[sol_id][2]}, training overlap: {self.all_sols_penalty_count[sol_id][3]}, Prop. alloc: {self.all_sols_penalty_count[sol_id][4]}")

    def get_fitness_scores(self):
        fitness_score = []
        for fit_score in self.fitness_scores:
            fitness_score.append(fit_score)
        return fitness_score

    def get_penalties_for_sols(self):
        return self.all_sols_penalty_count

    def generate_training_hours(self):
        for sol in range(self.pop_size):
            random.seed(config['structs']['SEED_1'])
            for pilot in range(self.pilots_per_sol):
                training_start_time = random.randint(0, 720)
                self.pilots_status_pop[sol][pilot]['train_hs'] = [training_start_time, training_start_time + 24]
            for attendant in range(self.attend_per_sol):
                training_start_time = random.randint(0, 720)
                self.attend_status_pop[sol][attendant]['train_hs'] = [training_start_time, training_start_time + 24]
            random.seed(None)
        
    def create_initial_sols(self):
        sol = ImpossibleSolution()
        initial_sol_schedule = sol.get_initial_schedule()

        for i in range(len(self.population)):
            sol_schedule = copy.deepcopy(initial_sol_schedule)
            self.population[i] = sol_schedule
        self.sort_population()

    def sort_population(self):
        for sol in self.population:
            sol.sort(key=lambda flight: flight[-1])
            
    def fill_in_distance_matrix(self):
        '''Creation of a triangular matrix of distances to save space'''
        for i in range(config['structs']['N_AIRPORTS']):
            for j in range(0, i):
                distance = random.randint(1000, 44700)
                self.distance_matrix[i][j] = distance
                self.distance_matrix[j][i] = distance

    def check_consistency(self):
        key_params = [[flight[0], flight[1], flight[-1]] for flight in self.population[0]]
        for sol in self.population:
            for id, flight in enumerate(sol):
                reference_params = [flight[0], flight[1], flight[-1]]
                if key_params[id] != reference_params:
                    raise ValueError(f"Inconsistent flight data at solution index: {id}. Expected: {key_params[id]}, found: {reference_params}")

    def reset_crew_member_times_for_sol(self, sol_id):
        # Reset time for all pilots and attendants in given solution
        for pilot in self.pilots_status_pop[sol_id]:
            pilot['time'] = 0
        for attendant in self.attend_status_pop[sol_id]:
            attendant['time'] = 0
   
    def calculate_fitness(self, solution, sol_id, pilot_status, attendant_status):
        self.canc_penalty_count = 0
        self.loc_penalty_count = 0
        self.rest_penalty_count = 0
        self.loc_proper_allocation = 0
        self.overlap_penalty_count = 0
        fitness_score = 0

        self.reset_crew_member_times_for_sol(sol_id)

        for flight_id, flight in enumerate(solution):
            src_id, dst_id, *crew_members, penalties, timestamp = flight

            loc_penalties = 0
            rest_penalties = 0

            if None in crew_members:
                self.canc_penalty_count += 1
                fitness_score += cancellation_penalty
                # calculate penalty for training overlap 
                self.population[sol_id][flight_id][8] = [loc_penalties, rest_penalties]
                continue

            flight_duration = self.distance_matrix[src_id - 1][dst_id - 1] // plane_speed
            required_rest_time = min(8, flight_duration)

            for idx, crew_member_idx in enumerate(crew_members):
                if crew_member_idx is not None:

                    # determine if the crew member is a pilot or an attendant
                    if idx < config['structs']['PILOTS_PER_PLANE']:
                        crew_member_status = pilot_status[crew_member_idx - 1]  # Adjust the index if necessary
                    else:
                        crew_member_status = attendant_status[crew_member_idx - 1]  # Adjust the index if necessary

                    # calculate penalty for wrong location
                    if crew_member_status['location'] != src_id:
                        self.loc_penalty_count += 1
                        loc_penalties += 1
                        fitness_score += location_penalty
                    else:
                        self.loc_proper_allocation += 1

                    # calculate penalty for lack of rest time
                    if timestamp - crew_member_status['time'] < required_rest_time:
                        rest_penalties += 1
                        self.rest_penalty_count += 1
                        fitness_score += rest_penalty

                    if idx < config['structs']['PILOTS_PER_PLANE']:
                        self.pilots_status_pop[sol_id][crew_member_idx - 1]['location'] = dst_id
                        self.pilots_status_pop[sol_id][crew_member_idx - 1]['time'] = timestamp + flight_duration
                    else:
                        self.attend_status_pop[sol_id][crew_member_idx - 1]['location'] = dst_id
                        self.attend_status_pop[sol_id][crew_member_idx - 1]['time'] = timestamp + flight_duration

                    # calculate penalty for training overlap 
                    self.population[sol_id][flight_id][8] = [loc_penalties, rest_penalties]

                    if timestamp > crew_member_status['train_hs'][0] and timestamp < crew_member_status['train_hs'][1] or \
                    timestamp + flight_duration > crew_member_status['train_hs'][0] and timestamp + flight_duration <= crew_member_status['train_hs'][1]:
                        self.overlap_penalty_count += 1
                        fitness_score += training_overlap_penalty
                        
        self.all_sols_penalty_count.append((self.loc_penalty_count, self.rest_penalty_count, self.canc_penalty_count, self.overlap_penalty_count, self.loc_proper_allocation))
        return fitness_score
    
    def fix_location_heuristic_for_all(self, solutions):
        modified_solutions = []
        for sol_id, sol in enumerate(solutions):
            modified_sol = self.fix_location_heuristic(sol, sol_id)
            modified_solutions.append(modified_sol)
        return modified_solutions

    def fix_location_heuristic(self, solution, sol_id):
        penalized_flights = sorted(enumerate(solution), key=lambda x: x[1][8][0], reverse=True)
        # print(f"Penalized flights: {penalized_flights}")

        top_penalized_flights = penalized_flights[:max(1, len(penalized_flights) // 10)]
        # print(f"Top penalized flights: {top_penalized_flights}")

        for flight_id, flight in top_penalized_flights:
            # print(f"flight_id: {flight_id}")
            # print(f"flight: {flight}")
            src_id, _, *_, penalties, _ = flight
            if penalties[0] == 0:
                continue
            
            new_flight_id = flight_id - 1
            # print(f"New flight id: {new_flight_id}")
            while new_flight_id >= 0 and solution[new_flight_id][1] != src_id:
                new_flight_id -= 1
            
            if new_flight_id >= 0 and solution[new_flight_id][1] == src_id:
                new_crew = solution[new_flight_id][2:8]
                solution[flight_id][2:8] = new_crew
        return solution
        
    def update_fitness_for_all_sols(self):
        self.all_sols_penalty_count = []
        for sol_id, sol in enumerate(self.population):
            fitness_score = self.calculate_fitness(sol, sol_id, self.pilots_status_pop[sol_id], self.attend_status_pop[sol_id])
            self.fitness_scores[sol_id] = fitness_score
    
    def create_initial_generation_no_update(self):
        '''
        Assigns pilots and attendants to flights in a random but allowed fashion
        '''
        for sol_idx, sol in enumerate(self.population):
            for flight in sol:
                src_id = flight[0]

                # Assign pilots
                available_pilots = [idx for idx, status in enumerate(self.pilots_status_pop[sol_idx]) if status['location'] == src_id]
                for slot in range(config['structs']['PILOTS_PER_PLANE']):
                    if available_pilots:
                        chosen_idx = random.choice(available_pilots)
                        flight[2 + slot] = chosen_idx + 1  
                        available_pilots.remove(chosen_idx)

                # Assign attendants
                available_attendants = [idx for idx, status in enumerate(self.attend_status_pop[sol_idx]) if status['location'] == src_id]
                for slot in range(config['structs']['PILOTS_PER_PLANE'], config['structs']['PILOTS_PER_PLANE'] + config['structs']['ATTEND_PER_PLANE']):
                    if available_attendants:
                        chosen_idx = random.choice(available_attendants)
                        flight[2 + slot] = chosen_idx + 1  
                        available_attendants.remove(chosen_idx)
    
    def create_initial_generation_random(self):
        '''
        Assigns pilots and attendants to flights in a completely random fashion
        '''
        for sol_idx, sol in enumerate(self.population):
            for flight in sol:
                # Assign pilots
                available_pilots = [idx for idx in range(len(self.pilots_status_pop[sol_idx]))]
                for slot in range(config['structs']['PILOTS_PER_PLANE']):
                    if available_pilots:
                        chosen_idx = random.choice(available_pilots)
                        flight[2 + slot] = chosen_idx + 1  
                        available_pilots.remove(chosen_idx)

                # Assign attendants
                available_attendants = [idx for idx in range(len(self.attend_status_pop[sol_idx]))]
                for slot in range(config['structs']['PILOTS_PER_PLANE'], config['structs']['PILOTS_PER_PLANE'] + config['structs']['ATTEND_PER_PLANE']):
                    if available_attendants:
                        chosen_idx = random.choice(available_attendants)
                        flight[2 + slot] = chosen_idx + 1  
                        available_attendants.remove(chosen_idx)

    def create_initial_generation_with_update(self):
        '''
        Assigns pilots and attendants to flights in a random but allowed fashion
        '''
        for sol_idx, sol in enumerate(self.population):
            initial_pilots_status_pop = copy.deepcopy(self.pilots_status_pop)
            initial_attend_status_pop = copy.deepcopy(self.attend_status_pop)
            for flight in sol:
                src_id = flight[0]
                dest_id = flight[1]

                # Assign pilots
                available_pilots = [idx for idx, status in enumerate(self.pilots_status_pop[sol_idx]) if status['location'] == src_id]
                for slot in range(config['structs']['PILOTS_PER_PLANE']):
                    if available_pilots:
                        chosen_idx = random.choice(available_pilots)
                        flight[2 + slot] = chosen_idx + 1  
                        self.pilots_status_pop[sol_idx][chosen_idx]['location'] = dest_id
                        available_pilots.remove(chosen_idx)

                # Assign attendants
                available_attendants = [idx for idx, status in enumerate(self.attend_status_pop[sol_idx]) if status['location'] == src_id]
                for slot in range(config['structs']['PILOTS_PER_PLANE'], config['structs']['PILOTS_PER_PLANE'] + config['structs']['ATTEND_PER_PLANE']):
                    if available_attendants:
                        chosen_idx = random.choice(available_attendants)
                        flight[2 + slot] = chosen_idx + 1  
                        self.attend_status_pop[sol_idx][chosen_idx]['location'] = dest_id
                        available_attendants.remove(chosen_idx)
            self.pilots_status_pop = initial_pilots_status_pop
            self.attend_status_pop = initial_attend_status_pop

    def assign_airports_to_crew_members(self):
        '''
        Assigns the same airports to pilots and attendants in self.pilots_status_pop
        and self.attend_status_pop for each solution
        '''
        random.seed(config['structs']['SEED_1'])

        # Generate a fixed set of locations for all pilots and attendants
        pilot_locations = [random.randint(1, config['structs']['N_AIRPORTS']) for _ in range(self.pilots_per_sol)]
        attendant_locations = [random.randint(1, config['structs']['N_AIRPORTS']) for _ in range(self.attend_per_sol)]

        # Assign these locations to each pilot and attendant in every solution
        for status_pilots, status_attendants in zip(self.pilots_status_pop, self.attend_status_pop):
            for pilot_status, location in zip(status_pilots, pilot_locations):
                pilot_status['location'] = location

            for attendant_status, location in zip(status_attendants, attendant_locations):
                attendant_status['location'] = location

        random.seed(None)


    def reset_state_of_status_pops(self):
        self.assign_airports_to_crew_members()

    def select_solutions(self):
        num_to_select = int(self.pop_size * self.selection_rate)
        solutions_with_scores = list(zip(self.population, self.fitness_scores))

        solutions_with_scores.sort(key=lambda x: x[1], reverse=False)
        selected_solutions = [solution for solution, _ in solutions_with_scores[:num_to_select]]
        return selected_solutions

    def crossover_solutions(self, selected_solutions):
        new_solutions = []

        # Ensure we have an even number of solutions to pair up for crossover
        if len(selected_solutions) % 2 != 0:
            selected_solutions.pop()
        while selected_solutions:
                # Randomly pair up solutions
                parent1 = selected_solutions.pop(random.randrange(len(selected_solutions)))
                parent2 = selected_solutions.pop(random.randrange(len(selected_solutions)))

                if random.random() < self.crossover_rate:
                    # Perform crossover
                    crossover_point = random.randint(1, len(parent1) - 2)  # Choose a random crossover point, but not at the ends

                    # Create children by swapping flights from crossover point
                    child1 = parent1[:crossover_point] + parent2[crossover_point:]
                    child2 = parent2[:crossover_point] + parent1[crossover_point:]

                    new_solutions.extend([child1, child2])
                else:
                    # If crossover doesn't occur, keep parents in the new population
                    new_solutions.extend([parent1, parent2])

        return new_solutions

    def informed_mutate_solution(self, solution):
        '''select two distinct flights but in an informed manner
        to minimize the location penalties - that means, select flights
        that have the same source and destination for example or something like this'''
        pass
    
    def informed_mutate_solutions(self, solutions):
        '''Use informed mutate_solution'''
        mutated_solutions = []
        for sol in solutions:
            if random.random() < self.mutation_rate:
                mutated_sol = self.informed_mutate_solution(sol)
                mutated_solutions.append(mutated_sol)
            else:
                mutated_solutions.append(sol)
        return mutated_solutions

    def informed_mutate_solution_from_all(self, solution, n_flights):
        '''select some random flights (number selected equal to n_flights)
        and mutate the solutions in an informed manner - so not totally random
        but instead '''
        pass
        
    def informed_mutate_solutions_from_all(self, solutions, n_flights):
        mutated_solutions = []
        for sol in solutions:
            if random.random() < self.mutation_rate:
                mutated_sol = self.informed_mutate_solution_from_all(sol, n_flights)
                mutated_solutions.append(mutated_sol)
            else:
                mutated_solutions.append(sol)
        return mutated_solutions

    def mutate_solution(self, solution):
        '''Randomly select two distinct flights and swap their crew assignment'''
        if len(solution) > 1:
            flight_indexes = random.sample(range(len(solution)), 2)
            flight1_idx, flight2_idx = flight_indexes[0], flight_indexes[1]

            solution[flight1_idx][2:-1], solution[flight2_idx][2:-1] = solution[flight2_idx][2:-1], solution[flight1_idx][2:-1]

        return solution

    def mutate_solutions(self, solutions):
        mutated_solutions = []
        for sol in solutions:
            if random.random() < self.mutation_rate:
                mutated_sol = self.mutate_solution(sol)
                mutated_solutions.append(mutated_sol)
            else:
                mutated_solutions.append(sol)
        return mutated_solutions

    def mutate_solution_from_all(self, solution, n_flights):
        '''select a random flight and change the crew member from one 
        change the assigned crew members to random unassigned crew_member'''
        flight_indexes = random.sample(range(len(solution)), n_flights)
        for idx in flight_indexes:
            pilot_slot = random.choice([2, 3])
            solution[idx][pilot_slot] = random.randint(1, self.pilots_per_sol)
            attendant_slot = random.choice([4, 5, 6, 7])
            solution[idx][attendant_slot] = random.randint(1, self.attend_per_sol)

        return solution
        
    def mutate_solutions_from_all(self, solutions, n_flights):
        mutated_solutions = []
        for sol in solutions:
            if random.random() < self.mutation_rate:
                mutated_sol = self.mutate_solution_from_all(sol, n_flights)
                mutated_solutions.append(mutated_sol)
            else:
                mutated_solutions.append(sol)
        return mutated_solutions

    def evolutionary_algorithm_loop(self, n_iterations, print_flag, initial=None):
        '''
        selection based on the fitness function
        from the chosen solutions mutate the solution with some probability
        from the chosen solutions crossover the solutions with some probability
        '''
        for i in range(n_iterations):
            top_solutions = self.select_solutions()
            to_crossover = copy.deepcopy(top_solutions)

            # Perform crossover and mutation on copies of these top solutions
            new_solutions = self.crossover_solutions(to_crossover)
            # 50 / 50 mutation rate for two types of mutation operators
            if random.random() < 0.5:
                mutated_new_solutions = self.mutate_solutions(new_solutions)
            else:
                mutated_new_solutions = self.mutate_solutions_from_all(new_solutions, config['algo']['N_FLIGHTS_TO_MUT'])
            
            location_fixed_solutions = self.fix_location_heuristic_for_all(mutated_new_solutions)
            # Combine the top 50% of the original population with the new solutions
            self.population = top_solutions + location_fixed_solutions 

            # Update fitness scores for the entire population
            self.update_fitness_for_all_sols()
            # self.print_average_fit_score(i)
            if print_flag:
                self.print_fitness_scores(i)
                self.print_best_score()
                print(f"Initial sols: {initial}")
            # for j in range(len(self.population)):
            #     self.print_penalties_for_sols(i, j)
            self.reset_state_of_status_pops()
            