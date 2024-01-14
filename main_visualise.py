from src.allowed_approach.visualisation import plot_compare_multiple_fitness_scores

def main():
    test_1_with_init_struct_I = {
        'results/allowed/plot_test_case_0_structs_I_01-11-21-20-25': 'ZD1, with_init, work_time',
        'results/allowed/plot_test_case_1_structs_I_01-11-21-33-27': 'ZD1, with_init, random',
        'results/allowed/plot_test_case_2_structs_I_01-11-21-48-02': 'ZD1, with_init, smallest_id',
    }
    test_1_with_init_struct_II = {
        'results/allowed/plot_test_case_0_structs_II_01-11-00-37-41': 'ZD2, with_init, work_time',
        'results/allowed/plot_test_case_1_structs_II_01-11-21-36-34': 'ZD2, with_init, random',
        'results/allowed/plot_test_case_2_structs_II_01-11-21-50-39': 'ZD2, with_init, smallest_id',
    }
    test_1_with_init_struct_III = {
        'results/allowed/plot_test_case_0_structs_III_01-11-21-26-51': 'ZD3, with_init, work_time',
        'results/allowed/plot_test_case_1_structs_III_01-11-21-40-40': 'ZD3, with_init, random',
        'results/allowed/plot_test_case_2_structs_III_01-11-21-54-03': 'ZD3, with_init, smallest_id',
    }
    test_1_two_pop_struct_I = {
        'results/allowed/plot_test_case_two_pop0_structs_I_01-14-09-53-07': 'ZD1, two_pop, work_time',
        'results/allowed/plot_test_case_two_pop1_structs_I_01-14-10-01-47': 'ZD1, two_pop, random',
        'results/allowed/plot_test_case_two_pop2_structs_I_01-14-10-10-22': 'ZD1, two_pop, smallest_id'
    }
    test_1_two_pop_struct_II = {
        'results/allowed/plot_test_case_two_pop0_structs_II_01-14-09-54-33': 'ZD2, two_pop, work_time',
        'results/allowed/plot_test_case_two_pop1_structs_II_01-14-10-03-08': 'ZD2, two_pop, random',
        'results/allowed/plot_test_case_two_pop2_structs_II_01-14-10-11-57': 'ZD2, two_pop, smallest_id'
    }
    test_1_two_pop_struct_III = {
        'results/allowed/plot_test_case_two_pop0_structs_III_01-14-09-57-01': 'ZD3, two_pop, work_time',
        'results/allowed/plot_test_case_two_pop1_structs_III_01-14-10-05-38': 'ZD3, two_pop, random',
        'results/allowed/plot_test_case_two_pop2_structs_III_01-14-10-14-14': 'ZD3, two_pop, smallest_id'
    }
    
    plot_compare_multiple_fitness_scores(plotname='results/final_results/ZD1_with_init_allowed_heuristic', **test_1_with_init_struct_I)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/ZD2_with_init_allowed_heuristic', **test_1_with_init_struct_II)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/ZD3_with_init_allowed_heuristic', **test_1_with_init_struct_III)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/ZD1_two_pop_allowed_heuristic', **test_1_two_pop_struct_I)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/ZD2_two_pop_allowed_heuristic', **test_1_two_pop_struct_II)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/ZD3_two_pop_allowed_heuristic', **test_1_two_pop_struct_III)

    test_2_structs_I = {
        'results/allowed/plot_test_case_3_structs_I_01-11-22-01-46' : 'ZD1, 25% prawd. mutacji',
        'results/allowed/plot_test_case_4_structs_I_01-11-22-15-17' : 'ZD1, 50% prawd. mutacji',
        'results/allowed/plot_test_case_5_structs_I_01-11-22-29-50' : 'ZD1, 75% prawd. mutacji',
        'results/allowed/plot_test_case_0_structs_I_01-11-21-20-25' : 'ZD1, 100% prawd. mutacji',
    }
    test_2_structs_II = {
        'results/allowed/plot_test_case_3_structs_II_01-11-22-04-02' : 'ZD2, 25% prawd. mutacji',
        'results/allowed/plot_test_case_4_structs_II_01-14-12-41-50' : 'ZD2, 50% prawd. mutacji',
        'results/allowed/plot_test_case_5_structs_II_01-11-22-32-51' : 'ZD2, 75% prawd. mutacji',
        'results/allowed/plot_test_case_0_structs_II_01-11-00-37-41' : 'ZD2, 100% prawd. mutacji'
    }
    test_2_structs_III = {
        'results/allowed/plot_test_case_3_structs_III_01-11-22-08-01' : 'ZD3, 25% prawd. mutacji',
        'results/allowed/plot_test_case_4_structs_III_01-11-22-21-31' : 'ZD3, 50% prawd. mutacji',
        'results/allowed/plot_test_case_5_structs_III_01-11-22-37-24' : 'ZD3, 75% prawd. mutacji',
        'results/allowed/plot_test_case_0_structs_III_01-11-21-26-51' : 'ZD3, 100% prawd. mutacji'
    }

    plot_compare_multiple_fitness_scores(plotname='results/final_results/ZD1_mutation_rate', **test_2_structs_I)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/ZD2_mutation_rate', **test_2_structs_II)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/ZD3_mutation_rate', **test_2_structs_III)

if __name__ == "__main__":
    main()