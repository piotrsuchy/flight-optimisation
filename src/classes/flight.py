import math
import random
import logging
from .scheduler_singleton import scheduler_instance

class Flight:
    _next_id = 1

    def __init__(self, base_airport, destination_airport, plane):
        self.id = Flight._next_id
        Flight._next_id += 1
        self.base_airport = base_airport
        self.destination_airport = destination_airport
        self.plane = plane
        self.pilots = None
        self.crew = None
        self.distance = self.calculate_distance()
        self.duration = self.calculate_duration()
        self.status = "started"

    def __repr__(self):
        return f"ID: {self.id}, Duration: {self.duration:.2f}, from airport {self.base_airport.id} to airport {self.destination_airport.id}"

    def calculate_distance(self):
        return math.sqrt((self.base_airport.x - self.destination_airport.x)**2 +
                         (self.base_airport.y - self.destination_airport.y)**2)

    def calculate_duration(self):
        return self.distance / self.plane.speed

    def start_flight(self):
        logging.info(f"Choosing crew for the flight {self.id} from base {self.base_airport.id} to base {self.id}, in the plane {self.plane.id}")
            # choose 2 pilots from the base_airport.pilots that have status is_available == True
            # if that is not possible - fewer than 2 available pilots - cancel flight and log that it is not possible
        available_pilots = [pilot for pilot in self.base_airport.pilots if pilot.is_available]
        if len(available_pilots) < 2:
            logging.warning(f"Flight {self.id}: Not enough available pilots at airport {self.base_airport.id}, flight cancelled")
            return

        # Now similarly for attendants, you can allocate them here.
        available_attendants = [attendant for attendant in self.base_airport.attendants if attendant.is_available]
        required_attendants = self.plane.attendants_needed
        if len(available_attendants) < required_attendants:
            logging.warning(f"Flight {self.id}: Not enough available attendants at airport {self.base_airport.id}, flight cancelled.")
            return
        
        self.pilots = random.sample(available_pilots, 2)
        self.crew = random.sample(available_attendants, 4)

        for pilot in self.pilots:
            pilot.flight_start(self.duration, self.destination_airport)
            pilot.occupy()
        
        for attendant in self.crew:
            attendant.flight_start(self.duration, self.destination_airport)
            attendant.occupy()

        logging.info(f"At hour {scheduler_instance.current_simulation_time:.2f}: Scheduled flight: {self}")
        
        # start flight from the plane's perspective
        self.plane.flight_start(self.destination_airport)
        # start flight from the airport's perspective
        self.base_airport.airport_maintenance()
        scheduler_instance.schedule_event(self.duration, self.end_flight)

    def end_flight(self):
        self.status = "completed"
        for pilot in self.pilots:
            pilot.start_rest(min(12, self.duration))
        for attendant in self.crew:
            attendant.start_rest(min(12, self.duration))
        self.destination_airport.airport_maintenance()