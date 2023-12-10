import json
import random
import copy
from imp_solution import ImpossibleSolution

# from .decorators import timing_decorator
with open('parameters.json') as parameters_file:
    config = json.load(parameters_file)

location_penalty = config['pen']['LOCATION_PENALTY']
rest_penalty = config['pen']['REST_PENALTY']
cancellation_penalty = config['pen']['CANCEL_PENALTY']
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
        self.pilots_status_pop = [[{'location': None, 'time': 0} 
                                for _ in range(self.pilots_per_sol)]
                                for _ in range(self.pop_size)]
        self.attend_status_pop = [[{'location': None, 'time': 0} 
                                for _ in range(self.attend_per_sol)]
                                for _ in range(self.pop_size)]
        self.fitness_scores = [None for _ in range(self.pop_size)]

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

    def print_distance_matrix(self):
        for row in self.distance_matrix:
            print(row)

    def print_population(self):
        for id, sol in enumerate(self.population):
            print(f"Sol: {id}: ")
            for flight in sol:
                print(flight)

    def check_consistency(self):
        key_params = [[flight[0], flight[1], flight[-1]] for flight in self.population[0]]
        for sol in self.population:
            for id, flight in enumerate(sol):
                reference_params = [flight[0], flight[1], flight[-1]]
                if key_params[id] != reference_params:
                    raise ValueError(f"Inconsistent flight data at solution index: {id}. Expected: {key_params[id]}, found: {reference_params}")
    
    def calculate_fitness(self, solution, pilot_status, attendant_status):
        fitness_score = 0

        for flight in solution:
            src_id, dst_id, *crew_members, timestamp = flight

            if None in crew_members:
                fitness_score -= cancellation_penalty
                continue  # Skip the rest of the checks for this flight
            flight_duration = self.distance_matrix[src_id - 1][dst_id - 1] // plane_speed
            required_rest_time = min(8, flight_duration)

            for idx, crew_member_idx in enumerate(crew_members):
                if crew_member_idx is not None:
                    print(f"Debug: crew_member_idx={crew_member_idx}, len(pilot_status)={len(pilot_status)} len(pilot_status[0])={len(pilot_status[0])}")
                    # Determine if the crew member is a pilot or an attendant
                    if idx < config['structs']['PILOTS_PER_PLANE']:
                        crew_member_status = pilot_status[crew_member_idx - 1]  # Adjust the index if necessary
                    else:
                        crew_member_status = attendant_status[crew_member_idx - 1]  # Adjust the index if necessary
                    # print(f"Crew member {crew_member_idx} location: {crew_member_status['location']} :::: should be: {src_id}")
                    # print(f"Crew member rest_time: {timestamp - crew_member_status['time']}")

                    if crew_member_status['location'] != src_id:
                        # print(f"Location penalty applied for flight from {flight[0]} to {flight[1]} - crew_member: {crew_member_idx}")
                        # print(f"Crew member location: {crew_member_status['location']}")
                        fitness_score -= location_penalty

                    if timestamp - crew_member_status['time'] < required_rest_time:
                        # print(f"Rest penalty applied for flight from {flight[0]} to {flight[1]} - crew_member: {crew_member_idx}")
                        # print(f"Crew member rest_time: {timestamp - crew_member_status['time']}")
                        fitness_score -= rest_penalty

                    crew_member_status['location'] = dst_id
                    crew_member_status['time'] = timestamp + flight_duration

        return fitness_score
    
    def update_fitness_for_all_sols(self):
        for i, sol in enumerate(self.population):
            fitness_score = self.calculate_fitness(sol, self.pilots_status_pop[i], self.attend_status_pop[i])
            self.fitness_scores[i] = fitness_score
    
    def create_initial_generation(self):
        '''
        Assigns pilots and attendants to flights in a random but allowed fashion
        '''
        for sol_idx, sol in enumerate(self.population):
            for flight in sol:
                src_id = flight[0]

                # Assign pilots
                available_pilots = [idx for idx, status in enumerate(self.pilots_status_pop[sol_idx]) if status['location'] == src_id]
                # print(f"For flight from {flight[0]} to {flight[1]} available pilots: {available_pilots}")
                # for idx in available_pilots:
                #     print(f"Current location of pilot with id: {idx} -- {self.pilots_status_pop[sol_idx][idx]['location']}")
                for slot in range(config['structs']['PILOTS_PER_PLANE']):
                    if available_pilots:
                        chosen_idx = random.choice(available_pilots)
                        flight[2 + slot] = chosen_idx + 1  # +1 if pilot IDs start from 1
                        available_pilots.remove(chosen_idx)

                # Assign attendants
                available_attendants = [idx for idx, status in enumerate(self.attend_status_pop[sol_idx]) if status['location'] == src_id]
                # print(f"For flight from {flight[0]} to {flight[1]} available attendants: {available_attendants}")
                # for idx in available_attendants:
                #     print(f"Current location of attendant with id: {idx} -- {self.attend_status_pop[sol_idx][idx]['location']}")
                for slot in range(config['structs']['PILOTS_PER_PLANE'], config['structs']['PILOTS_PER_PLANE'] + config['structs']['ATTEND_PER_PLANE']):
                    if available_attendants:
                        chosen_idx = random.choice(available_attendants)
                        flight[2 + slot] = chosen_idx + 1  # +1 if attendant IDs start from 1
                        available_attendants.remove(chosen_idx)

    def assign_airports_to_crew_members(self):
        '''
        Assigns the airports to pilots and attendants in self.pilots_status_pop
        and self.attend_status_pop
        '''
        random.seed(config['structs']['SEED_1'])

        for status_pilots, status_attendants in zip(self.pilots_status_pop, self.attend_status_pop):
            for pilot_status in status_pilots:
                pilot_status['location'] = random.randint(1, config['structs']['N_AIRPORTS'])

            for attendant_status in status_attendants:
                attendant_status['location'] = random.randint(1, config['structs']['N_AIRPORTS'])

        random.seed(None)

    def select_solutions(self):
        num_to_select = int(self.pop_size * self.selection_rate)
        solutions_with_scores = list(zip(self.population, self.fitness_scores))

        solutions_with_scores.sort(key=lambda x: x[1])
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

                if random.random() < 1:
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

    def combine_populations(self, new_solutions):
        # Combine and sort the entire population (old + new) based on fitness
        combined_population = self.population + new_solutions
        for i, sol in enumerate(combined_population):
            fitness_score = self.calculate_fitness(sol, self.pilots_status_pop[i], self.attend_status_pop[i])
            # sort the population by fitness score but don't update the self.fitness_score just yet
            
        # combined_population.sort(key=lambda sol: self.calculate_fitness(sol, self.pilots_status_pop, self.attend_status_pop))
        
        # Select the top solutions to form the new population
        return combined_population[:self.pop_size]

    def mutate_solution(self, solution):
        # Randomly select two distinct flights
        if len(solution) > 1:
            flight_indexes = random.sample(range(len(solution)), 2)
            flight1_idx, flight2_idx = flight_indexes[0], flight_indexes[1]
            print(f"Chosen flights before mutation:")
            print(solution[flight1_idx])
            print(solution[flight2_idx])

            # Swap crew assignments between the two flights
            # Assuming crew assignments are from index 2 to the second last index
            solution[flight1_idx][2:-1], solution[flight2_idx][2:-1] = solution[flight2_idx][2:-1], solution[flight1_idx][2:-1]

            # Print the flights after mutation for verification 
            print(f"Mutated Flights:")
            print(solution[flight1_idx])
            print(solution[flight2_idx])

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


    def evolutionary_algorithm_loop(self, n_iterations):
        '''
        selection based on the fitness function
        from the chosen solutions mutate the solution with some probability
        from the chosen solutiosn crossover the solutions with some probability
        '''
        for _ in range(n_iterations):
            # selection
            selected_solutions = self.select_solutions()
            # crossover
            new_solutions = self.crossover_solutions(selected_solutions)
            mutated_new_solutions = self.mutate_solutions(new_solutions)
            self.population = self.combine_populations(mutated_new_solutions) 
            # self.update_fitness_for_all_sols()


def test_main():
    imp_evol_algo = ImpossibleEvolutionaryAlgorithm()

    # initial assignments - made only once
    imp_evol_algo.fill_in_distance_matrix()
    imp_evol_algo.assign_airports_to_crew_members()
    imp_evol_algo.create_initial_sols()

    imp_evol_algo.create_initial_generation()
    imp_evol_algo.print_population()
    imp_evol_algo.update_fitness_for_all_sols()

    # imp_evol_algo.evolutionary_algorithm_loop(100)

    solutions = imp_evol_algo.select_solutions()
    new_solutions = imp_evol_algo.crossover_solutions(solutions)
    mutated_new_solutions = imp_evol_algo.mutate_solutions(new_solutions)

    imp_evol_algo.population = imp_evol_algo.combine_populations(mutated_new_solutions)
    print("Population after crossover and mutation: ")
    imp_evol_algo.print_population()
    imp_evol_algo.update_fitness_for_all_sols()
    
test_main()
