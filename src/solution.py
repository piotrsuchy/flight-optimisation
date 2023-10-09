import random
import logging
from .classes.flight import Flight
from .classes.scheduler_singleton import scheduler_instance
from .passenger_demand import generate_demand_array

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# disabling the logging below the level of critical
# logging.disable(logging.CRITICAL)


class Solution:
    def __init__(self, solution_id, airports, simulation_hs):
        self.id = solution_id
        self.scheduler = scheduler_instance 
        self.airports = airports
        self.simulation_hs = simulation_hs 
        self.flights = []
        self.fitness_score = None

    def __str__(self):
        return f"Sol ID: {self.id}, Total Flights: {len(self.flights)}, fitness score: {self.fitness_score}"

    def _schedule_flights(self, flights_q):
        # Starting by choosing the base and destination of the flight
        for _ in range(flights_q):
            base = random.choice(self.airports)
            destination = random.choice(self.airports)
            while base == destination:  
                destination = random.choice(self.airports)
            
            # Filter flight attributes, so that the bases of crew and planes match the flight
            available_planes = [plane for plane in base.planes if plane.is_available]
            if not available_planes:
                logging.warning(f"Not enough available planes at the airport {base.id}")
                continue

            plane = random.choice(available_planes)
            flight = Flight(base, destination, plane, self)
            
            # Start the flight after a random delay
            delay = random.uniform(0, self.simulation_hs)  # Delay between 0.1 to 1 hour
            flight.day = int(delay / 24)
            self.scheduler.schedule_event(delay, flight.start_flight)
            logging.info(f"Sol {self.id}: Scheduled flight: {flight} starting at hour: {delay:.2f} of the simulation.")

    def run_events(self):
        # Run the simulation until all events are processed
        self.scheduler.run_until_no_events()
