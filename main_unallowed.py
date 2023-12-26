import json
from src.unallowed_approach.imp_evol_algo import ImpossibleEvolutionaryAlgorithm

def main():
    # from .decorators import timing_decorator
    with open('parameters.json') as parameters_file:
        config = json.load(parameters_file)

    imp_evol_algo = ImpossibleEvolutionaryAlgorithm()

    # initial assignments - made only once
    imp_evol_algo.fill_in_distance_matrix()
    imp_evol_algo.assign_airports_to_crew_members()
    print(f"Imp_evol_algo.pilots_status_pop: {imp_evol_algo.pilots_status_pop}")
    print(f"Imp_evol_algo.attend_status_pop: {imp_evol_algo.attend_status_pop}")
    imp_evol_algo.create_initial_sols()
    imp_evol_algo.generate_training_hours()

    if config['algo']['INITIAL_HEURISTIC'] == "with_update":
        imp_evol_algo.create_initial_generation_with_update()
    elif config['algo']['INITIAL_HEURISTIC'] == "random":
        imp_evol_algo.create_initial_generation_random()
    elif config['algo']['INITIAL_HEURISTIC'] == "no_update":
        imp_evol_algo.create_initial_generation_no_update()
    else:
        raise ValueError(f"In parameters file the initial_heuristic parameters has incorrect value. Choose one of 'with_update', 'random' or 'no_update'")

    imp_evol_algo.update_fitness_for_all_sols()
    initial_penalties = imp_evol_algo.get_penalties_for_sols()
    for i in range(len(imp_evol_algo.population)):
        print(f"START of first gen----")
        imp_evol_algo.print_penalties_for_sols(0, i)
        print(f"END of first gen----")
    imp_evol_algo.print_average_fit_score("A")
    imp_evol_algo.print_fitness_scores(0)
    fit_scores = imp_evol_algo.get_fitness_scores()

    imp_evol_algo.evolutionary_algorithm_loop(config['algo']['N_ITERATIONS'], print_flag=1, initial=fit_scores)
    print(f"Initial fitness values: {fit_scores}")

    print(f"---Final penalties applied---")
    for i in range(len(imp_evol_algo.population)):
        imp_evol_algo.print_penalties_for_sols(config['algo']['N_ITERATIONS']+1, i)

    print(f"---Initial penalties applied---")
    for i in range(len(initial_penalties)):
        print(f"Sol: {i}, Fit: {fit_scores[i]} Loc: {initial_penalties[i][0]}, Rest: {initial_penalties[i][1]}, Canc: {initial_penalties[i][2]}, train_ov: {initial_penalties[i][3]}, Prop. alloc: {initial_penalties[i][4]}")

if __name__ == "__main__":
    main()