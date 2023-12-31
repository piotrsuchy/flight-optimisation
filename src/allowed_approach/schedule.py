import random
import json
from .classes.flight import Flight


class Schedule:
    def __init__(self) -> None:
        self.flight_schedule = []

    def __str__(self):
        res = ""
        for flight in self.flight_schedule:
            res += f"{flight} \n"
        return res
    
    def __eq__(self, other):
        if not isinstance(other, Schedule):
            return False
        if len(self.flight_schedule) != len(other.flight_schedule):
            return False
        return all(self_flight == other_flight for self_flight, other_flight in zip(self.flight_schedule, other.flight_schedule))

    def create_random_schedule(
            self, sol, flights_q, simulation_length, seed=None):
        if seed is None:
            seed = 42
        random.seed(seed)

        for _ in range(flights_q):
            base = random.choice(sol.structures.airports)
            destination = random.choice(sol.structures.airports)
            while base == destination:
                destination = random.choice(sol.structures.airports)

            simulation_time = int(random.uniform(1, simulation_length))
            flight = Flight(base, destination, sol, simulation_time)

            flight.day = int(simulation_time / 24)
            self.flight_schedule.append(flight)
            self.sort_schedule_by_timestamp()
        random.seed(None)

    def create_schedule_from_json(self, sol, filename):
        with open(filename, 'r') as file:
            data = json.load(file)

        for flight_data in data["population"][sol.id - 1]:
            flight = self.create_flight_from_json(sol, flight_data)
            self.flight_schedule.append(flight)
        
        self.sort_schedule_by_timestamp()
        
    def create_flight_from_json(self, sol, flight_data):
        source_airport_id, destination_airport_id, _, _, _, _, _, _, _, timestamp = flight_data
        source_airport = sol.structures.airports[source_airport_id - 1]
        destination_airport = sol.structures.airports[destination_airport_id - 1]

        return Flight(source_airport, destination_airport, sol, timestamp)

    def assign_sols_to_flights(self, sol):
        for flight in self.flight_schedule:
            flight.sol = sol

    def sort_schedule_by_timestamp(self):
        self.flight_schedule.sort(key=lambda x: x.simulation_time)
