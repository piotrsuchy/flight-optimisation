from src.structures import Structures
from src.evolutionary_algorithm import EvolutionaryAlgorithm
import time
from copy import deepcopy

def main():
    start_time = time.time()
    initial_structures = Structures()
 
    evol_algo = EvolutionaryAlgorithm(initial_structures, 100)
    evol_algo.initialize_population_and_run_events()
    evol_algo.update_all_fitness_scores()
    evol_algo.print_revenue_and_costs()
    initial_population = deepcopy(evol_algo.population)

    # Sort and print results for Roulette Selection
    print("\nSorted Population using Roulette Selection:")
    evol_algo.roulette_sort()
    for individual in evol_algo.population:
        print(f"Individual: {individual[1]}, Fitness Score: {individual[0].fitness_score}")

    evol_algo.population = initial_population

    # Sort and print results for Tournament Selection
    print("\nSorted Population using Tournament Selection:")
    evol_algo.tournament_sort()
    for individual in evol_algo.population:
        print(f"Individual: {individual[1]}, Fitness Score: {individual[0].fitness_score}")

    evol_algo.population = initial_population

    # Sort and print results for Rank Selection
    print("\nSorted Population using Rank Selection:")
    evol_algo.rank_sort()
    for individual in evol_algo.population:
        print(f"Individual: {individual[1]}, Fitness Score: {individual[0].fitness_score}")

    end_time = time.time()
    print(f"Duration: {end_time - start_time}")
    # demand_matrix = generate_demand_array(sim.airports)
    # visualize_demand_for_day(demand_matrix, sim.airports, day=3)

    
if __name__ == "__main__":
    main()