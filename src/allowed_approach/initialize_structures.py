import json
from src.allowed_approach.structures import Structures
from src.allowed_approach.solution import Solution
from config.logs_and_args import save_to_file
from src.allowed_approach.evol_algo import EvolutionaryAlgorithm

def main():
    with open('parameters.json') as parameters_file:
        config = json.load(parameters_file)
    
    initial_structures = Structures()

    evol_algo = EvolutionaryAlgorithm(
        initial_structures=initial_structures,
        population_size=config['algo']['POPULATION_SIZE'])
    evol_algo.initialize_population()
    evol_algo.assign_schedules_for_initialized_sols()
    evol_algo.run_schedules()

    save_to_file(evol_algo, 'initial_structs/evol_algo_1.pkl')
    save_to_file(Solution.schedulers, 'initial_structs/schedulers_dict.pkl')

if __name__ == "__main__":
    main()