import matplotlib.pyplot as plt
import json

def plot_compare_two_fitness_scores(file_path_1, file_path_2):
    with open(f'{file_path_1}_scores.json', 'r') as file:
        data_1 = json.load(file)

    with open(f'{file_path_2}_scores.json', 'r') as file:
        data_2 = json.load(file)

    # extract data for plotting
    iterations = [item['iteration'] for item in data_1['fitness_scores']]
    best_scores = [item['best_score'] for item in data_1['fitness_scores']]
    median_scores = [item['median_score'] for item in data_1['fitness_scores']]
    top_half_medians = [item['top_half_median'] for item in data_1['fitness_scores']]
    bottom_half_medians = [item['bottom_half_median'] for item in data_1['fitness_scores']]
    
    plt.figure(figsize=(10, 6))
    plt.plot(iterations, best_scores, label='best score')
    plt.plot(iterations, median_scores, label='median score')
    plt.plot(iterations, top_half_medians, label='top half median')
    plt.plot(iterations, bottom_half_medians, label='bottom half median')

    iterations = [item['iteration'] for item in data_2['fitness_scores']]
    best_scores = [item['best_score'] for item in data_2['fitness_scores']]
    median_scores = [item['median_score'] for item in data_2['fitness_scores']]
    top_half_medians = [item['top_half_median'] for item in data_2['fitness_scores']]
    bottom_half_medians = [item['bottom_half_median'] for item in data_2['fitness_scores']]

    plt.plot(iterations, best_scores, label='best score')
    plt.plot(iterations, median_scores, label='median score')
    plt.plot(iterations, top_half_medians, label='top half median')
    plt.plot(iterations, bottom_half_medians, label='bottom half median')

    plt.xlabel('iteration')
    plt.ylabel('fitness score')
    plt.title('Comparison of two fitness scores')
    plt.legend()
    plt.show()

def plot_compare_multiple_fitness_scores(**kwargs):
    plt.figure(figsize=(10, 6))

    for file_path, label in kwargs.items():
        with open(f'{file_path}_scores.json', 'r') as file:
            data = json.load(file)

        iterations = [item['iteration'] for item in data['fitness_scores']]
        best_scores = [item['best_score'] for item in data['fitness_scores']]
        median_scores = [item['median_score'] for item in data['fitness_scores']]

        plt.plot(iterations, best_scores, label=f'best score - ({label})')
        plt.plot(iterations, median_scores, label=f'median score - ({label})')

    plt.xlabel('Iteration')
    plt.ylabel('Fitness Score')
    plt.title('Comparison of Fitness Scores for different operators')
    plt.legend()
    plt.show()

def plot_fitness_scores(file_path):
    with open(f'{file_path}_scores.json', 'r') as file:
        data = json.load(file)

    # extract data for plotting
    iterations = [item['iteration'] for item in data['fitness_scores']]
    best_scores = [item['best_score'] for item in data['fitness_scores']]
    median_scores = [item['median_score'] for item in data['fitness_scores']]
    top_half_medians = [item['top_half_median'] for item in data['fitness_scores']]
    bottom_half_medians = [item['bottom_half_median'] for item in data['fitness_scores']]

    # plotting
    plt.figure(figsize=(10, 6))
    plt.plot(iterations, best_scores, label='best score')
    plt.plot(iterations, median_scores, label='median score')
    plt.plot(iterations, top_half_medians, label='top half median')
    plt.plot(iterations, bottom_half_medians, label='bottom half median')
    plt.xlabel('iteration')
    plt.ylabel('fitness score')
    plt.title('evolution of fitness scores over iterations')
    plt.legend()
    plt.show()

def plot_penalties(file_path):
    with open(f'{file_path}_penalties.json', 'r') as file:
        data = json.load(file)

    iterations = [item['iteration'] for item in data['penalties']]
    cancelled_nums = [item['cancelled_num'] for item in data['penalties']]
    training_nums = [item['training_num'] for item in data['penalties']]
    dayoff_nums = [item['dayoff_num'] for item in data['penalties']]
    location_nums = [item['location_num'] for item in data['penalties']]
    rest_nums = [item['rest_num'] for item in data['penalties']]
    overwork_nums = [item['overwork_num']+1 for item in data['penalties']]

    #plot penalties
    plt.figure(figsize=(10, 6))
    plt.plot(iterations, cancelled_nums, label='number of cancelled flights')
    plt.plot(iterations, training_nums, label='number of training overlaps')
    plt.plot(iterations, dayoff_nums, label='number of dayoff overlaps')
    plt.plot(iterations, location_nums, label='number of location penalties applied')
    plt.plot(iterations, rest_nums, label='number of rest penalties applied')
    plt.plot(iterations, overwork_nums, label='number of overwork hours')
    plt.yscale('log')
    plt.xlabel('iteration')
    plt.ylabel('number of penalties applied in the best solution')
    plt.title('evolution of number of different penalties applied on the best solution')
    plt.legend()
    plt.show()
