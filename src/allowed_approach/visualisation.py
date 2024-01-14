import matplotlib.pyplot as plt
import pandas as pd
import json

def plot_compare_two_fitness_scores(plotname, file_path_1, file_path_2):
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
    plt.plot(iterations, best_scores, label='najlepszy wynik')
    plt.plot(iterations, median_scores, label='mediana wyników')
    plt.plot(iterations, top_half_medians, label='mediana 50% lepszych wyników')
    plt.plot(iterations, bottom_half_medians, label='mediana 50% gorszych wynikó∑')

    iterations = [item['iteration'] for item in data_2['fitness_scores']]
    best_scores = [item['best_score'] for item in data_2['fitness_scores']]
    median_scores = [item['median_score'] for item in data_2['fitness_scores']]
    top_half_medians = [item['top_half_median'] for item in data_2['fitness_scores']]
    bottom_half_medians = [item['bottom_half_median'] for item in data_2['fitness_scores']]

    plt.plot(iterations, best_scores, label='najlepszy wynik')
    plt.plot(iterations, median_scores, label='mediana wyników')
    plt.plot(iterations, top_half_medians, label='mediana 50% lepszych wyników')
    plt.plot(iterations, bottom_half_medians, label='mediana 50% gorszych wynikó∑')

    plt.xlabel('Liczba iteracji')
    plt.ylabel('Funkcja celu')
    plt.grid()
    # plt.title('Comparison of two fitness scores')
    plt.legend(bbox_to_anchor=(0.5, -0.15), loc='upper center', ncol=2)
    plt.tight_layout()
    plt.savefig(plotname)

def plot_compare_multiple_fitness_scores(plotname, moving_avg_period=20, **kwargs):
    plt.figure(figsize=(10, 6))
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # Example color list

    for i, (file_path, label) in enumerate(kwargs.items()):
        color = colors[i % len(colors)]  # Cycle through colors
        with open(f'{file_path}_scores.json', 'r') as file:
            data = json.load(file)

        iterations = [item['iteration'] for item in data['fitness_scores']]
        best_scores = [item['best_score'] for item in data['fitness_scores']]
        median_scores = [item['median_score'] for item in data['fitness_scores']]

        if moving_avg_period == 0:
            plt.plot(iterations, best_scores, label=f'Best Score - {label}', color=color)
        else:
            median_scores_smoothed = pd.Series(median_scores).rolling(window=moving_avg_period).mean()
            plt.plot(iterations, best_scores, label=f'Best Score - {label}', color=color)
            plt.plot(iterations, median_scores_smoothed, label=f'Median Score (MA) - {label}', linestyle='--', color=color, linewidth=0.15)

    plt.xlabel('Number of Iterations')
    plt.ylabel('Objective Function')
    plt.grid()
    plt.legend(bbox_to_anchor=(0.5, -0.15), loc='upper center', ncol=2)
    plt.tight_layout()
    plt.savefig(plotname)


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
    plt.plot(iterations, best_scores, label='najlepszy wynik')
    plt.plot(iterations, median_scores, label='mediana wyników')
    plt.plot(iterations, top_half_medians, label='mediana 50% lepszych wyników')
    plt.plot(iterations, bottom_half_medians, label='mediana 50% gorszych wyników')
    plt.xlabel('Liczba iteracji')
    plt.ylabel('Funkcja celu')
    plt.grid()
    # plt.title('evolution of fitness scores over iterations')
    plt.legend(bbox_to_anchor=(0.5, -0.15), loc='upper center', ncol=2)
    plt.tight_layout()
    plt.savefig(f"{file_path}_scores.png")

def plot_penalties(file_path, plotname=None):
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
    plt.plot(iterations, cancelled_nums, label='liczba anulowanych lotów')
    plt.plot(iterations, training_nums, label='liczba kar za szkolenie')
    plt.plot(iterations, dayoff_nums, label='liczba kar za dzień wolny')
    plt.plot(iterations, location_nums, label='liczba kar za złą lokalizację')
    plt.plot(iterations, rest_nums, label='liczba kar za odpoczynek')
    plt.plot(iterations, overwork_nums, label='liczba nadgodzin')
    plt.yscale('log')
    plt.xlabel('Liczba iteracji')
    plt.ylabel('Kary nałożone na najlepsze rozwiązanie')
    plt.grid()
    # plt.title('evolution of number of different penalties applied on the best solution')
    plt.legend(bbox_to_anchor=(0.5, -0.15), loc='upper center', ncol=2)
    plt.tight_layout()
    if plotname:
        plt.savefig(f"results/final_results/{plotname}.png")
    else:
        plt.savefig(f"{file_path}_penalties.png")
