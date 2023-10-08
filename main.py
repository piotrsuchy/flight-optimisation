from src.solution import Solution
from src.evolutionary_algorithm import EvolutionaryAlgorithm
import time

def main():
    start_time = time.time()
    evol_algo = EvolutionaryAlgorithm(50)
    evol_algo.initialize_population()
    evol_algo.update_all_fitness_scores()
    evol_algo.print_fitness_scores()
    end_time = time.time()
    print(f"Duration: {end_time - start_time}")
    # demand_matrix = generate_demand_array(sim.airports)
    # visualize_demand_for_day(demand_matrix, sim.airports, day=3)

    
if __name__ == "__main__":
    main()