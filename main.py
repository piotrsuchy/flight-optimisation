import time
import json
from src.structures import Structures
from src.evol_algo import EvolutionaryAlgorithm
from src.decorators import timing_decorator
from debug.test_availability import test_availability
from config.logs_and_args import get_args, setup_logging
# from memory_profiler import profile

# @timing_decorator
# @profile


def main():
    with open('parameters.json') as parameters_file:
        config = json.load(parameters_file)

    args = get_args()
    # print(f"ARGS: {args.log}")
    setup_logging(args.log)

    initial_structures = Structures()

    # initial population
    evol_algo = EvolutionaryAlgorithm(
        initial_structures=initial_structures,
        population_size=config['algo']['POPULATION_SIZE'])
    evol_algo.initialize_population()
    evol_algo.assign_schedules_for_initialized_sols()
    evol_algo.run_schedules()
    evol_algo.run_events()
    evol_algo.update_all_fitness_scores()
    evol_algo.sort_population()
    evol_algo.print_fitness_scores(0)

    # mutation
    evol_algo.evol_algo_loop(config['algo']['N_ITERATIONS'])

    # test_availability(evol_algo)


if __name__ == "__main__":
    main()
