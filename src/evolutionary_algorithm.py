from structures import Structures
from solution import Solution

# Constants
TICKET_PRICE = 100
PLANE_OPERATIONAL_COST_PER_HOUR = 4000
PILOT_COST_PER_HOUR = 120
ATTENDANT_COST_PER_HOUR = 80
FLIGHT_CANCELLATION_COST_PER_PERSON = TICKET_PRICE*2
MAX_WEEKLY_HOURS = 60
OVERWORK_PENALTY_PER_HOUR = PILOT_COST_PER_HOUR*3

class EvolutionaryAlgorithm:
    def __init__(self, population_size=100):
        self.population_size = population_size
        self.population = []
        self.structures = Structures()

    def initialize_population(self):
        for _ in range(self.population_size):
            sol = Solution(self.structures.airports, 720)
            sol._schedule_flights(300)
            self.population.append((sol, -1))

    def fitness_function(self, sol):
        # Initializing metrics
        revenue = 0
        operational_costs = 0
        penalties = 0
        
        # 1. Calculate Revenue
        for flight in sol.flights:
            from_airport_idx = flight.base_airport.id - 1
            to_airport_idx = flight.destination_airport.id - 1
            day_of_flight = flight.day  # Assuming the Flight class has a day attribute
            demand = self.structures.passenger_demand[from_airport_idx][to_airport_idx][day_of_flight]
            
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

            for pilot in flight.pilots:
                if pilot.week_worked_hs > MAX_WEEKLY_HOURS:
                    penalties += OVERWORK_PENALTY_PER_HOUR * (pilot.week_worked_hs - MAX_WEEKLY_HOURS)
            
            for attendant in flight.crew:
                if attendant.week_worked_hs > MAX_WEEKLY_HOURS:
                    penalties += OVERWORK_PENALTY_PER_HOUR * (attendant.week_worked_hs - MAX_WEEKLY_HOURS)

        return revenue - operational_costs - penalties
