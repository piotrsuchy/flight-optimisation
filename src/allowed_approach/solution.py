import logging
import json
from .event_scheduler import EventScheduler

with open('parameters.json') as parameters_file:
    config = json.load(parameters_file)
    
class Solution:
    schedulers = {}

    def __init__(self, solution_id,
                 initial_structures, simulation_hs):
        self.id = solution_id
        self.initialized = "Initialized"
        self.scheduler = EventScheduler()
        Solution.schedulers[self.id] = self.scheduler
        self.scheduler.set_time(0)
        self.structures = initial_structures
        self.simulation_hs = simulation_hs
        self.flights = []
        self.fitness_score = None
        self.events = None
        self.schedule = None
        self.pilot_cancel = 0
        self.atten_cancel = 0
        self.training_penalty = 0
        self.dayoff_penalty = 0

    def __str__(self):
        return f"Sol ID: {self.id}, fitness score: {self.fitness_score}, status: {self.initialized}, Total Flights: {len(self.flights)}, Cancelled: {self.get_cancelled_flights_num()}"

    @staticmethod
    def get_scheduler_by_id(sol_id):
        return Solution.schedulers.get(sol_id)

    def get_scheduler_events(self):
        self.all_events = self.scheduler.get_events()
        for event in self.all_events:
            print(f"event: {event}")

    def get_cancelled_flights_num(self):
        cancelled_num = len([f for f in self.flights if f.status[-1] == "cancelled"])
        return cancelled_num

    def get_training_penal_num(self):
        return self.training_penalty / config['pen']['TRAINING_OVERLAP_PENALTY']

    def get_dayoff_penal_num(self):
        return self.dayoff_penalty / config['pen']['DAYOFF_PENALTY']

    def print_flight_simulation_times(self):
        for flight in self.flights:
            print(flight.simulation_time)

    def print_flights(self):
        for flight in self.flights:
            print(flight)

    def set_sol_ids(self, sol_id):
        for airport in self.structures.airports:
            airport.set_sol_id(sol_id)

            for pilot in airport.pilots:
                pilot.set_sol_id(sol_id)

            for attendant in airport.attendants:
                attendant.set_sol_id(sol_id)

    def _schedule_flights(self, heuristic):
        '''
        This function schedules flights_q flights for a solution by taking two different airports
        and scheduling the start_flight() method of class Flight for them using the existing
        Schedule structure.
        '''

        for flight in self.schedule.flight_schedule:
            # Assign crew to the flight based on AvailabilityLog
            scheduled_time = flight.simulation_time
            self.scheduler.schedule_event(scheduled_time, flight.start_flight, heuristic)
            self.flights.append(flight)
            logging.info(
                f"Sol {self.id}: Scheduled flight: {flight} starting at hour: {scheduled_time:.2f} of the simulation.")

    def run_events(self):
        '''
        This function runs all the events for a specific solution using a scheduler instance
        '''
        self.scheduler.run_until_no_events()
