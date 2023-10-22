import argparse
import logging
from src.structures import Structures
from src.evolutionary_algorithm import EvolutionaryAlgorithm
import time
from copy import deepcopy


def main():
    parser = argparse.ArgumentParser(
        description='Run the evolutionary algorithm.')
    parser.add_argument('--log', action='store_true', help='enable logging')
    args = parser.parse_args()

    if args.log:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
    else:
        logging.basicConfig(level=logging.CRITICAL)

    start_time = time.time()
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

    end_time = time.time()
    print(f"Duration: {end_time - start_time}")

    start_time = time.time()
    test_availability(evol_algo)
    end_time = time.time()
    print(f"Duration of testing availability is {end_time - start_time}")


def test_availability(evol_algo):
    print(f"Checking the availability_log object for airport 1:")
    sol_1 = evol_algo.population[0][0]
    first_airport = sol_1.structures.airports[0]
    availability_log = first_airport.availability_log

    simulation_times = [0, 100, 700]
    for sim_time in simulation_times:
        try:
            availability = availability_log.get_availability(sim_time)
            print(f"Availability at simulation time {sim_time}:")
            print(f"  Pilots: {len(availability.pilots)}")
            print(f"  Attendants: {len(availability.attendants)}")
            print(f"  Planes: {len(availability.planes)}")
        except ValueError as e:
            print(f"Error at simulation time {sim_time}: {e}")


if __name__ == "__main__":
    main()
