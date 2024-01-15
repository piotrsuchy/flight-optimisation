from src.allowed_approach.visualisation import plot_compare_multiple_fitness_scores, plot_penalties

def main():
    test_1_with_init_struct_I = {
        'results/allowed/plot_test_case_0_structs_I_01-11-21-20-25': 'with_init, work_time',
        'results/allowed/plot_test_case_1_structs_I_01-11-21-33-27': 'with_init, random',
        'results/allowed/plot_test_case_2_structs_I_01-11-21-48-02': 'with_init, smallest_id',
    }
    test_1_with_init_struct_II = {
        'results/allowed/plot_test_case_0_structs_II_01-11-00-37-41': 'with_init, work_time',
        'results/allowed/plot_test_case_1_structs_II_01-11-21-36-34': 'with_init, random',
        'results/allowed/plot_test_case_2_structs_II_01-11-21-50-39': 'with_init, smallest_id',
    }
    test_1_with_init_struct_III = {
        'results/allowed/plot_test_case_0_structs_III_01-11-21-26-51': 'with_init, work_time',
        'results/allowed/plot_test_case_1_structs_III_01-11-21-40-40': 'with_init, random',
        'results/allowed/plot_test_case_2_structs_III_01-11-21-54-03': 'with_init, smallest_id',
    }
    test_1_two_pop_struct_I = {
        'results/allowed/plot_test_case_two_pop0_structs_I_01-14-09-53-07': 'two_pop, work_time',
        'results/allowed/plot_test_case_two_pop1_structs_I_01-14-10-01-47': 'two_pop, random',
        'results/allowed/plot_test_case_two_pop2_structs_I_01-14-10-10-22': 'two_pop, smallest_id'
    }
    test_1_two_pop_struct_II = {
        'results/allowed/plot_test_case_two_pop0_structs_II_01-14-09-54-33': 'two_pop, work_time',
        'results/allowed/plot_test_case_two_pop1_structs_II_01-14-10-03-08': 'two_pop, random',
        'results/allowed/plot_test_case_two_pop2_structs_II_01-14-10-11-57': 'two_pop, smallest_id'
    }
    test_1_two_pop_struct_III = {
        'results/allowed/plot_test_case_two_pop0_structs_III_01-14-09-57-01': 'two_pop, work_time',
        'results/allowed/plot_test_case_two_pop1_structs_III_01-14-10-05-38': 'two_pop, random',
        'results/allowed/plot_test_case_two_pop2_structs_III_01-14-10-14-14': 'two_pop, smallest_id'
    }
    
    plot_compare_multiple_fitness_scores(plotname='results/final_results/ZD1_with_init_allowed_heuristic_3', moving_avg_period=0, **test_1_with_init_struct_I)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/ZD2_with_init_allowed_heuristic_3', moving_avg_period=0, **test_1_with_init_struct_II)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/ZD3_with_init_allowed_heuristic_3', moving_avg_period=0, **test_1_with_init_struct_III)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/ZD1_two_pop_allowed_heuristic_3', moving_avg_period=0, **test_1_two_pop_struct_I)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/ZD2_two_pop_allowed_heuristic_3', moving_avg_period=0, **test_1_two_pop_struct_II)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/ZD3_two_pop_allowed_heuristic_3', moving_avg_period=0, **test_1_two_pop_struct_III)

    test_2_structs_I = {
        'results/allowed/plot_test_case_3_structs_I_01-11-22-01-46' : '25% prawd. mutacji',
        'results/allowed/plot_test_case_4_structs_I_01-11-22-15-17' : '50% prawd. mutacji',
        'results/allowed/plot_test_case_5_structs_I_01-11-22-29-50' : '75% prawd. mutacji',
        'results/allowed/plot_test_case_0_structs_I_01-11-21-20-25' : '100% prawd. mutacji',
    }
    test_2_structs_II = {
        'results/allowed/plot_test_case_3_structs_II_01-11-22-04-02' : '25% prawd. mutacji',
        'results/allowed/plot_test_case_4_structs_II_01-14-12-41-50' : '50% prawd. mutacji',
        'results/allowed/plot_test_case_5_structs_II_01-11-22-32-51' : '75% prawd. mutacji',
        'results/allowed/plot_test_case_0_structs_II_01-11-00-37-41' : '100% prawd. mutacji'
    }
    test_2_structs_III = {
        'results/allowed/plot_test_case_3_structs_III_01-11-22-08-01' : '25% prawd. mutacji',
        'results/allowed/plot_test_case_4_structs_III_01-11-22-21-31' : '50% prawd. mutacji',
        'results/allowed/plot_test_case_5_structs_III_01-11-22-37-24' : '75% prawd. mutacji',
        'results/allowed/plot_test_case_0_structs_III_01-11-21-26-51' : '100% prawd. mutacji'
    }

    plot_compare_multiple_fitness_scores(plotname='results/final_results/ZD1_mutation_rate_3', moving_avg_period=0, **test_2_structs_I)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/ZD2_mutation_rate_3', moving_avg_period=0, **test_2_structs_II)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/ZD3_mutation_rate_3', moving_avg_period=0, **test_2_structs_III)

    # ----------------------------------------- APPROACH II ------------------------------------------------------- # 

    test_un_1_structs_I = {
        'results/unallowed/plot_test_case_0_structs_I_01-14-14-04-29' : 'operator z aktualizacją',
        'results/unallowed/plot_test_case_1_structs_I_01-14-14-14-04' : 'operator bez aktualizacji',
        'results/unallowed/plot_test_case_2_structs_I_01-14-14-23-38' : 'operator losowy'
    }
    test_un_1_structs_II = {
        'results/unallowed/plot_test_case_0_structs_II_01-14-14-05-52' : 'operator z aktualizacją',
        'results/unallowed/plot_test_case_1_structs_II_01-14-14-15-26' : 'operator bez aktualizacji',
        'results/unallowed/plot_test_case_2_structs_II_01-14-14-24-55' : 'operator losowy'
    }
    test_un_1_structs_III = {
        'results/unallowed/plot_test_case_0_structs_III_01-14-14-08-30' : 'operator z aktualizacją',
        'results/unallowed/plot_test_case_1_structs_III_01-14-14-18-07' : 'operator bez aktualizacji',
        'results/unallowed/plot_test_case_2_structs_III_01-14-14-27-27' : 'operator losowy'
    }

    plot_compare_multiple_fitness_scores(plotname='results/final_results/unallowed/ZD1_initial_heuristic_3', moving_avg_period=5, line_width=0.7, **test_un_1_structs_I)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/unallowed/ZD2_initial_heuristic_3', moving_avg_period=5, line_width=0.7, **test_un_1_structs_II)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/unallowed/ZD3_initial_heuristic_3', moving_avg_period=5, line_width=0.7, **test_un_1_structs_III)

    plot_penalties('results/unallowed/plot_test_case_0_structs_I_01-14-14-04-29', 'unallowed/ZD1_with_update_penalties_3')
    plot_penalties('results/unallowed/plot_test_case_2_structs_I_01-14-14-23-38', 'unallowed/ZD1_random_penalties_3')

    # --- test case - crossover probability
    # test_un_2_structs_I = {
    #     'results/unallowed/plot_test_case_0_structs_I_01-14-14-04-29' : 'ZD1, 0% prawd. krzyżowania',
    #     'results/unallowed/plot_test_case_3_structs_I_01-14-14-32-58' : 'ZD1, 20% prawd. krzyżowania',
    #     'results/unallowed/plot_test_case_4_structs_I_01-14-14-42-21' : 'ZD1, 40% prawd. krzyżowania',
    #     'results/unallowed/plot_test_case_5_structs_I_01-14-14-51-34' : 'ZD1, 60% prawd. krzyżowania'
    # }
    # test_un_2_structs_II = {
    #     'results/unallowed/plot_test_case_0_structs_II_01-14-14-05-52' : 'ZD2, 0% prawd. krzyżowania',
    #     'results/unallowed/plot_test_case_3_structs_II_01-14-14-34-23' : 'ZD2, 20% prawd. krzyżowania',
    #     'results/unallowed/plot_test_case_4_structs_II_01-14-14-43-46' : 'ZD2, 40% prawd. krzyżowania',
    #     'results/unallowed/plot_test_case_5_structs_II_01-14-14-52-59' : 'ZD2, 60% prawd. krzyżowania'
    # }
    # test_un_2_structs_III = {
    #     'results/unallowed/plot_test_case_0_structs_III_01-14-14-08-30' : 'ZD3, 0% prawd. krzyżowania',
    #     'results/unallowed/plot_test_case_3_structs_III_01-14-14-37-00' : 'ZD3, 20% prawd. krzyżowania',
    #     'results/unallowed/plot_test_case_4_structs_III_01-14-14-46-22' : 'ZD3, 40% prawd. krzyżowania',
    #     'results/unallowed/plot_test_case_5_structs_III_01-14-14-55-37' : 'ZD3, 60% prawd. krzyżowania'
    # }

    # plot_compare_multiple_fitness_scores(plotname='results/final_results/unallowed/ZD1_krzyż', **test_un_2_structs_I)
    # plot_compare_multiple_fitness_scores(plotname='results/final_results/unallowed/ZD2_krzyż', **test_un_2_structs_II)
    # plot_compare_multiple_fitness_scores(plotname='results/final_results/unallowed/ZD3_krzyż', **test_un_2_structs_III)

    test_un_crossover_structs_I = {
        'results/unallowed/plot_test_case_0_structs_I_01-14-14-04-29' : '0% prawd. krzyżowania',
        'results/unallowed/plot_test_case_0_structs_I_01-14-19-11-02' : '25% prawd. krzyżowania',
        'results/unallowed/plot_test_case_1_structs_I_01-14-19-20-29' : '50% prawd. krzyżowania',
        'results/unallowed/plot_test_case_2_structs_I_01-14-19-29-57' : '75% prawd. krzyżowania',
        'results/unallowed/plot_test_case_3_structs_I_01-14-19-39-07' : '100% prawd. krzyżowania'
    }
    test_un_crossover_structs_II = {
        'results/unallowed/plot_test_case_0_structs_II_01-14-14-05-52' : '0% prawd. krzyżowania',
        'results/unallowed/plot_test_case_0_structs_II_01-14-19-12-26' : '25% prawd. krzyżowania',
        'results/unallowed/plot_test_case_1_structs_II_01-14-19-21-55' : '50% prawd. krzyżowania',
        'results/unallowed/plot_test_case_2_structs_II_01-14-19-31-24' : '75% prawd. krzyżowania',
        'results/unallowed/plot_test_case_3_structs_II_01-14-19-40-32' : '100% prawd. krzyżowania'
    }
    test_un_crossover_structs_III = {
        'results/unallowed/plot_test_case_0_structs_III_01-14-14-08-30' : '0% prawd. krzyżowania',
        'results/unallowed/plot_test_case_0_structs_III_01-14-19-15-03' : '25% prawd. krzyżowania',
        'results/unallowed/plot_test_case_1_structs_III_01-14-19-24-33' : '50% prawd. krzyżowania',
        'results/unallowed/plot_test_case_2_structs_III_01-14-19-33-58' : '75% prawd. krzyżowania',
        'results/unallowed/plot_test_case_3_structs_III_01-14-19-43-07' : '100% prawd. krzyżowania'
    }

    plot_compare_multiple_fitness_scores(plotname='results/final_results/unallowed/ZD1_cross_3', moving_avg_period=20, line_width=0.5, **test_un_crossover_structs_I)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/unallowed/ZD2_cross_3', moving_avg_period=10, line_width=1, **test_un_crossover_structs_II)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/unallowed/ZD3_cross_3', moving_avg_period=10, line_width=1, **test_un_crossover_structs_III)

    # --- test case - fix location heuristic

    test_un_lok_structs_I = {
        'results/unallowed/plot_test_case_6_structs_I_01-14-15-00-53' : '5% prawd. naprawy lok.',
        'results/unallowed/plot_test_case_7_structs_I_01-14-15-09-57' : '15% prawd. naprawy lok.',
        'results/unallowed/plot_test_case_8_structs_I_01-14-16-14-33' : '30% prawd. naprawy lok.',
        'results/unallowed/plot_test_case_9_structs_I_01-14-16-26-38' : '60% prawd. naprawy lok.'
    }
    test_un_lok_structs_II = {
        'results/unallowed/plot_test_case_6_structs_II_01-14-15-02-16' : '5% prawd. naprawy lok.',
        'results/unallowed/plot_test_case_7_structs_II_01-14-15-11-22' : '15% prawd. naprawy lok.',
        'results/unallowed/plot_test_case_8_structs_II_01-14-16-16-25' : '30% prawd. naprawy lok.',
        'results/unallowed/plot_test_case_9_structs_II_01-14-16-28-24' : '60% prawd. naprawy lok.'
    }
    test_un_lok_structs_III = {
        'results/unallowed/plot_test_case_6_structs_III_01-14-15-04-50' : '5% prawd. naprawy lok.',
        'results/unallowed/plot_test_case_7_structs_III_01-14-15-13-58' : '15% prawd. naprawy lok.',
        'results/unallowed/plot_test_case_8_structs_III_01-14-16-19-49' : '30% prawd. naprawy lok.',
        'results/unallowed/plot_test_case_9_structs_III_01-14-16-31-50' : '60% prawd. naprawy lok.'
    }

    plot_compare_multiple_fitness_scores(plotname='results/final_results/unallowed/ZD1_lok_3', moving_avg_period=20, line_width=0.5, **test_un_lok_structs_I)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/unallowed/ZD2_lok_3', moving_avg_period=20, line_width=0.5, **test_un_lok_structs_II)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/unallowed/ZD3_lok_3', moving_avg_period=20, line_width=0.5, **test_un_lok_structs_III)



if __name__ == "__main__":
    main()