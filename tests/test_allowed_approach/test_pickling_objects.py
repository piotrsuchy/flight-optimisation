import pickle
import json
import unittest
from src.allowed_approach.structures import Structures
from src.allowed_approach.evol_algo import EvolutionaryAlgorithm
from src.allowed_approach.classes.crew_member import Pilot, FlightAttendant


def save_to_file(obj, filename):
    with open(filename, 'wb') as file:
        pickle.dump(obj, file)

def load_from_file(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

with open('parameters.json') as parameters_file:
    config = json.load(parameters_file)

class TestStructuresPickle(unittest.TestCase):

    def test_pickle_unpickle_structures(self):
        # Create original Structures object
        original_structures = Structures()

        # Save to file
        save_to_file(original_structures, 'test_structures.pkl')

        # Load from file
        unpickled_structures = load_from_file('test_structures.pkl')

        self.assertEqual(original_structures.airports, unpickled_structures.airports)
    
    def test_pickle_unpickle_evol_algo(self):
        initial_structures = Structures()

        # initial population
        evol_algo = EvolutionaryAlgorithm(
            initial_structures=initial_structures,
            population_size=config['algo']['POPULATION_SIZE'])
        evol_algo.initialize_population()
        evol_algo.assign_schedules_for_initialized_sols()

if __name__ == '__main__':
    unittest.main()
