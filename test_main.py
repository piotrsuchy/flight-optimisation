from src.unallowed_approach.imp_evol_algo import ImpossibleEvolutionaryAlgorithm

def test_status_consistency_between_sols():
    algo = ImpossibleEvolutionaryAlgorithm()
    algo.assign_airports_to_crew_members()  # Initial assignment

    sol_0_pilots_status = algo.pilots_status_pop[0]

    # for sol_id in range(len(algo.pilots_status_pop)):
    for pilot in algo.pilots_status_pop[2]:
        print(pilot)
    print(f"----------OTHER SOL---------")
    for pilot in sol_0_pilots_status:
        print(pilot)

def main():
    test_status_consistency_between_sols()
    
    
main()