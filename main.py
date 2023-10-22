import logging
from src.structures import Structures
from src.evolutionary_algorithm import EvolutionaryAlgorithm
from src.decorators import timing_decorator
from copy import deepcopy
from debug.test_availability import test_availability
from config import get_args


@timing_decorator
def main():
    args = get_args()

    if args.log:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
    else:
        logging.basicConfig(level=logging.CRITICAL)

    initial_structures = Structures()
    evol_algo = EvolutionaryAlgorithm(initial_structures, 50)
    evol_algo.initialize_population_and_run_events()
    evol_algo.update_all_fitness_scores()
    evol_algo.print_revenue_and_costs()
    initial_population = deepcopy(evol_algo.population)

    # Sort and print results for Roulette Selection
    print("\nSorted Population using Roulette Selection:")
    evol_algo.roulette_sort()
    for individual in evol_algo.population:
        print(
            f"Individual: {individual[1]}, Fitness Score: {individual[0].fitness_score}")

    evol_algo.population = initial_population

    # Sort and print results for Tournament Selection
    print("\nSorted Population using Tournament Selection:")
    evol_algo.tournament_sort()
    for individual in evol_algo.population:
        print(
            f"Individual: {individual[1]}, Fitness Score: {individual[0].fitness_score}")

    evol_algo.population = initial_population

    # Sort and print results for Rank Selection
    print("\nSorted Population using Rank Selection:")
    evol_algo.rank_sort()
    for individual in evol_algo.population:
        print(
            f"Individual: {individual[1]}, Fitness Score: {individual[0].fitness_score}")

    test_availability(evol_algo)


if __name__ == "__main__":
    main()
