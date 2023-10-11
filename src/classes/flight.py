import math
import random
import logging

from src.solution import Solution

class Flight:
    _next_id = 1

    def __init__(self, base_airport, destination_airport, sol):
        self.id = Flight._next_id
        Flight._next_id += 1
        self.base_airport = base_airport
        self.destination_airport = destination_airport
        self.plane = None
        self.pilots = None
        self.crew = None
        self.distance = None
        self.duration = None
        self.status = "started"
        self.day_of_flight = None
        self.sol = sol


    def __repr__(self):
        return f"ID: {self.id}, from airport {self.base_airport.id} to airport {self.destination_airport.id}"


    def calculate_distance(self):
        return math.sqrt((self.base_airport.x - self.destination_airport.x)**2 +
                         (self.base_airport.y - self.destination_airport.y)**2)


    def calculate_duration(self):
        return self.distance / self.plane.speed


    def set_dist_and_dur(self):
        self.distance = self.calculate_distance()
        self.duration = self.calculate_duration()


    def start_flight(self):
        '''
        This function starts the flight and handles:
        - choosing the available crew and plane
        - flight cancelling
        - incrementing total flights count and cancelled flights in Solution class
        - calling flight_start from POV of plane and crew 

        To change: 2 and 4 harcoded as the number of needed pilots and attendants respectively
        '''
        # print("Start flight is called")
        logging.info(f"Choosing crew for the flight {self.id} from base {self.base_airport.id} to base {self.id}")

        #TODO: add checking for airports 

        available_pilots = [pilot for pilot in self.base_airport.pilots if pilot.is_eligible()]
        if len(available_pilots) < 2:
            self.cancel_flight(self.sol, "pilots")
            return

        available_attendants = [attendant for attendant in self.base_airport.attendants if attendant.is_eligible()]
        if len(available_attendants) < 4:
            self.cancel_flight(self.sol, "attendants")
            return

        available_planes = [plane for plane in self.base_airport.planes if plane.is_available]
        if not available_planes:
            self.cancel_flight(self.sol, "plane")
            return
        
        self.pilots = random.sample(available_pilots, 2)
        self.crew = random.sample(available_attendants, 4)
        self.plane = random.choice(available_planes)
        self.set_dist_and_dur()

        for pilot in self.pilots:
            pilot.flight_start(self.duration, self.destination_airport)
        
        for attendant in self.crew:
            attendant.flight_start(self.duration, self.destination_airport)

        self.plane.flight_start(self.destination_airport)
        self.base_airport.airport_maintenance()

        scheduler_instance = Solution.get_scheduler_by_id(self.sol.id)
        logging.info(f"At hour {scheduler_instance.current_simulation_time:.2f}: Scheduled flight: {self}")
        scheduler_instance.schedule_event(self.duration, self.end_flight)


    def end_flight(self):
        self.status = "completed"
        self.plane.maintenance()
        for pilot in self.pilots:
            pilot.start_rest(min(12, self.duration))
        for attendant in self.crew:
            attendant.start_rest(min(12, self.duration))
        self.destination_airport.airport_maintenance()


    def cancel_flight(self, sol, reason):
        self.status = "cancelled"
        sol.cancelled_flights.append(self)
        if reason == "pilots":
            logging.warning(f"Flight {self.id}: Not enough available pilots at airport {self.base_airport.id}, flight cancelled.")
        elif reason == "attendants":
            logging.warning(f"Flight {self.id}: Not enough available attendants at airport {self.base_airport.id}, flight cancelled.")
        elif reason == "planes":
            logging.warning(f"Flight {self.id}: Not enough available planes at airport {self.base_airport.id}, flight cancelled.")
        else:
            logging.warning(f"Flights {self.id}: Flight cancelled, reason unspecified.")