from src.allowed_approach.visualisation import plot_compare_multiple_fitness_scores, plot_penalties

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

    # ----------------------------------------- APPROACH II ------------------------------------------------------- # 

    test_un_1_structs_I = {
        'results/unallowed/plot_test_case_0_structs_I_01-14-14-04-29' : 'ZD1, z aktualizacją',
        'results/unallowed/plot_test_case_1_structs_I_01-14-14-14-04' : 'ZD1, bez aktualizacji',
        'results/unallowed/plot_test_case_2_structs_I_01-14-14-23-38' : 'ZD1, losowo'
    }
    test_un_1_structs_II = {
        'results/unallowed/plot_test_case_0_structs_II_01-14-14-05-52' : 'ZD2, z aktualizacją',
        'results/unallowed/plot_test_case_1_structs_II_01-14-14-15-26' : 'ZD2, bez aktualizacji',
        'results/unallowed/plot_test_case_2_structs_II_01-14-14-24-55' : 'ZD2, losowo'
    }
    test_un_1_structs_III = {
        'results/unallowed/plot_test_case_0_structs_III_01-14-14-08-30' : 'ZD3, z aktualizacją',
        'results/unallowed/plot_test_case_1_structs_III_01-14-14-18-07' : 'ZD3, bez aktualizacji',
        'results/unallowed/plot_test_case_2_structs_III_01-14-14-27-27' : 'ZD3, losowo'
    }

    plot_compare_multiple_fitness_scores(plotname='results/final_results/unallowed/ZD1_initial_heuristic', **test_un_1_structs_I)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/unallowed/ZD2_initial_heuristic', **test_un_1_structs_II)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/unallowed/ZD3_initial_heuristic', **test_un_1_structs_III)

    plot_penalties('results/unallowed/plot_test_case_0_structs_I_01-14-14-04-29', 'unallowed/ZD1_with_update_penalties')
    plot_penalties('results/unallowed/plot_test_case_2_structs_I_01-14-14-23-38', 'unallowed/ZD1_random_penalties')

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
        'results/unallowed/plot_test_case_0_structs_I_01-14-14-04-29' : 'ZD1, 0% prawd. krzyżowania',
        'results/unallowed/plot_test_case_0_structs_I_01-14-19-11-02' : 'ZD1, 25% prawd. krzyżowania',
        'results/unallowed/plot_test_case_1_structs_I_01-14-19-20-29' : 'ZD1, 50% prawd. krzyżowania',
        'results/unallowed/plot_test_case_2_structs_I_01-14-19-29-57' : 'ZD1, 75% prawd. krzyżowania',
        'results/unallowed/plot_test_case_3_structs_I_01-14-19-39-07' : 'ZD1, 100% prawd. krzyżowania'
    }
    test_un_crossover_structs_II = {
        'results/unallowed/plot_test_case_0_structs_II_01-14-14-05-52' : 'ZD2, 0% prawd. krzyżowania',
        'results/unallowed/plot_test_case_0_structs_II_01-14-19-12-26' : 'ZD2, 25% prawd. krzyżowania',
        'results/unallowed/plot_test_case_1_structs_II_01-14-19-21-55' : 'ZD2, 50% prawd. krzyżowania',
        'results/unallowed/plot_test_case_2_structs_II_01-14-19-31-24' : 'ZD2, 75% prawd. krzyżowania',
        'results/unallowed/plot_test_case_3_structs_II_01-14-19-40-32' : 'ZD2, 100% prawd. krzyżowania'
    }
    test_un_crossover_structs_III = {
        'results/unallowed/plot_test_case_0_structs_III_01-14-14-08-30' : 'ZD3, 0% prawd. krzyżowania',
        'results/unallowed/plot_test_case_0_structs_III_01-14-19-15-03' : 'ZD3, 25% prawd. krzyżowania',
        'results/unallowed/plot_test_case_1_structs_III_01-14-19-24-33' : 'ZD3, 50% prawd. krzyżowania',
        'results/unallowed/plot_test_case_2_structs_III_01-14-19-33-58' : 'ZD3, 75% prawd. krzyżowania',
        'results/unallowed/plot_test_case_3_structs_III_01-14-19-43-07' : 'ZD3, 100% prawd. krzyżowania'
    }

    plot_compare_multiple_fitness_scores(plotname='results/final_results/unallowed/ZD1_cross_2', **test_un_crossover_structs_I)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/unallowed/ZD2_cross_2', **test_un_crossover_structs_II)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/unallowed/ZD3_cross_2', **test_un_crossover_structs_III)

    # --- test case - fix location heuristic

    test_un_lok_structs_I = {
        'results/unallowed/plot_test_case_6_structs_I_01-14-15-00-53' : '5% prawd. operatora naprawy lok.',
        'results/unallowed/plot_test_case_7_structs_I_01-14-15-09-57' : '15% prawd. operatora naprawy lok.',
        'results/unallowed/plot_test_case_8_structs_I_01-14-16-14-33' : '30% prawd. operatora naprawy lok.',
        'results/unallowed/plot_test_case_9_structs_I_01-14-16-26-38' : '60% prawd. operatora naprawy lok.'
    }
    test_un_lok_structs_II = {
        'results/unallowed/plot_test_case_6_structs_II_01-14-15-02-16' : '5% prawd. operatora naprawy lok.',
        'results/unallowed/plot_test_case_7_structs_II_01-14-15-11-22' : '15% prawd. operatora naprawy lok.',
        'results/unallowed/plot_test_case_8_structs_II_01-14-16-16-25' : '30% prawd. operatora naprawy lok.',
        'results/unallowed/plot_test_case_9_structs_II_01-14-16-28-24' : '60% prawd. operatora naprawy lok.'
    }
    test_un_lok_structs_III = {
        'results/unallowed/plot_test_case_6_structs_III_01-14-15-04-50' : '5% prawd. operatora naprawy lok.',
        'results/unallowed/plot_test_case_7_structs_III_01-14-15-13-58' : '15% prawd. operatora naprawy lok.',
        'results/unallowed/plot_test_case_8_structs_III_01-14-16-19-49' : '30% prawd. operatora naprawy lok.',
        'results/unallowed/plot_test_case_9_structs_III_01-14-16-31-50' : '60% prawd. operatora naprawy lok.'
    }

    plot_compare_multiple_fitness_scores(plotname='results/final_results/unallowed/ZD1_lok', **test_un_lok_structs_I)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/unallowed/ZD2_lok', **test_un_lok_structs_II)
    plot_compare_multiple_fitness_scores(plotname='results/final_results/unallowed/ZD3_lok', **test_un_lok_structs_III)



if __name__ == "__main__":
    main()