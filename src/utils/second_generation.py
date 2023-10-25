from decorators import timing_decorator

@timing_decorator
def update_all_fitness_scores(population):
    '''
    This function uses the fitness_function() method to calculate the fitness score
    of all solutions in the population
    '''
    for sol_id, sol in enumerate(population):
        revenue, operation_costs, penalties, delay_penalty = fitness_function(
            sol[0])
        population[sol_id][1] = [
            revenue, operation_costs, penalties, delay_penalty]
        population[sol_id][0].fitness_score = revenue - \
            operation_costs - penalties

@timing_decorator
def print_revenue_and_costs():
    for sol in population:
        print(
            f"Sol: {sol[0]}, rev: {sol[1][0]:.2e}, op_costs: {sol[1][1]:.2e}, penalties: {sol[1][2]:.2e}, delay_penalties: {sol[1][2]:.2e}")