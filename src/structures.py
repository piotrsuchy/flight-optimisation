import logging
import random

from .classes.airport import Airport
from .classes.plane import Plane
from .classes.crew_member import Pilot, FlightAttendant


class Structures:
    def __init__(self, n_airports=10, n_pilots_f_a=12, n_attendants_f_a=24, n_planes_f_a=8):
        self.airports = []
        self.n_airports = n_airports
        self.n_pilots_f_a = n_pilots_f_a
        self.n_attendants_f_a = n_attendants_f_a
        self.n_planes_f_a = n_planes_f_a
        self.generate_structs()


    def generate_structs(self):
        logging.info(f"--------------------STRUCTURE GENERATION BEGAN--------------------")
        self._create_airports(self.n_airports)
        for airport in self.airports:
            self._create_crew(airport, self.n_pilots_f_a, self.n_attendants_f_a)
            self._create_planes(airport, self.n_planes_f_a)
            airport.availability_log.add_snapshot(0)
        logging.info(f"--------------------STRUCTURE GENERATION ENDED--------------------")


    def _create_airports(self, quantity):
        for _ in range(quantity):
            airport = Airport()
            self.airports.append(airport)
            self._create_planes(airport, quantity=self.n_planes_f_a)
            self._create_crew(airport, pilots_q=self.n_pilots_f_a, attendants_q=self.n_attendants_f_a)


    def _create_planes(self, airport, quantity):
        for _ in range(quantity):
            capacity = random.randint(50, 400)
            speed = random.uniform(500, 800)
            plane = Plane(capacity, base=airport, speed=speed, pilots_needed=2, attendants_needed=4)
            airport.add_plane(plane)  # Added directly to airport instance


    def _create_crew(self, airport, pilots_q, attendants_q):
        # Directly allocating pilots and attendants to the airport instance
        for _ in range(pilots_q):
            pilot = Pilot(airport)
            airport.add_pilot(pilot)
        
        for _ in range(attendants_q):
            attendant = FlightAttendant(airport)
            airport.add_attendant(attendant)


    def print_airports(self):
        logging.info(f"---------------------------------------Airports:--------------------------------------")
        for i in self.airports:
            print(i)


    def print_structures(self):
        self.print_airports()
        for airport in self.airports:
            airport.show_fleet_and_crew()