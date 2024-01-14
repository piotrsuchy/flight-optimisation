import json
import subprocess
import datetime

test_cases_unallowed = [
    {
        "algo": { # test_case_0_with_update
            "POPULATION_SIZE": 20,
            "CROSSOVER_RATE": 0,
            "N_ITERATIONS_UN": 2500,
            "MUTATION_RATE": 1,
            "UNALL_FIX_LOCATION_PERCENT": 0,
            "ONE_MUTATE_RATIO": 0.5,
            "UNALL_INITIAL_HEURISTIC": "with_update"
        }
    },
    {
        "algo": { # test_case_1_no_update
            "POPULATION_SIZE": 20,
            "N_ITERATIONS_UN": 2500,
            "MUTATION_RATE": 1,
            "UNALL_FIX_LOCATION_PERCENT": 0,
            "ONE_MUTATE_RATIO": 0.5,
            "UNALL_INITIAL_HEURISTIC": "no_update"
        }
    },
    {
        "algo": { # test_case_2_random
            "POPULATION_SIZE": 20,
            "N_ITERATIONS_UN": 2500,
            "MUTATION_RATE": 1,
            "UNALL_FIX_LOCATION_PERCENT": 0,
            "ONE_MUTATE_RATIO": 0.5,
            "UNALL_INITIAL_HEURISTIC": "random"
        }
    },
    {
        "algo": { # crossover_1
            "POPULATION_SIZE": 20,
            "N_ITERATIONS_UN": 2500,
            "MUTATION_RATE": 1,
            "UNALL_FIX_LOCATION_PERCENT": 0,
            "CROSSOVER_RATE": 0.2,
            "ONE_MUTATE_RATIO": 0.5,
            "UNALL_INITIAL_HEURISTIC": "with_update"
        }
    },
    {
        "algo": { # crossover_2
            "POPULATION_SIZE": 20,
            "N_ITERATIONS_UN": 2500,
            "MUTATION_RATE": 1,
            "UNALL_FIX_LOCATION_PERCENT": 0,
            "CROSSOVER_RATE": 0.4,
            "ONE_MUTATE_RATIO": 0.5,
            "UNALL_INITIAL_HEURISTIC": "with_update"
        }
    },
    {
        "algo": { # crossover_3 
            "POPULATION_SIZE": 20,
            "N_ITERATIONS_UN": 2500,
            "MUTATION_RATE": 1,
            "UNALL_FIX_LOCATION_PERCENT": 0,
            "CROSSOVER_RATE": 0.6,
            "ONE_MUTATE_RATIO": 0.5,
            "UNALL_INITIAL_HEURISTIC": "with_update"
        }
    },
    {
        "algo": { # fix location_1 
            "UNALL_FIX_LOCATION_PERCENT": 0.05,
            "ONE_MUTATE_RATIO": 0.5,
            "UNALL_INITIAL_HEURISTIC": "with_update"
        }
    },
    {
        "algo": { # fix location_2
            "UNALL_FIX_LOCATION_PERCENT": 0.15,
            "ONE_MUTATE_RATIO": 0.5,
            "UNALL_INITIAL_HEURISTIC": "with_update"
        }
    },
    {
        "algo": { # fix location_3
            "UNALL_FIX_LOCATION_PERCENT": 0.30,
            "ONE_MUTATE_RATIO": 0.5,
            "UNALL_INITIAL_HEURISTIC": "with_update"
        }
    },
    {
        "algo": { # fix location_4
            "UNALL_FIX_LOCATION_PERCENT": 0.60,
            "ONE_MUTATE_RATIO": 0.5,
            "UNALL_INITIAL_HEURISTIC": "random"
        }
    }
]

test_cases_allowed = [
    {
        "algo": {
            "POPULATION_SIZE": 20,
            "N_ITERATIONS_AL": 40,
            "ALLOWED_HEURISTIC": "work_time",
            "ALLOWED_GEN_CREATION": "with_init"
        }
    },
    {
        "algo": {
            "POPULATION_SIZE": 20,
            "N_ITERATIONS_AL": 40,
            "ALLOWED_HEURISTIC": "random",
            "ALLOWED_GEN_CREATION": "with_init"
        }
    },
    {
        "algo": {
            "POPULATION_SIZE": 20,
            "N_ITERATIONS_AL": 40,
            "ALLOWED_HEURISTIC": "smallest_id",
            "ALLOWED_GEN_CREATION": "with_init"
        }
    },
    {
        "algo": {
            "POPULATION_SIZE": 20,
            "N_ITERATIONS_AL": 40,
            "ALLOWED_HEURISTIC": "work_time",
            "ALLOWED_GEN_CREATION": "with_init",
            "MUTATION_RATE": 0.25
        }
    },
    {
        "algo": {
            "POPULATION_SIZE": 20,
            "N_ITERATIONS_AL": 40,
            "ALLOWED_HEURISTIC": "work_time",
            "ALLOWED_GEN_CREATION": "with_init",
            "MUTATION_RATE": 0.5
        }
    },
    {
        "algo": {
            "POPULATION_SIZE": 20,
            "N_ITERATIONS_AL": 40,
            "ALLOWED_HEURISTIC": "work_time",
            "ALLOWED_GEN_CREATION": "with_init",
            "MUTATION_RATE": 0.75
        }
    }
]

test_cases_allowed_two_pop = [
    {
        "algo": {
            "POPULATION_SIZE": 20,
            "N_ITERATIONS_AL": 40,
            "ALLOWED_HEURISTIC": "work_time",
            "ALLOWED_GEN_CREATION": "two_pop",
            "MUTATION_RATE": 1
        }
    },
    {
        "algo": {
            "POPULATION_SIZE": 20,
            "N_ITERATIONS_AL": 40,
            "ALLOWED_HEURISTIC": "random",
            "ALLOWED_GEN_CREATION": "two_pop",
            "MUTATION_RATE": 1
        }
    },
    {
        "algo": {
            "POPULATION_SIZE": 20,
            "N_ITERATIONS_AL": 40,
            "ALLOWED_HEURISTIC": "smallest_id",
            "ALLOWED_GEN_CREATION": "two_pop",
            "MUTATION_RATE": 1
        }
    }
]

structs_files = ['structs_I.json', 'structs_II.json', 'structs_III.json']

def get_current_timestamp():
    return datetime.datetime.now().strftime("%m-%d-%H-%M-%S")

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
    current_timestamp = get_current_timestamp()
    command = f'python main_allowed.py --pickle json'
    inputs = f'{plot_filename}_{current_timestamp}\n{structs_file}\n'
    process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)
    process.communicate(input=inputs.encode())
    return process.returncode == 0

def run_main_unallowed(structs_file, plot_filename):
    current_timestamp = get_current_timestamp()
    command = f'python main_unallowed.py'
    inputs = f'{plot_filename}_{current_timestamp}\nyes\n{structs_file}\nno\n'
    process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)
    process.communicate(input=inputs.encode())
    return process.returncode == 0

def main():
    # for test_case_index, test_case in enumerate(test_cases_allowed):

    #     print(f"Test case being run: {test_case}")
    #     update_parameters_file(test_case)

    #     for structs_file in structs_files:
    #         plot_filename = f"plot_test_case_with_init{test_case_index}_{structs_file.split('.')[0]}"

    #         print(f"Running test case {test_case_index} with {structs_file}")
    #         success = run_main_allowed(structs_file, plot_filename)

    #         if not success:
    #             print(f"Error occurred while running test case {test_case_index} with {structs_file}")
    #         else:
    #             print(f"Completed test case {test_case_index} with {structs_file}")

    # print("All test cases for allowed approach completed.")

    for test_case_index, test_case in enumerate(test_cases_unallowed):

        print(f"Test case being run: {test_case}")
        update_parameters_file(test_case)

        for structs_file in structs_files:
            plot_filename = f"plot_test_case_{test_case_index}_{structs_file.split('.')[0]}"

            print(f"Running test case {test_case_index} with {structs_file}")
            success = run_main_unallowed(structs_file, plot_filename)

            if not success:
                print(f"Error occurred while running test case {test_case_index} with {structs_file}")
            else:
                print(f"Completed test case {test_case_index} with {structs_file}")

    print("All test cases for unallowed approach completed.")

    # for test_case_index, test_case in enumerate(test_cases_allowed_two_pop):

    #     print(f"Test case being run: {test_case}")
    #     update_parameters_file(test_case)

    #     for structs_file in structs_files:
    #         plot_filename = f"plot_test_case_two_pop{test_case_index}_{structs_file.split('.')[0]}"

    #         print(f"Running test case {test_case_index} with {structs_file}")
    #         success = run_main_allowed(structs_file, plot_filename)

    #         if not success:
    #             print(f"Error occurred while running test case {test_case_index} with {structs_file}")
    #         else:
    #             print(f"Completed test case {test_case_index} with {structs_file}")

    # print("All test cases for unallowed approach completed.")

if __name__ == "__main__":
    main()
