import random
from flight import Flight

class Schedule:
    def __init__(self) -> None:
        self.flight_schedule = []

    def create_random_schedule(self, airports, flights_q, simulation_length):
        for _ in range(flights_q):
            base = random.choice(airports)
            destination = random.choice(airports)
            while base == destination:
                destination = random.choice(airports)

            simulation_time = random.uniform(0, simulation_length)
            flight = Flight(base, destination, None, simulation_time)

            flight.day = int(simulation_time / 24)
            self.flight_schedule.append(flight)
            self.sort_schedule_by_timestamp()
        
    def assign_sols_to_flights(self, sol):
        for flight in self.flight_schedule:
            flight.sol = sol
    
    def sort_schedule_by_timestamp(self):
        self.flight_schedule.sort(key=lambda x: x.simulation_time)