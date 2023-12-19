import unittest
import copy
from src.unallowed_approach.imp_evol_algo import ImpossibleEvolutionaryAlgorithm

class TestImpossibleEvolutionaryAlgorithm(unittest.TestCase):

    def test_status_consistency_between_sols(self):
        algo = ImpossibleEvolutionaryAlgorithm()
        algo.assign_airports_to_crew_members()  # Initial assignment

        # Extract locations of pilots and attendants in the first solution
        sol_0_pilot_locations = [pilot_status['location'] for pilot_status in algo.pilots_status_pop[0]]
        sol_0_attendant_locations = [attendant_status['location'] for attendant_status in algo.attend_status_pop[0]]

        for sol_id in range(1, len(algo.pilots_status_pop)):  # Start from the second solution
            current_pilot_locations = [pilot_status['location'] for pilot_status in algo.pilots_status_pop[sol_id]]
            current_attendant_locations = [attendant_status['location'] for attendant_status in algo.attend_status_pop[sol_id]]

            self.assertEqual(current_pilot_locations, sol_0_pilot_locations, f"Sol: {sol_id} has different pilot locations than initial sol")
            self.assertEqual(current_attendant_locations, sol_0_attendant_locations, f"Sol: {sol_id} has different attendant locations than initial sol")
            
    def check_location_consistency_between_sols(self, algo):
        sol_0_pilot_locations = [pilot_status['location'] for pilot_status in algo.pilots_status_pop[0]]
        sol_0_attendant_locations = [attendant_status['location'] for attendant_status in algo.attend_status_pop[0]]

        for sol_id in range(1, len(algo.pilots_status_pop)):
            current_pilot_locations = [pilot_status['location'] for pilot_status in algo.pilots_status_pop[sol_id]]
            current_attendant_locations = [attendant_status['location'] for attendant_status in algo.attend_status_pop[sol_id]]

            self.assertEqual(current_pilot_locations, sol_0_pilot_locations, f"Sol: {sol_id} has different pilot locations than initial sol")
            self.assertEqual(current_attendant_locations, sol_0_attendant_locations, f"Sol: {sol_id} has different attendant locations than initial sol")
    
    def test_status_consistency(self):
        algo = ImpossibleEvolutionaryAlgorithm()

        # Initial setups
        algo.fill_in_distance_matrix()
        algo.assign_airports_to_crew_members()
        algo.create_initial_sols()
        algo.generate_training_hours()

        # Assign initial population and check status
        algo.create_initial_generation_with_update()
        self.check_location_consistency_between_sols(algo)
        algo.update_fitness_for_all_sols()

        # Perform some iterations and check status again
        algo.evolutionary_algorithm_loop(5, print_flag=0)  
        self.check_location_consistency_between_sols(algo)
        # check if for each solution the location is the same


if __name__ == '__main__':
    unittest.main()
