import logging
import json
import random
from src.allowed_approach.classes.airport import Airport
from src.allowed_approach.classes.crew_member import Pilot, FlightAttendant

with open('parameters.json') as parameters_file:
    config = json.load(parameters_file)

class Structures:
    def __init__(self, n_airports=config['structs']['N_AIRPORTS'], n_pilots_f_a=config['structs']['N_PILOTS_F_A'],
                 n_attendants_f_a=config['structs']['N_ATTENDANTS_F_A'], filename=None):
        self.airports = []
        self.n_airports = n_airports
        self.n_pilots_f_a = n_pilots_f_a
        self.n_attendants_f_a = n_attendants_f_a
        if filename is None:
            self.generate_structs()
        else:
            self.generate_structs_based_on_json(filename)
                
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
    
    def fill_in_distance_matrix(self):
        distance_matrix = [[None for _ in range(config['structs']['N_AIRPORTS'])] for _ in range(config['structs']['N_AIRPORTS'])]
        for i in range(config['structs']['N_AIRPORTS']):
            for j in range(0, i):
                distance = int(random.randint(config['structs']['MIN_DIST'], config['structs']['MAX_DIST']))
                distance_matrix[i][j] = distance
                distance_matrix[j][i] = distance
        Airport.distance_matrix = distance_matrix

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

    def generate_structs_based_on_json(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)

        self._create_airports_based_on_json(data["distance_matrix"])
        self._create_crew_based_on_json(data["pilots_status_pop"][0], Pilot)
        self._create_crew_based_on_json(data["attend_status_pop"][0], FlightAttendant)
        for airport in self.airports:
            airport.availability_log.add_snapshot(0)

    def _create_airports_based_on_json(self, distance_matrix):
        self.n_airports = len(distance_matrix)
        self.airports = [Airport() for _ in range(self.n_airports)]

        Airport.set_distance_matrix(distance_matrix)

    def _create_crew_based_on_json(self, crew_status, CrewType):
        for idx, airport in enumerate(self.airports):
            airport_crew = [crew for crew in crew_status if crew['location'] == idx + 1]

            for crew in airport_crew:
                training_hours = crew['train_hs'][0]
                crew_member = CrewType(base=airport, training_hours=training_hours)
                if CrewType == Pilot:
                    airport.add_pilot(crew_member)
                elif CrewType == FlightAttendant:
                    airport.add_attendant(crew_member)

    def print_airports(self):
        logging.info(
            f"---------------------------------------Airports:--------------------------------------")
        for i in self.airports:
            print(i)

    def print_structures(self):
        self.print_airports()
        for airport in self.airports:
            airport.show_fleet_and_crew()
