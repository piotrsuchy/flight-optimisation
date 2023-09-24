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

    def print_airports(self):
        logging.info(f"---------------------------------------Airports:--------------------------------------")
        for i in self.airports:
            print(i)

    def print_pilots(self):
        logging.info(f"---------------------------------------Pilots:----------------------------------------")
        for i in self.pilots:
            print(i)

    def print_attendants(self):
        logging.info(f"---------------------------------------Attendants:------------------------------------")
        for i in self.attendants:
            print(i)

    def print_planes(self):
        logging.info(f"---------------------------------------Planes:----------------------------------------")
        for i in self.planes:
            print(i)   

    def print_structures(self):
        self.print_airports()
        self.print_pilots()
        self.print_attendants()
        self.print_planes()

    def generate_structs(self, airport_q=5, plane_q=10, pilots_q=30, attend_q=80, flights_q=10):
        logging.info(f"--------------------STRUCTURE GENERATION BEGAN--------------------")
        self._create_airports(airport_q)
        self._create_planes(plane_q)
        self._create_crew(pilots_q, attend_q)
        self._schedule_flights(flights_q)
        logging.info(f"--------------------STRUCTURE GENERATION ENDED--------------------")

    def _create_airports(self, quantity=5):
        for i in range(quantity):
            airport = Airport()
            airport.x = random.randint(0, 10000)
            airport.y = random.randint(0, 10000)
            airport.id = i + 1
            self.airports.append(airport)

    def _create_planes(self, quantity=10):
        for i in range(quantity):
            base = random.choice(self.airports)
            capacity = random.randint(50, 200)  # Random capacity between 50 and 200
            speed = random.uniform(500, 800)  # Speed between 500 to 800 km/h
            self.planes.append(Plane(capacity, base=base, speed=speed, pilots_needed=2, attendants_needed=4))

    def _create_crew(self, pilots_q=30, attendants_q=80):
        # Create 30 pilots and 80 flight attendants in random airports
        self.pilots = [Pilot(random.choice(self.airports)) for _ in range(pilots_q)]
        self.attendants = [FlightAttendant(random.choice(self.airports)) for _ in range(attendants_q)]

    def _schedule_flights(self, flights_q=10):
        # Starting by choosing the base and destination of the flight
        for _ in range(flights_q):
            base = random.choice(self.airports)
            destination = random.choice(self.airports)
            while base == destination:  # Make sure we don't pick the same airport
                destination = random.choice(self.airports)
            
            # Filter flight attributes, so that the bases of crew and planes match the flight
            available_planes = [plane for plane in self.planes if plane.base == base]
            available_pilots = [pilot for pilot in self.pilots if pilot.current_base == base]
            available_attendants = [attendant for attendant in self.attendants if attendant.current_base == base]
            
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
            logging.info(f"At hour {self.scheduler.current_simulation_time:.2f}: Scheduled flight from {base} to {destination} with delay {delay:.2f} hours.")

    def run_simulation(self):
        # Run the simulation until all events are processed
        self.scheduler.run_until_no_events()