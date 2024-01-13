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
    # plt.title('Comparison of two fitness scores')
    plt.legend()
    plt.savefig(plotname)


def plot_compare_multiple_fitness_scores(plotname, moving_avg_period=5, **kwargs):
    plt.figure(figsize=(10, 6))

    for file_path, label in kwargs.items():
        with open(f'{file_path}_scores.json', 'r') as file:
            data = json.load(file)

        iterations = [item['iteration'] for item in data['fitness_scores']]
        best_scores = [item['best_score'] for item in data['fitness_scores']]
        median_scores = [item['median_score'] for item in data['fitness_scores']]

        median_scores_smoothed = pd.Series(median_scores).rolling(window=moving_avg_period).mean()

        plt.plot(iterations, best_scores, label=f'Najlepszy wynik - {label}')
        plt.plot(iterations, median_scores_smoothed, label=f'Mediana wyników (MA) - {label}', linestyle='--')

    plt.xlabel('Liczba iteracji')
    plt.ylabel('Funkcja celu')
    # plt.title('Comparison of Fitness Scores with Moving Average for Median Scores')
    plt.legend()
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
    plt.plot(iterations, bottom_half_medians, label='mediana 50% gorszych wynikó∑')
    plt.xlabel('Liczba iteracji')
    plt.ylabel('Funkcja celu')
    # plt.title('evolution of fitness scores over iterations')
    plt.legend()
    plt.savefig(f"{file_path}_scores.png")

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
    plt.plot(iterations, cancelled_nums, label='liczba anulowanych lotów')
    plt.plot(iterations, training_nums, label='liczba kar za szkolenie')
    plt.plot(iterations, dayoff_nums, label='liczba kar za dzień wolny')
    plt.plot(iterations, location_nums, label='liczba kar za złą lokalizację')
    plt.plot(iterations, rest_nums, label='liczba kar za odpoczynek')
    plt.plot(iterations, overwork_nums, label='liczba nadgodzin')
    plt.yscale('log')
    plt.xlabel('Liczba iteracji')
    plt.ylabel('Kary nałożone na najlepsze rozwiązanie')
    # plt.title('evolution of number of different penalties applied on the best solution')
    plt.legend()
    plt.savefig(f"{file_path}_penalties.png")
