import json
from statistics import mean
from src.unallowed_approach.imp_evol_algo import ImpossibleEvolutionaryAlgorithm

def run_experiment(use_update):
    imp_evol_algo = ImpossibleEvolutionaryAlgorithm()

    # Initial setups
    imp_evol_algo.fill_in_distance_matrix()
    imp_evol_algo.assign_airports_to_crew_members()
    imp_evol_algo.create_initial_sols()
    imp_evol_algo.generate_training_hours()

    # Choose the function based on the input parameter
    if use_update:
        imp_evol_algo.create_initial_generation_with_update()
    else:
        imp_evol_algo.create_initial_generation()

    imp_evol_algo.update_fitness_for_all_sols()

    fitness_scores = imp_evol_algo.get_fitness_scores()

    return fitness_scores

def main():
    # from .decorators import timing_decorator
    with open('parameters.json') as parameters_file:
        config = json.load(parameters_file)

    # Run experiment A (without update)
    fitness_scores_A = run_experiment(use_update=False)

    # Run experiment B (with update)
    fitness_scores_B = run_experiment(use_update=True)


    print(f"Without update fit. values: {fitness_scores_A}. Mean: {mean(fitness_scores_A)}")
    print(f"With update fit. values: {fitness_scores_B}. Mean: {mean(fitness_scores_B)}")


if __name__ == "__main__":
    main()