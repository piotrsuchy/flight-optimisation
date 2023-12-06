import time
import json
from src.structures import Structures
from src.evolutionary_algorithm import EvolutionaryAlgorithm
from src.decorators import timing_decorator
from debug.test_availability import test_availability
from config import get_args, setup_logging
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

    i = 0

    while i < 10:
        i += 1
        print(f"Mutation check iteration: {i}")
        evol_algo.population = evol_algo.population[:len(evol_algo.population)//2]
        for sol_list in evol_algo.population:
            sol = sol_list[0]
            mutation_successful = False
            while not mutation_successful:
                try: 
                    time = evol_algo.mutation_pilots(sol)
                    mutation_successful = True
                except ValueError:
                    print("Error during mutation. Retrying with a different flight.")
            sol.initialized = "Mutated"
            for airport in sol.structures.airports:
                airport.check_consistency()
            evol_algo.reschedule_flights(sol, time, i)
            sol.scheduler.peek_all_events()

        evol_algo.run_events()

        for sol_list in evol_algo.population:
            print(f"------FLIGHTS OF SOL: {sol_list[0]}-------")
            sol_list[0].print_flights()
            print(f"------------------------------------------")

        print(f"")
        evol_algo.add_new_solutions()
        evol_algo.update_all_fitness_scores()
        evol_algo.sort_population()
        evol_algo.print_fitness_scores(i)

    # mutation
    # evol_algo.evol_algo_loop(config['algo']['N_ITERATIONS'])

    # test_availability(evol_algo)


if __name__ == "__main__":
    main()
