import logging
import json

from .classes.airport import Airport
from .classes.crew_member import Pilot, FlightAttendant

with open('parameters.json') as parameters_file:
    config = json.load(parameters_file)

class Structures:
    def __init__(self, n_airports=config['structs']['N_AIRPORTS'], n_pilots_f_a=config['structs']['N_PILOTS_F_A'],
                 n_attendants_f_a=config['structs']['N_ATTENDANTS_F_A']):
        self.airports = []
        self.n_airports = n_airports
        self.n_pilots_f_a = n_pilots_f_a
        self.n_attendants_f_a = n_attendants_f_a
        self.generate_structs()
    
    def __eq__(self, other):
        if not isinstance(other, Structures):
            return False
        if self.n_airports != other.n_airports or self.n_pilots_f_a != other.n_pilots_f_a or self.n_attendants_f_a != other.n_attendants_f_a:
            print(f"The number of airports or pilots or attendants is not the same!")
            return False
        else:
            for self_airport, other_airport in zip(self.airport, other.airports):
                if self_airport.x != other_airport.x or self_airport.y != other_airport.y:
                    print(f"The coordinates of airports is not the same!")
                    return False
        return True 

    def generate_structs(self):
        logging.info(
            f"--------------------STRUCTURE GENERATION BEGAN--------------------")
        self._create_airports(self.n_airports)
        for airport in self.airports:
            # self._create_crew(airport, self.n_pilots_f_a,
                              # self.n_attendants_f_a)
            airport.availability_log.add_snapshot(0)
        logging.info(
            f"--------------------STRUCTURE GENERATION ENDED--------------------")

    def _create_airports(self, quantity):
        for _ in range(quantity):
            airport = Airport()
            self.airports.append(airport)
            self._create_crew(airport, pilots_q=self.n_pilots_f_a,
                              attendants_q=self.n_attendants_f_a)

    def _create_crew(self, airport, pilots_q, attendants_q):
        # Directly allocating pilots and attendants to the airport instance
        for _ in range(pilots_q):
            pilot = Pilot(airport)
            airport.add_pilot(pilot)

        for _ in range(attendants_q):
            attendant = FlightAttendant(airport)
            airport.add_attendant(attendant)

    def print_airports(self):
        logging.info(
            f"---------------------------------------Airports:--------------------------------------")
        for i in self.airports:
            print(i)

    def print_structures(self):
        self.print_airports()
        for airport in self.airports:
            airport.show_fleet_and_crew()
