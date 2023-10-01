import random
import logging
from .classes.airport import Airport
from .classes.crew_member import Pilot, FlightAttendant
from .classes.flight import Flight
from .classes.plane import Plane
from .classes.scheduler_singleton import scheduler_instance

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Simulation:
    def __init__(self):
        self.scheduler = scheduler_instance 
        self.airports = []

    def print_airports(self):
        logging.info(f"---------------------------------------Airports:--------------------------------------")
        for i in self.airports:
            print(i)

    def print_structures(self):
        self.print_airports()
        for airport in self.airports:
            airport.show_fleet_and_crew()

    def generate_structs(self, airport_q=10, flights_q=20):
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

    def _create_crew(self, airport, pilots_q=80, attendants_q=160):
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
            while base == destination:  
                destination = random.choice(self.airports)
            
            # Filter flight attributes, so that the bases of crew and planes match the flight
            available_planes = [plane for plane in base.planes if plane.is_available]
            if not available_planes:
                logging.warning(f"Not enough available planes at the airport {base.id}")
                continue

            plane = random.choice(available_planes)
            flight = Flight(base, destination, plane)
            
            # Start the flight after a random delay
            delay = random.uniform(0, 60)  # Delay between 0.1 to 1 hour
            self.scheduler.schedule_event(delay, flight.start_flight)
            logging.info(f"Scheduled flight: {flight} starting at hour: {delay:.2f} of the simulation.")

    def run_simulation(self):
        # Run the simulation until all events are processed
        self.scheduler.run_until_no_events()