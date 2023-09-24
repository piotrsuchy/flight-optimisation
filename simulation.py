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

    def print_airports(self):
        logging.info(f"---------------------------------------Airports:--------------------------------------")
        for i in self.airports:
            print(i)

    def print_structures(self):
        self.print_airports()
        for airport in self.airports:
            airport.show_fleet_and_crew()

    def generate_structs(self, airport_q=20, flights_q=1000):
        logging.info(f"--------------------STRUCTURE GENERATION BEGAN--------------------")
        self._create_airports(airport_q)
        self._schedule_flights(flights_q)
        logging.info(f"--------------------STRUCTURE GENERATION ENDED--------------------")

    def _create_airports(self, quantity=5):
        for _ in range(quantity):
            airport = Airport()
            self.airports.append(airport)
            self._create_planes(airport, quantity=5)
            self._create_crew(airport, pilots_q=6, attendants_q=16)


    def _create_planes(self, airport, quantity=10):
        for _ in range(quantity):
            capacity = random.randint(50, 200)
            speed = random.uniform(500, 800)
            plane = Plane(capacity, base=airport, speed=speed, pilots_needed=2, attendants_needed=4)
            airport.add_plane(plane)  # Added directly to airport instance

    def _create_crew(self, airport, pilots_q=30, attendants_q=80):
        # Directly allocating pilots and attendants to the airport instance
        for _ in range(pilots_q):
            pilot = Pilot(airport)
            airport.add_pilot(pilot)
        
        for _ in range(attendants_q):
            attendant = FlightAttendant(airport)
            airport.add_attendant(attendant)


    def _schedule_flights(self, flights_q=10):
        # Starting by choosing the base and destination of the flight
        for _ in range(flights_q):
            base = random.choice(self.airports)
            destination = random.choice(self.airports)
            while base == destination:  # Make sure we don't pick the same airport
                destination = random.choice(self.airports)
            
            # Filter flight attributes, so that the bases of crew and planes match the flight
            available_planes = [plane for plane in base.planes if plane.ready]
            available_pilots = [pilot for pilot in base.pilots if pilot.is_available]
            available_attendants = [attendant for attendant in base.attendants if attendant.is_available]
            
            if not available_planes:
                logging.warning(f"Not enough planes at the airport {base.id}")
                continue

            plane = random.choice(available_planes)

            if len(available_pilots) < plane.pilots_needed:
                logging.warning(f"Not enough pilots at the airport {base.id}")
                continue
            if len(available_attendants) < plane.attendants_needed:
                logging.warning(f"Not enough pilots at the airport {base.id}")
                continue

            pilot_list = random.sample(available_pilots, plane.pilots_needed)
            attendant_list = random.sample(available_attendants, plane.attendants_needed)

            flight = Flight(base, destination, plane, pilot_list, attendant_list)
            
            # Start the flight after a random delay
            delay = random.uniform(0.1, 1)  # Delay between 0.1 to 1 hour
            self.scheduler.schedule_event(delay, flight.start_flight, self.scheduler)
            logging.info(f"At hour {self.scheduler.current_simulation_time:.2f}: Scheduled flight: {flight}")

    def run_simulation(self):
        # Run the simulation until all events are processed
        self.scheduler.run_until_no_events()