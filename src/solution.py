import random
import logging
from .classes.flight import Flight
from .classes.scheduler_singleton import scheduler_instance
from .passenger_demand import generate_demand_array

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# disabling the logging below the level of critical
# logging.disable(logging.CRITICAL)


class Solution:
    def __init__(self, airports, simulation_hs):
        self.scheduler = scheduler_instance 
        self.airports = airports
        self.simulation_hs = simulation_hs 
        self.flights = []

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
            self.scheduler.schedule_event(delay, flight.start_flight)
            logging.info(f"Scheduled flight: {flight} starting at hour: {delay:.2f} of the simulation.")

    def run_simulation(self):
        # Run the simulation until all events are processed
        self.scheduler.run_until_no_events()