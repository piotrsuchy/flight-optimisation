import json
from src.unallowed_approach.imp_evol_algo import ImpossibleEvolutionaryAlgorithm
from src.allowed_approach.visualisation import plot_fitness_scores, plot_penalties
from config.logs_and_args import get_args

def main():
    # from .decorators import timing_decorator
    with open('parameters.json') as parameters_file:
        config = json.load(parameters_file)

    args = get_args()
    if args.file_name is None:
        args.file_name = input("Enter the file name in which to save the plot: ")

    imp_evol_algo = ImpossibleEvolutionaryAlgorithm()

    load_from_file = input("Load structures from file? (yes/no): ")
    if load_from_file.lower() == 'yes':
        filename = input("Enter the filename to load structures: ")
        imp_evol_algo.load_structures(filename)
    else:
        imp_evol_algo.fill_in_distance_matrix()
        imp_evol_algo.assign_airports_to_crew_members()
        imp_evol_algo.create_initial_sols()
        imp_evol_algo.generate_training_hours()
        imp_evol_algo.generate_days_off()

    # Save structures
    save_from_file = input("Save structures to file? (yes/no): ")
    if save_from_file.lower() == 'yes':
        save_filename = input("Enter the filename to save structures: ")
        imp_evol_algo.save_structures(save_filename)

    if config['algo']['UNALL_INITIAL_HEURISTIC'] == "with_update":
        imp_evol_algo.create_initial_generation_with_update()
    elif config['algo']['UNALL_INITIAL_HEURISTIC'] == "random":
        imp_evol_algo.create_initial_generation_random()
    elif config['algo']['UNALL_INITIAL_HEURISTIC'] == "no_update":
        imp_evol_algo.create_initial_generation_no_update()
    else:
        raise ValueError(f"In parameters file the initial_heuristic parameters has incorrect value. Choose one of 'with_update', 'random' or 'no_update'")

    imp_evol_algo.update_fitness_for_all_sols()
    imp_evol_algo.save_initial_scores_and_penalties()
    initial_penalties = imp_evol_algo.get_penalties_for_sols()
    for i in range(len(imp_evol_algo.population)):
        print(f"START of first gen----")
        imp_evol_algo.print_penalties_for_sols(0, i)
        print(f"END of first gen----")
    imp_evol_algo.print_average_fit_score("A")
    imp_evol_algo.print_fitness_scores(0)
    fit_scores = imp_evol_algo.get_fitness_scores()

    imp_evol_algo.evolutionary_algorithm_loop(config['algo']['N_ITERATIONS_UN'], print_flag=1, initial=fit_scores)
    print(f"Initial fitness values: {fit_scores}")

    imp_evol_algo.save_iteration_scores_to_file(args.file_name)
    imp_evol_algo.save_iteration_penalties_to_file(args.file_name)

    print(f"---Final penalties applied---")
    for i in range(len(imp_evol_algo.population)):
        imp_evol_algo.print_penalties_for_sols(config['algo']['N_ITERATIONS_UN']+1, i)

    print(f"---Initial penalties applied---")
    for i in range(len(initial_penalties)):
        print(f"Sol: {i}, Fit: {fit_scores[i]} Loc: {initial_penalties[i][0]}, Rest: {initial_penalties[i][1]}, Canc: {initial_penalties[i][2]}, train_ov: {initial_penalties[i][3]}, overwork: {initial_penalties[i][5]}, days_off: {initial_penalties[i][6]}, Prop. alloc: {initial_penalties[i][4]}")

    if args.file_name:
        plot_fitness_scores(args.file_name)
        plot_penalties(args.file_name)

if __name__ == "__main__":
    main()