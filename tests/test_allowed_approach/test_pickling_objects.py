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
        '''Basic check for the Structures'''
        original_structures = Structures()

        save_to_file(original_structures, 'initial_structs/test_structures.pkl')

        unpickled_structures = load_from_file('initial_structs/test_structures.pkl')

        for original_airport, unpickled_airport in zip(original_structures.airports, unpickled_structures.airports):
            self.assertEqual(original_airport, unpickled_airport)
    
    def test_pickle_unpickle_evol_algo(self):
        '''Testing if after initializing the algo the pickled object is the same,
        as described in __eq__ method'''
        original_structures = Structures()
        evol_algo = EvolutionaryAlgorithm(
            initial_structures=original_structures,
            population_size=config['algo']['POPULATION_SIZE'])
        evol_algo.initialize_population()
        evol_algo.assign_schedules_for_initialized_sols()

        save_to_file(original_structures, 'initial_structs/test_pickle_unpickle_evol_algo.pkl')
        unpickled_structures = load_from_file('initial_structs/test_pickle_unpickle_evol_algo.pkl')

        for original_airport, unpickled_airport in zip(original_structures.airports, unpickled_structures.airports):
            self.assertEqual(original_airport, unpickled_airport)
            

if __name__ == '__main__':
    unittest.main()
