import logging
import time
from src.structures import Structures
from src.evolutionary_algorithm import EvolutionaryAlgorithm
from src.decorators import timing_decorator
from debug.test_availability import test_availability
from config import get_args
# from copy import deepcopy
# from src.event_scheduler import EventScheduler
# from memory_profiler import profile


@timing_decorator
# @profile
def main():
    args = get_args()

    if args.log:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
    else:
        logging.basicConfig(level=logging.CRITICAL)

    initial_structures = Structures()
    evol_algo = EvolutionaryAlgorithm(initial_structures, 100)
    evol_algo.initialize_population()
    evol_algo.create_initial_schedule()
    evol_algo.assign_schedules_for_all_sols()
    print(f"Printing events for sol")
    print(evol_algo.save_events_for_sol_by_id(5))
    evol_algo.run_events()
    evol_algo.update_all_fitness_scores()
    evol_algo.print_revenue_and_costs()
    start_time = time.time()
    # initial_population1 = deepcopy(evol_algo.population)
    # initial_population2 = deepcopy(evol_algo.population)
    # initial_population3 = deepcopy(evol_algo.population)
    end_time = time.time()
    print(f"Duration of deepcopying {end_time - start_time}")
    # Sort and print results for Roulette Selection
    print("\nSorted Population using Roulette Selection:")
    evol_algo.roulette_sort()
    for individual in evol_algo.population:
        print(
            f"Individual: {individual[1]}, Fitness Score: {individual[0].fitness_score}")

    print(f"-----------Printing flights for solutions--------")
    evol_algo.population[0][0].print_flights()
    # evol_algo.population[5][0].print_flights()
    test_availability(evol_algo)


if __name__ == "__main__":
    main()
