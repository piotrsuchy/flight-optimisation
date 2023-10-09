from .structures import Structures
from .solution import Solution
from .passenger_demand import generate_demand_array, visualize_demand

# Constants
TICKET_PRICE = 1000
PLANE_OPERATIONAL_COST_PER_HOUR = 2000
PILOT_COST_PER_HOUR = 120
ATTENDANT_COST_PER_HOUR = 80
FLIGHT_CANCELLATION_COST_PER_PERSON = TICKET_PRICE
MAX_WEEKLY_HOURS = 60
OVERWORK_PENALTY_PER_HOUR = PILOT_COST_PER_HOUR*2

class EvolutionaryAlgorithm:
    def __init__(self, population_size=100):
        self.population_size = population_size
        self.population = []
        self.structures = Structures()
        self.passenger_demand = generate_demand_array(self.structures.airports, 30)

    def initialize_population_and_run_events(self):
        for sol_id in range(self.population_size):
            sol = Solution(sol_id+1, self.structures.airports, 720)
            sol._schedule_flights(150)
            sol.run_events()
            # population is a list of [sol, [revenue, op_costs, penalties]]
            self.population.append([sol, -1])


    def fitness_function(self, sol):
        '''
        This function calculates the fitness score of a single solution
        '''
        # Initializing metrics
        revenue = 0
        operational_costs = 0
        penalties = 0
        
        # 1. Calculate Revenue
        for flight in sol.flights:
            from_airport_idx = flight.base_airport.id - 1
            to_airport_idx = flight.destination_airport.id - 1
            day_of_flight = flight.day  # Assuming the Flight class has a day attribute
            demand = self.passenger_demand[from_airport_idx][to_airport_idx][day_of_flight]
            
            # Calculate seats filled (minimum of demand and plane capacity)
            filled_seats = min(demand, flight.plane.capacity)
            revenue += filled_seats * TICKET_PRICE
            
        # 2. Calculate Operational Costs
        for flight in sol.flights:
            flight_duration = flight.duration
            plane_cost = PLANE_OPERATIONAL_COST_PER_HOUR * flight_duration
            pilot_cost = PILOT_COST_PER_HOUR * flight_duration
            attendant_cost = ATTENDANT_COST_PER_HOUR * flight_duration
            operational_costs += plane_cost + 2 * pilot_cost + 4 * attendant_cost  # Assuming 2 pilots and 4 attendants
            
        # 3. Calculate Penalties
        for flight in sol.flights:
            if flight.status == "cancelled":
                penalties += FLIGHT_CANCELLATION_COST_PER_PERSON * filled_seats
                break

            try:
                for pilot in flight.pilots:
                    if pilot.week_worked_hs > MAX_WEEKLY_HOURS:
                        penalties += OVERWORK_PENALTY_PER_HOUR * (pilot.week_worked_hs - MAX_WEEKLY_HOURS)
            
                for attendant in flight.crew:
                    if attendant.week_worked_hs > MAX_WEEKLY_HOURS:
                        penalties += OVERWORK_PENALTY_PER_HOUR * (attendant.week_worked_hs - MAX_WEEKLY_HOURS)
            except TypeError:
                print(f"In sol: {sol.id} in flight: {flight.id} pilots or attendants are None")

        return [revenue, operational_costs, penalties]

    def update_all_fitness_scores(self):
        '''
        This function uses the fitness_function() method to calculate the fitness score
        of all solutions in the population
        '''
        for sol_id, sol in enumerate(self.population):
            revenue, operation_costs, penalties = self.fitness_function(sol[0])
            self.population[sol_id][1] = [revenue, operation_costs, penalties]
            self.population[sol_id][0].fitness_score = revenue - operation_costs - penalties


            
    def print_revenue_and_costs(self):
        for sol in self.population:
            print(f"Sol: {sol[0]}, revenue: {sol[1][0]}, operational_costs: {sol[1][1]}, penalties: {sol[1][2]}, fitness_function: {sol[1]}")