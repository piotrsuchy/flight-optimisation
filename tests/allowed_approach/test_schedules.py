import unittest
import json
import copy
from src.allowed_approach.evol_algo import EvolutionaryAlgorithm
from src.allowed_approach.structures import Structures
from src.allowed_approach.schedule import Schedule
from src.allowed_approach.solution import Solution

class TestSchedule(unittest.TestCase):

    def test_random_schedule(self):
        initial_structures1 = Structures()
        sol1 = Solution(0, initial_structures1, 720)

        schedule1 = Schedule()
        schedule2 = Schedule()

        schedule1.create_random_schedule(sol1, 500, 720, seed=50)
        schedule2.create_random_schedule(sol1, 500, 720, seed=50)
    
        print(schedule1)
        print("----------schedule1")
        print(schedule2)
        self.assertEqual(schedule1, schedule2)

    def test_consistent_schedules(self):
        with open('parameters.json') as parameters_file:
            config = json.load(parameters_file)
        initial_structures = Structures()

        evol_algo = EvolutionaryAlgorithm(
            initial_structures=initial_structures,
            population_size=config['algo']['POPULATION_SIZE'])
        evol_algo.initialize_population()
        evol_algo.assign_schedules_for_initialized_sols()

        first_schedule = evol_algo.population[0][0].schedule
        for sol_list in evol_algo.population[1:]:
            current_schedule = sol_list[0].schedule
            if first_schedule != current_schedule:
                for first_flight, current_flight in zip(first_schedule.flight_schedule, current_schedule.flight_schedule):
                    if first_flight != current_flight:
                        print("Mismatched flights:")
                        print("First flight:", first_flight)
                        print("Current flight:", current_flight)
                        break  # Break after the first mismatch
                self.fail("Schedules are not consistent")

if __name__ == '__main__':
    unittest.main()

