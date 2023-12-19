import json
import random
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
    imp_evol_algo.generate_training_hours()

    imp_evol_algo.create_initial_generation_with_update()
    # imp_evol_algo.print_population()

    two_sol_idx = random.sample(range(config['algo']['POPULATION_SIZE']), 2)
    sol_1 = imp_evol_algo.population[two_sol_idx[0]]
    sol_2 = imp_evol_algo.population[two_sol_idx[1]]
    diff_counter = 0

    for flight_1, flight_2 in zip(sol_1, sol_2):
        if flight_1 != flight_2:
            print(f"1: Flights are different")
            print(f"1: Flight1: {flight_1}")
            print(f"1: Flight2: {flight_2}")
            diff_counter += 1

    print(f"1: Diff counter: {diff_counter}")

    imp_evol_algo.update_fitness_for_all_sols()
    initial_penalties = imp_evol_algo.get_penalties_for_sols()
    # for i in range(len(imp_evol_algo.population)):
    #     print(f"START of first gen----")
    #     imp_evol_algo.print_penalties_for_sols(0, i)
    #     print(f"END of first gen----")
    # imp_evol_algo.print_average_fit_score("A")
    # imp_evol_algo.print_fitness_scores(0)
    # fit_scores = imp_evol_algo.get_fitness_scores()

    imp_evol_algo.evolutionary_algorithm_loop(config['algo']['N_ITERATIONS'], print_flag=1)
    # print(f"Initial fitness values: {fit_scores}")

    # print(f"---Final penalties applied---")
    # for i in range(len(imp_evol_algo.population)):
    #     imp_evol_algo.print_penalties_for_sols(config['algo']['N_ITERATIONS']+1, i)

    # print(f"---Initial penalties applied---")
    # for i in range(len(initial_penalties)):
    #     print(f"Loc: {initial_penalties[i][0]}, Rest: {initial_penalties[i][1]}, Canc: {initial_penalties[i][2]}, training overlap: {initial_penalties[i][3]}, Prop. alloc: {initial_penalties[i][4]}")

    sol_1 = imp_evol_algo.population[two_sol_idx[0]]
    sol_2 = imp_evol_algo.population[two_sol_idx[1]]
    diff_counter = 0

    for flight_1, flight_2 in zip(sol_1, sol_2):
        if flight_1 != flight_2:
            print(f"2: Flights are different")
            print(f"2: Flight1: {flight_1}")
            print(f"2: Flight2: {flight_2}")
            diff_counter += 1

    print(f"2: Diff counter: {diff_counter}")
    print(f"End of the program: Breakpoint to check the state")

if __name__ == "__main__":
    main()