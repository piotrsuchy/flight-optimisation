import json
import copy
from imp_solution import ImpossibleSolution

# from .decorators import timing_decorator
with open('parameters.json') as parameters_file:
    config = json.load(parameters_file)
    
class ImpossibleEvolutionaryAlgorithm:
    def __init__(self):
        self.population = [None for _ in range(config['algo']['POPULATION_SIZE'])]

    def create_initial_sols(self):
        sol = ImpossibleSolution()
        initial_sol_schedule = sol.get_initial_schedule()

        for i in range(len(self.population)):
            sol_schedule = copy.deepcopy(initial_sol_schedule)
            self.population[i] = sol_schedule

    def print_population(self):
        for id, sol in enumerate(self.population):
            print(f"Sol: {id}: {sol}")

    def check_consistency(self):
        key_params = [[flight[0], flight[1], flight[-1]] for flight in self.population[0]]
        for sol in self.population:
            for id, flight in enumerate(sol):
                reference_params = [flight[0], flight[1], flight[-1]]
                if key_params[id] != reference_params:
                    raise ValueError(f"Inconsistent flight data at solution index: {id}. Expected: {key_params[id]}, found: {reference_params}")

def test_main():
    imp_evol_algo = ImpossibleEvolutionaryAlgorithm()
    imp_evol_algo.create_initial_sols()
    imp_evol_algo.print_population()
    imp_evol_algo.check_consistency()
    
test_main()
