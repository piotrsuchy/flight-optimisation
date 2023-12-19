import unittest
import random
import copy
import json
from src.unallowed_approach.imp_evol_algo import ImpossibleEvolutionaryAlgorithm

class TestImpossibleEvolutionaryAlgorithm(unittest.TestCase):

    def test_training_hours_consistency(self):
        with open('parameters.json') as parameters_file:
            config = json.load(parameters_file)

        algo = ImpossibleEvolutionaryAlgorithm()
        algo.generate_training_hours()

        # Store the original training hours
        original_pilot_training_hours = [[pilot['train_hs'] for pilot in status_pop] for status_pop in algo.pilots_status_pop]
        original_attendant_training_hours = [[attendant['train_hs'] for attendant in status_pop] for status_pop in algo.attend_status_pop]

        algo.fill_in_distance_matrix()
        algo.assign_airports_to_crew_members()
        algo.create_initial_sols()

        algo.create_initial_generation()
        # imp_evol_algo.print_population()
        algo.update_fitness_for_all_sols()

        top_solutions = algo.select_solutions()
        to_crossover = copy.deepcopy(top_solutions)

        # Perform crossover and mutation on copies of these top solutions
        new_solutions = algo.crossover_solutions(to_crossover)
        # 50 / 50 mutation rate for two types of mutation operators
        if random.random() < 0.5:
            mutated_new_solutions = algo.mutate_solutions(new_solutions)
        else:
            mutated_new_solutions = algo.mutate_solutions_from_all(new_solutions, config['algo']['N_FLIGHTS_TO_MUT'])

        # Combine the top 50% of the original population with the new solutions
        algo.population = top_solutions + mutated_new_solutions

        # Update fitness scores for the entire population
        algo.update_fitness_for_all_sols()
        # self.print_average_fit_score(i)
        algo.reset_state_of_status_pops()
        # Verify that training hours remain the same
        for sol_idx, status_pop in enumerate(algo.pilots_status_pop):
            for pilot_idx, pilot in enumerate(status_pop):
                self.assertEqual(pilot['train_hs'], original_pilot_training_hours[sol_idx][pilot_idx], 
                                 f"Training hours for pilot {pilot_idx} in solution {sol_idx} have changed.")

        for sol_idx, status_pop in enumerate(algo.attend_status_pop):
            for attendant_idx, attendant in enumerate(status_pop):
                self.assertEqual(attendant['train_hs'], original_attendant_training_hours[sol_idx][attendant_idx], 
                                 f"Training hours for attendant {attendant_idx} in solution {sol_idx} have changed.")

if __name__ == '__main__':
    unittest.main()
