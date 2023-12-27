from src.unallowed_approach.imp_evol_algo import ImpossibleEvolutionaryAlgorithm

test_population = [
    [  
        [1, 2, 101, 2, 1, 2, 3, 4, [3, 0], 10],  # Flight 1 (3 location mismatches)
        [2, 3, 3, 4, 5, 6, 7, 8, [0, 0], 20],  # Flight 2
        [3, 2, 103, 106, 201, 202, 203, 204, [100, 0], 30],  # Flight 1 (3 location mismatches)
        [3, 1, 103, 104, 205, 206, 207, 208, [2, 0], 40],  # Flight 2
    ],
]

# Create an instance of ImpossibleEvolutionaryAlgorithm with this test population
test_algorithm = ImpossibleEvolutionaryAlgorithm()
test_algorithm.population = test_population

# Print the initial state for comparison
print("Before fix:")
print(test_population[0])  # Print the first flight of the first solution

population = test_algorithm.fix_location_heuristic_for_all(test_algorithm.population)

# Print the state after applying the heuristic
print("After fix:")
print(population)  # Again, print the first flight of the first solution
