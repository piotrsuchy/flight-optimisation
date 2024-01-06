import matplotlib.pyplot as plt
import json

def plot_fitness_scores(file_path):
    with open(f'{file_path}_scores.json', 'r') as file:
        data = json.load(file)

    # Extract data for plotting
    iterations = [item['iteration'] for item in data['fitness_scores']]
    best_scores = [item['best_score'] for item in data['fitness_scores']]
    median_scores = [item['median_score'] for item in data['fitness_scores']]
    top_half_medians = [item['top_half_median'] for item in data['fitness_scores']]
    bottom_half_medians = [item['bottom_half_median'] for item in data['fitness_scores']]

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(iterations, best_scores, label='Best Score')
    plt.plot(iterations, median_scores, label='Median Score')
    plt.plot(iterations, top_half_medians, label='Top Half Median')
    plt.plot(iterations, bottom_half_medians, label='Bottom Half Median')
    plt.xlabel('Iteration')
    plt.ylabel('Fitness Score')
    plt.title('Evolution of Fitness Scores Over Iterations')
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
    plt.plot(iterations, cancelled_nums, label='Number of cancelled flights')
    plt.plot(iterations, training_nums, label='Number of training overlaps')
    plt.plot(iterations, dayoff_nums, label='Number of dayoff overlaps')
    plt.plot(iterations, location_nums, label='Number of location penalties applied')
    plt.plot(iterations, rest_nums, label='Number of rest penalties applied')
    plt.plot(iterations, overwork_nums, label='Number of overwork hours')
    plt.yscale('log')
    plt.xlabel('Iteration')
    plt.ylabel('Number of penalties applied in the best solution')
    plt.title('Evolution of number of different penalties applied on the best solution')
    plt.legend()
    plt.show()
