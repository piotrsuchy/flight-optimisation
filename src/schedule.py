import random
from .classes.flight import Flight

class Schedule:
    def __init__(self) -> None:
        self.flight_schedule = []

    def __str__(self):
        res = ""
        for flight in self.flight_schedule:
            res += f"{flight} \n"
        return res

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

    def clear_assignments_from_timestamp(self, simulation_time):
        # Perform a binary search to find the index of the flight at the given simulation time
        low, high = 0, len(self.flight_schedule) - 1
        index = -1  # Default to -1 if no flight is found at the exact simulation time

        while low <= high:
            mid = (low + high) // 2
            mid_flight_time = self.flight_schedule[mid].simulation_time

            if mid_flight_time < simulation_time:
                low = mid + 1
            elif mid_flight_time > simulation_time:
                high = mid - 1
            else:  # exact match found
                index = mid
                break
        
        # If not found, find the next flight in the schedule after the simulation time
        if index == -1 and low < len(self.flight_schedule):
            index = low
        
        # Clear assignments for all flights from the found index onwards
        for flight in self.flight_schedule[index:]:
            if flight.simulation_time >= simulation_time:  # Proceed if the condition matches
                flight.pilots = None
                flight.attendant = None
                flight.plane = None
                flight.status = "started"