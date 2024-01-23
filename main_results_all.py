import json
import pandas as pd
import glob
import os

def load_and_process_json(file_path, data_key):
    with open(file_path, 'r') as file:
        data = json.load(file)
        last_iteration_data = data[data_key][-1]
        return last_iteration_data

def process_combination(directory_path, test_case_type, test_case_index, struct_type, data_key, file_suffix):
    if test_case_type == 'plot_test_case' or test_case_type == 'plot_test_case_crossover':
        pattern = os.path.join(directory_path, f'{test_case_type}_{test_case_index}_{struct_type}_*_{file_suffix}.json')
    else:
        pattern = os.path.join(directory_path, f'{test_case_type}{test_case_index}_{struct_type}_*_{file_suffix}.json')
    files = glob.glob(pattern)

    if not files:
        print(f"No matching files found for {test_case_type}{test_case_index} with {struct_type} and {file_suffix}.")
        return

    combined_data = pd.DataFrame()
    for file in files:
        data = load_and_process_json(file, data_key)
        df = pd.DataFrame(data, index=[os.path.basename(file).split('.')[0]])
        combined_data = pd.concat([combined_data, df], axis=0)

    return combined_data

def main(directory_path):
    test_case_types = [('plot_test_case', range(10)), 
                       ('plot_test_case_with_init', range(6)), 
                       ('plot_test_case_crossover', range(4)), 
                       ('plot_test_case_two_pop', range(3))]
    struct_types = ['structs_I', 'structs_II', 'structs_III']

    for test_case_type, indices in test_case_types:
        for test_case_index in indices:
            for struct_type in struct_types:
                # Processing penalties
                penalties_data = process_combination(directory_path, test_case_type, test_case_index, struct_type, 'penalties', 'penalties')
                # Processing scores
                scores_data = process_combination(directory_path, test_case_type, test_case_index, struct_type, 'fitness_scores', 'scores')
                
                if penalties_data is not None and scores_data is not None:
                    combined_data = pd.concat([penalties_data, scores_data])
                    file_name = f'combined_results_{test_case_type}{test_case_index}_{struct_type}.csv'
                    print(f"Combined data for {file_name}:")
                    print(combined_data)
                    combined_data.to_csv(file_name)
                    print(f"Saved combined data to {file_name}.")

if __name__ == "__main__":
    directory_path = './'
    main(directory_path)
