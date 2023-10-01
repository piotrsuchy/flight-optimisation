from src.simulation import Simulation
from src.passenger_demand import generate_demand_array, visualize_demand, visualize_demand_for_day
import time

def main():
    start_time = time.time()
    sim = Simulation()
    sim.generate_structs()
    # sim.print_structures()
    sim.run_simulation()
    # sim.print_structures()

    print("------------------------------------------------------")
    print("---------------------GENERATING DEMAND----------------------")
    print("------------------------------------------------------")
    end_time = time.time()
    demand_matrix = generate_demand_array(sim.airports)
    print(f"Duration of the whole program: {end_time - start_time}")
    # visualize_demand_for_day(demand_matrix, sim.airports, day=3)

    
if __name__ == "__main__":
    main()