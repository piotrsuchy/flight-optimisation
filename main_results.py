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

    all_data = []
    for file in files:
        data = load_and_process_json(file, data_key)
        all_data.append(data)

    df = pd.DataFrame(all_data)
    average_values = df.mean()
    return average_values

def main(directory_path):
    test_case_types = [('plot_test_case', range(10)), 
                       ('plot_test_case_with_init', range(6)), 
                       ('plot_test_case_crossover', range(4)), 
                       ('plot_test_case_two_pop', range(3))]
    struct_types = ['structs_I', 'structs_II', 'structs_III']

    # q = 0

    for test_case_type, indices in test_case_types:
        for test_case_index in indices:
            for struct_type in struct_types:
                # q += 1
                # Processing penalties
                penalties_avg = process_combination(directory_path, test_case_type, test_case_index, struct_type, 'penalties', 'penalties')
                # Processing scores
                scores_avg = process_combination(directory_path, test_case_type, test_case_index, struct_type, 'fitness_scores', 'scores')
                
                if penalties_avg is not None and scores_avg is not None:
                    combined_avg = pd.concat([penalties_avg, scores_avg[['best_score', 'median_score']]])
                    file_name = f'results_{test_case_type}{test_case_index}_{struct_type}_average_values.csv'
                    print(f"\nCombined average values for {file_name}:")
                    print(combined_avg)
                    combined_avg.to_csv(file_name, header=False)
                    print(f"Saved combined average values to {file_name}.")

    # print(q)

if __name__ == "__main__":
    directory_path = './'  # Replace with your directory path
    main(directory_path)
