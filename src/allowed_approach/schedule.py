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

    def assign_sols_to_flights(self, sol):
        for flight in self.flight_schedule:
            flight.sol = sol

    def sort_schedule_by_timestamp(self):
        self.flight_schedule.sort(key=lambda x: x.simulation_time)
