import random
import logging
from classes.airport import Airport
from classes.crew_member import Pilot, FlightAttendant
from classes.flight import Flight
from classes.plane import Plane
from classes.eventscheduler import EventScheduler

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Simulation:
    def __init__(self):
        self.scheduler = EventScheduler()
        self.airports = []
        self.planes = []
        self.pilots = []
        self.attendants = []

    def generate_structs(self, airport_q=5, plane_q=10, pilots_q=30, attend_q=80, flights_q=10):
        self._create_airports(airport_q)
        self._create_planes(plane_q)
        self._create_crew(pilots_q, attend_q)
        self._schedule_flights(flights_q)

    def _create_airports(self, quantity=5):
        for i in range(quantity):
            airport = Airport()
            airport.x = random.randint(0, 100)
            airport.y = random.randint(0, 100)
            airport.id = i + 1
            self.airports.append(airport)

    def _create_planes(self, quantity=10):
        for i in range(quantity):
            capacity = random.randint(50, 200)  # Random capacity between 50 and 200
            pilots_needed = 2  # Assuming each plane needs 2 pilots
            speed = random.uniform(500, 800)  # Speed between 500 to 800 km/h
            self.planes.append(Plane(capacity, pilots_needed, speed))

    def _create_crew(self, pilots_q=30, attendants_q=80):
        # Create 30 pilots and 80 flight attendants in random airports
        self.pilots = [Pilot(random.choice(self.airports)) for _ in range(pilots_q)]
        self.attendants = [FlightAttendant(random.choice(self.airports)) for _ in range(attendants_q)]

    def _schedule_flights(self, flights_q=10):
        for _ in range(flights_q):
            base = random.choice(self.airports)
            destination = random.choice(self.airports)
            while base == destination:  # Make sure we don't pick the same airport
                destination = random.choice(self.airports)
            
            plane = random.choice(self.planes)
            pilot_list = random.sample(self.pilots, plane.pilots_needed)
            attendant_list = random.sample(self.attendants, 2)  # Assuming 2 attendants per flight
            
            flight = Flight(base, destination, plane, pilot_list, attendant_list)
            
            # Start the flight after a random delay
            delay = random.uniform(0.1, 1)  # Delay between 0.1 to 1 hour
            self.scheduler.schedule_event(delay, flight.start_flight, self.scheduler)

    def run_simulation(self):
        # Run the simulation until all events are processed
        self.scheduler.run_until_no_events()