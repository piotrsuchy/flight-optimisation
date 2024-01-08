import matplotlib.pyplot as plt
from src.allowed_approach.visualisation import plot_compare_two_fitness_scores, plot_compare_multiple_fitness_scores

def main():
    # plot_compare_two_fitness_scores('vis_test_1', 'vis_test_2')
    file_label_dict = {
        '233': '5% fix location',
        '234': '15% fix location',
        '2345': '45% fix location'
    }
    plot_compare_multiple_fitness_scores(**file_label_dict)
    

if __name__ == "__main__":
    main()