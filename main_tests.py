import json
import subprocess

# FOR CHAT: test cases to write correctly!
test_cases = [
    {
        "algo": {
            "ALLOWED_HEURISTIC": "work_time",
        },
        "algo": {
            "ALLOWED_HEURISTIC": "random",
        },
        "algo": {
            "ALLOWED_HEURISTIC": "smallest_id",
        }
    }
]

structs_files = ['structs_I.json', 'structs_II.json', 'structs_III.json']

def update_parameters_file(params, file_path='parameters.json'):
    def update_recursive(d, u):
        for k, v in u.items():
            if isinstance(v, dict):
                d[k] = update_recursive(d.get(k, {}), v)
            else:
                d[k] = v
        return d

    with open(file_path, 'r') as file:
        data = json.load(file)

    updated_data = update_recursive(data, params)

    with open(file_path, 'w') as file:
        json.dump(updated_data, file, indent=4)

def run_main_allowed(structs_file, plot_filename):
    command = f'python main_allowed.py --pickle json'
    inputs = f'{plot_filename}\n{structs_file}\n'
    process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)
    process.communicate(input=inputs.encode())
    return process.returncode == 0

def main():
    for test_case_index, test_case in enumerate(test_cases):
        update_parameters_file(test_case)

        for structs_file in structs_files:
            plot_filename = f"plot_test_case_{test_case_index}_structs_{structs_file.split('.')[0]}.png"

            print(f"Running test case {test_case_index} with {structs_file}")
            success = run_main_allowed(structs_file, plot_filename)

            if not success:
                print(f"Error occurred while running test case {test_case_index} with {structs_file}")
            else:
                print(f"Completed test case {test_case_index} with {structs_file}")

    print("All test cases completed.")

if __name__ == "__main__":
    main()
