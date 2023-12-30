import matplotlib.pyplot as plt
import json

def plot_fitness_scores(file_path):
    # Load data from the file
    with open(f'{file_path}.json', 'r') as file:
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
    # plt.savefig(f'{}.png')
    plt.legend()
    plt.show()
