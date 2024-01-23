import json
import pandas as pd
import glob
import os

def load_and_process_json(file_path, data_key):
    with open(file_path, 'r') as file:
        data = json.load(file)
        last_iteration_data = data[data_key][-1]
        return last_iteration_data, os.path.basename(file_path)

def process_combination(directory_path, test_case_type, test_case_index, struct_type, data_key, file_suffix):
    if test_case_type in ['plot_test_case', 'plot_test_case_crossover']:
        pattern = os.path.join(directory_path, f'{test_case_type}_{test_case_index}_{struct_type}_*_{file_suffix}.json')
    else:
        pattern = os.path.join(directory_path, f'{test_case_type}{test_case_index}_{struct_type}_*_{file_suffix}.json')
    files = glob.glob(pattern)

    all_data = []
    for file_path in files:
        data, filename = load_and_process_json(file_path, data_key)
        data['filename'] = filename
        all_data.append(data)

    return pd.DataFrame(all_data)

def main(directory_path):
    test_case_types = [('plot_test_case', range(10)), 
                       ('plot_test_case_with_init', range(6)), 
                       ('plot_test_case_crossover', range(4)), 
                       ('plot_test_case_two_pop', range(3))]
    struct_types = ['structs_I', 'structs_II', 'structs_III']

    best_results = {}
    for struct_type in struct_types:
        for test_case_type, _ in test_case_types:
            best_score = float('inf')
            best_file = None

            for test_case_index in range(10):  # Assuming a maximum of 10 runs per test case
                penalties_data = process_combination(directory_path, test_case_type, test_case_index, struct_type, 'penalties', 'penalties')
                scores_data = process_combination(directory_path, test_case_type, test_case_index, struct_type, 'fitness_scores', 'scores')
                combined_data = pd.concat([penalties_data, scores_data])

                if not combined_data.empty:
                    current_best_score = combined_data['best_score'].mean()
                    if current_best_score < best_score:
                        best_score = current_best_score
                        best_file = combined_data['filename'].iloc[0]  # Get the filename of the best score

            best_results[(struct_type, test_case_type)] = (best_score, best_file)

    # Output the results
    for (struct_type, test_case_type), (score, filename) in best_results.items():
        print(f"Best average score for {struct_type}, {test_case_type}: {score}")
        print(f"Contributing file: {filename}")

if __name__ == "__main__":
    directory_path = './'
    main(directory_path)
