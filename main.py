import time
from src.structures import Structures
from src.evolutionary_algorithm import EvolutionaryAlgorithm
from src.decorators import timing_decorator
from debug.test_availability import test_availability
from config import get_args, setup_logging
# from copy import deepcopy
# from src.event_scheduler import EventScheduler
# from memory_profiler import profile

@timing_decorator
# @profile
def main():
    args = get_args()
    print(f"ARGS: {args.log}")
    setup_logging(args.log)

    initial_structures = Structures()
    evol_algo = EvolutionaryAlgorithm(initial_structures, 100)
    evol_algo.initialize_population()
    # evol_algo.create_initial_schedule()
    evol_algo.assign_schedules_for_all_sols()
    evol_algo.print_population()
    evol_algo.run_schedules()
    evol_algo.print_population()
    evol_algo.print_schedules()
    evol_algo.run_events()
    evol_algo.update_all_fitness_scores()
    evol_algo.print_revenue_and_costs()
    start_time = time.time()
    end_time = time.time()
    print(f"Duration of deepcopying {end_time - start_time}")
    # Sort and print results for Roulette Selection
    print("\nSorted Population using Roulette Selection:")
    evol_algo.roulette_sort()
    for individual in evol_algo.population:
        print(
            f"Individual: {individual[1]}, Fitness Score: {individual[0].fitness_score}")

    test_availability(evol_algo)


if __name__ == "__main__":
    main()
