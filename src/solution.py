import random
import logging

from .schedule import Schedule
from .event_scheduler import EventScheduler


class Solution:
    schedulers = {}

    def __init__(self, solution_id, passenger_demand, initial_structures, simulation_hs):
        self.id = solution_id
        self.scheduler = EventScheduler()
        self.passenger_demand = passenger_demand
        Solution.schedulers[self.id] = self.scheduler
        self.structures = initial_structures
        self.simulation_hs = simulation_hs
        self.flights = []
        self.cancelled_flights = []
        self.passengers_taken = 0
        self.fitness_score = None
        self.events = None
        self.schedule = None

    def __str__(self):
        return f"Sol ID: {self.id}, Total Flights: {len(self.flights)}, Cancelled: {self.get_cancelled_flights_num()}, Fitness score: {self.fitness_score:.2e}, passengers taken: {self.passengers_taken}"

    @staticmethod
    def get_scheduler_by_id(sol_id):
        return Solution.schedulers.get(sol_id)

    def print_flights(self):
        for flight in self.flights:
            print(flight)

    def get_scheduler_events(self):
        self.all_events = self.scheduler.get_events()
        return self.all_events

    def set_sol_ids(self, sol_id):
        for airport in self.structures.airports:
            airport.set_sol_id(sol_id)
            print("setting sol for airport ", airport.id)
            for plane in airport.planes:
                plane.set_sol_id(sol_id)

            for pilot in airport.pilots:
                pilot.set_sol_id(sol_id)

            for attendant in airport.attendants:
                attendant.set_sol_id(sol_id)

    def _schedule_flights(self):
        '''
        This function schedules flights_q flights for a solution by taking two different airports
        and scheduling the start_flight() method of class Flight for them using the existing
        Schedule structure.
        '''
        
        for flight in self.schedule.flight_schedule:
            # Assign crew to the flight based on AvailabilityLog
            scheduled_time = flight.simulation_time
            print(f"Scheduling flight {flight}")
            self.scheduler.schedule_event(scheduled_time, flight.start_flight)
            self.flights.append(flight)
            print(f"Current simulation time: {self.scheduler.current_simulation_time}")
            logging.info(
                f"Sol {self.id}: Scheduled flight: {flight} starting at hour: {scheduled_time:.2f} of the simulation.")

    def get_cancelled_flights_num(self):
        return len(self.cancelled_flights)

    def run_events(self):
        '''
        This function runs all the events for a specific solution using a scheduler instance
        '''
        self.scheduler.run_until_no_events()
