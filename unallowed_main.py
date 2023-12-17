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
    imp_evol_algo.create_initial_sols()

    imp_evol_algo.create_initial_generation()
    # imp_evol_algo.print_population()
    imp_evol_algo.update_fitness_for_all_sols()
    for i in range(len(imp_evol_algo.population)):
        print(f"START of first gen----")
        imp_evol_algo.print_penalties_for_sols(0, i)
        print(f"END of first gen----")
    imp_evol_algo.print_average_fit_score("A")
    imp_evol_algo.print_fitness_scores(0)
    fit_scores = imp_evol_algo.get_fitness_scores()

    imp_evol_algo.evolutionary_algorithm_loop(config['algo']['N_ITERATIONS'])
    print(f"Initial fitness values: {fit_scores}")


if __name__ == "__main__":
    main()