from src.solution import Solution
from src.passenger_demand import generate_demand_array, visualize_demand, visualize_demand_for_day
import time

BASELINE_PARAMS = {
    'N_AIRPORTS': 10,
    'N_FLIGHTS': 300,
    'N_PILOTS_F_A': 6,
    'N_ATTENDANTS_F_A': 12,
    'N_PLANES_F_A': 4
}

MODIFICATION_FACTORS = [1, 10, 100, 1000]  

def simulation_main(**params):
    start_time = time.time()
    sim = Solution(n_airports=params['N_AIRPORTS'], 
                     n_flights=params['N_FLIGHTS'], 
                     n_pilots_f_a=params['N_PILOTS_F_A'], 
                     n_attendants_f_a=params['N_ATTENDANTS_F_A'], 
                     n_planes_f_a=params['N_PLANES_F_A'])
    sim.generate_structs()
    sim.run_simulation()
    end_time = time.time()
    # print(f"Duration of the whole program: {end_time - start_time}")
    # demand_matrix = generate_demand_array(sim.airports)
    return end_time - start_time  


if __name__ == "__main__":
    results = []

    # check for each parameter with modification factors 1, 10, 100, 100:
    for param, baseline_value in BASELINE_PARAMS.items():
        for factor in MODIFICATION_FACTORS:
            print(f"Checking for factor: {factor} in param: {param}.")
            modified_params = BASELINE_PARAMS.copy()
            modified_params[param] = baseline_value * factor
            
            duration = simulation_main(**modified_params)
            results.append({'param': param, 'factor': factor, 'duration': duration})

    # check for all parameters x10, and flights x100:
    modifed_params = BASELINE_PARAMS.copy()
    for param in BASELINE_PARAMS.keys():
        modified_params[param] *= 10
    modified_params['N_FLIGHTS'] *= 10
    duration = simulation_main(**modified_params)
    results.append(f"All 10x, flights 100x, duration: {duration}")
    # Visualize or Log results
    for result in results:
        print(result)
