import json
import re
import glob
import os

def load_and_process_json(file_path, data_key):
    with open(file_path, 'r') as file:
        data = json.load(file)
        last_iteration_data = data[data_key][-1]
        return last_iteration_data

def find_corresponding_scores_files(penalties_file):
    date_pattern = r'\d{2}-\d{2}-\d{2}-\d{2}-\d{2}'
    wildcard_file = re.sub(date_pattern, '*', penalties_file)
    scores_files = wildcard_file.replace('penalties', 'scores')
    return scores_files

def get_all_scores_files(directory_path, scores_files_pattern):
    return glob.glob(os.path.join(directory_path, scores_files_pattern))

def extract_best_score_from_scores_file(scores_file):
    try:
        with open(scores_file, 'r') as file:
            data = json.load(file)
            last_iteration_data = data['fitness_scores'][-1]  
            return last_iteration_data.get('best_score')
    except (FileNotFoundError, KeyError, json.JSONDecodeError):
        print(f"Error reading file: {scores_file}")
        return None

def main(directory_path):
    best_scores_info = {
        'structs_I': {},
        'structs_II': {},
        'structs_III': {}
    }

    best_penalties_filenames = {
        'structs_I': {
            'plot_test_case': 'plot_test_case_7_structs_I_01-22-14-02-34_penalties.json',
            'plot_test_case_with_init': 'plot_test_case_with_init1_structs_I_01-22-02-44-04_penalties.json',
            'plot_test_case_crossover': 'plot_test_case_crossover_3_structs_I_01-22-15-22-36_penalties.json',
            'plot_test_case_two_pop': 'plot_test_case_two_pop1_structs_I_01-22-08-33-36_penalties.json',
        },
        'structs_II': {
            'plot_test_case': 'plot_test_case_5_structs_II_01-22-07-41-45_penalties.json',
            'plot_test_case_with_init': 'plot_test_case_with_init1_structs_II_01-22-11-51-44_penalties.json',
            'plot_test_case_crossover': 'plot_test_case_crossover_3_structs_II_01-22-15-24-02_penalties.json',
            'plot_test_case_two_pop': 'plot_test_case_two_pop2_structs_II_01-22-08-43-23_penalties.json',
        },
        'structs_III': {
            'plot_test_case': 'plot_test_case_6_structs_III_01-22-03-30-47_penalties.json',
            'plot_test_case_with_init': 'plot_test_case_with_init3_structs_III_01-22-06-20-25_penalties.json',
            'plot_test_case_crossover': 'plot_test_case_crossover_3_structs_III_01-22-09-30-51_penalties.json',
            'plot_test_case_two_pop': 'plot_test_case_two_pop1_structs_III_01-22-08-37-28_penalties.json',
        }
    }

    for struct_type, test_cases in best_penalties_filenames.items():
        for test_case, penalties_file in test_cases.items():
            scores_files_pattern = find_corresponding_scores_files(penalties_file)
            all_scores_files = glob.glob(os.path.join(directory_path, scores_files_pattern))
            
            best_scores_info[struct_type][test_case] = []
            for scores_file in all_scores_files:
                best_score = extract_best_score_from_scores_file(scores_file)
                if best_score is not None:
                    best_scores_info[struct_type][test_case].append(best_score)

    # Print or process the best scores information
    for struct, scores in best_scores_info.items():
        print(f"Best scores for {struct}:")
        for test_case, score_list in scores.items():
            print(f" - {test_case}: {score_list}")

if __name__ == "__main__":
    directory_path = './'  # Update with the actual directory path
    main(directory_path)