from src.allowed_approach.visualisation import plot_compare_multiple_fitness_scores

def main():
    test_1_struct_I = {
        'results/allowed/plot_test_case_0_structs_I_01-11-21-20-25': 'ZD1, work_time',
        'results/allowed/plot_test_case_1_structs_I_01-11-21-33-27': 'ZD1, random',
        'results/allowed/plot_test_case_2_structs_I_01-11-21-48-02': 'ZD1, smallest_id'
    }
    test_1_struct_II = {
        'results/allowed/plot_test_case_0_structs_II_01-11-21-22-56': 'ZD2, work_time',
        'results/allowed/plot_test_case_1_structs_II_01-11-21-36-34': 'ZD2, random',
        'results/allowed/plot_test_case_2_structs_II_01-11-21-50-39': 'ZD2, smallest_id'
    }
    test_1_struct_III = {
        'results/allowed/plot_test_case_0_structs_III_01-11-21-26-51': 'ZD3, work_time',
        'results/allowed/plot_test_case_1_structs_III_01-11-21-40-40': 'ZD3, random',
        'results/allowed/plot_test_case_2_structs_III_01-11-21-54-03': 'ZD3, smallest_id'
    }
    
    plot_compare_multiple_fitness_scores(plotname='results/final_results/ZD1_allowed_heuristic', **test_1_struct_I)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/ZD2_allowed_heuristic', **test_1_struct_II)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/ZD3_allowed_heuristic', **test_1_struct_III)

if __name__ == "__main__":
    main()