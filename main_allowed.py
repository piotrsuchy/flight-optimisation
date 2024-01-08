import json
from src.allowed_approach.structures import Structures
from src.allowed_approach.solution import Solution
from src.allowed_approach.evol_algo import EvolutionaryAlgorithm
from src.allowed_approach.visualisation import plot_fitness_scores, plot_penalties
from config.logs_and_args import get_args, setup_logging, load_from_file

def main():
    with open('parameters.json') as parameters_file:
        config = json.load(parameters_file)

    args = get_args()
    if args.file_name is None:
        args.file_name = input("Enter the file name in which to save the plot: ")
    setup_logging(args.log)

    if args.pickle == "json":
        structs_filename = input("What is the name of the json file you want to load?")
        initial_structures = Structures(filename=f'{structs_filename}')
        evol_algo = EvolutionaryAlgorithm(
            initial_structures=initial_structures,
            population_size=config['algo']['POPULATION_SIZE'])
        evol_algo.initialize_population()
        evol_algo.assign_schedules_for_initialized_sols_from_json(f'{structs_filename}')
        evol_algo.run_schedules()
    elif args.pickle:
        print(f"Loading the structures and schedules from file: {args.pickle}")
        evol_algo = load_from_file(args.pickle)
        Solution.schedulers = load_from_file('initial_structs/schedulers_dict.pkl')
    else:
        print(f"Initializing random structures and schedules based on a seed")
        initial_structures = Structures()
        initial_structures.fill_in_distance_matrix()
        evol_algo = EvolutionaryAlgorithm(
            initial_structures=initial_structures,
            population_size=config['algo']['POPULATION_SIZE'])
        evol_algo.initialize_population()
        evol_algo.assign_schedules_for_initialized_sols()
        evol_algo.run_schedules()

    evol_algo.run_events()
    evol_algo.update_all_fitness_scores()
    evol_algo.save_initial_scores_and_penalties()
    evol_algo.sort_population()
    evol_algo.print_fitness_scores(0)

    '''evolutionary algorithm loop with initializing new populations
    at each loop and keeping best 50% of solutions, mutating whole pop
    and keeping a copy of elite pop - best 25% to save best'''
    if config['algo']['ALLOWED_GEN_CREATION'] == 'with_init':
        evol_algo.evol_algo_loop_with_init(config['algo']['N_ITERATIONS_AL'])
    elif config['algo']['ALLOWED_GEN_CREATION'] == 'two_pop':
        evol_algo.evol_algo_loop_two_pop(config['algo']['N_ITERATIONS_AL'])
    else:
        raise ValueError(f"ALLOWED_GEN_CREATION in parameters.json has to be either 'with_init' or 'two_pop'")

    print(f"----------------------------------------------------------------")
    evol_algo.print_all_info()

    evol_algo.save_iteration_scores_to_file(args.file_name)
    evol_algo.save_iteration_penalties_to_file(args.file_name)

    if args.file_name:
        plot_fitness_scores(args.file_name)
        plot_penalties(args.file_name)
    

if __name__ == "__main__":
    main()
