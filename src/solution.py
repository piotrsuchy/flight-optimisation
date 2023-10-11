import random
import logging

from .event_scheduler import EventScheduler

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)


class Solution:
    schedulers = {}

    def __init__(self, solution_id, initial_structures, simulation_hs):
        self.id = solution_id
        self.scheduler = EventScheduler()
        Solution.schedulers[self.id] = self.scheduler
        self.structures = initial_structures
        self.simulation_hs = simulation_hs 
        self.flights = []
        self.cancelled_flights = []
        self.fitness_score = None

    def __str__(self):
        return f"Sol ID: {self.id}, Total Flights: {len(self.flights)}, Cancelled: {self.get_cancelled_flights_num()}, Fitness score: {self.fitness_score:.2e}"

    @staticmethod
    def get_scheduler_by_id(sol_id):
        return Solution.schedulers.get(sol_id)

    def set_sol_ids(self, sol_id):
        for airport in self.structures.airports:
            airport.set_sol_id(sol_id)
            for plane in airport.planes:
                plane.set_sol_id(sol_id)

            for pilot in airport.pilots:
                pilot.set_sol_id(sol_id)

            for attendant in airport.attendants:
                attendant.set_sol_id(sol_id)

    def _schedule_flights(self, flights_q):
        '''
        This function schedules flights_q flights for a solution by taking two different airports 
        and scheduling the start_flight() method of class Flight for them
        '''
        from .classes.flight import Flight
        for _ in range(flights_q):
            base = random.choice(self.structures.airports)
            destination = random.choice(self.structures.airports)
            while base == destination:  
                destination = random.choice(self.structures.airports)
            
            flight = Flight(base, destination, self)
            self.flights.append(flight)
            
            # Start the flight after a random delay
            delay = random.uniform(0, self.simulation_hs)  # Delay between 0.1 to 1 hour
            flight.day = int(delay / 24)
            self.scheduler.schedule_event(delay, flight.start_flight)
            logging.info(f"Sol {self.id}: Scheduled flight: {flight} starting at hour: {delay:.2f} of the simulation.")

    def get_cancelled_flights_num(self):
        return len(self.cancelled_flights)

    def run_events(self):
        '''
        This function runs all the events for a specific solution using a scheduler instance
        '''
        self.scheduler.run_until_no_events()

