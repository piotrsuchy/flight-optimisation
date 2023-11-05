import math
import random
import logging

DAY_LENGTH = 24
DELAY_IF_AIRPORT_BUSY = 0.5


class Flight:
    _next_id = 1

    def __init__(self, base_airport, destination_airport, sol, simulation_time):
        self.id = Flight._next_id
        Flight._next_id += 1
        self.base_airport = base_airport
        self.destination_airport = destination_airport
        self.simulation_time = simulation_time
        self.plane = None
        self.pilots = None
        self.attendants = None
        self.distance = None
        self.duration = None
        self.status = "started"
        self.day_of_flight = None
        self.delay = 0
        self.sol = sol

    def __repr__(self):
        return f"ID: {self.id}, from airport {self.base_airport.id} to airport {self.destination_airport.id}, time of the flight: {self.simulation_time:.2f}"

    def calculate_distance(self):
        return math.sqrt((self.base_airport.x - self.destination_airport.x)**2 +
                         (self.base_airport.y - self.destination_airport.y)**2)

    def calculate_duration(self):
        return self.distance / self.plane.speed

    def set_dist_and_dur(self):
        self.distance = self.calculate_distance()
        self.duration = self.calculate_duration()

    def assign_random_crew(self):
        available_pilots = self.base_airport.get_eligible_pilots()
        if len(available_pilots) < 2:
            self.cancel_flight(self.sol, "pilots")
            return

        available_attendants = self.base_airport.get_eligible_attendants()
        if len(available_attendants) < 4:
            self.cancel_flight(self.sol, "attendants")
            return

        available_planes = self.base_airport.get_available_planes()

        available_planes = [
            plane for plane in self.base_airport.planes if plane.is_available]
        if not available_planes:
            self.cancel_flight(self.sol, "plane")
            return

        # random heuristic - could be a different one
        self.pilots = random.sample(available_pilots, 2)
        self.attendants = random.sample(available_attendants, 4)
        self.plane = random.choice(available_planes)

    def assign_crew(self):
        # take the base airport
        # take it's availability log
        # based on the simulation_time 
        # we can know the available crew members
        # we will take for example based on some 
        # heuristic like smallest ID
        # or the first in the list 
        # or the least amount of worked hours
        # and assign the crew to the flight
        pass

    def start_flight(self):
        '''
        This function starts the flight and handles:
        - assigning random crew if it has no pilot or attendant already assigned
        - incrementing total flights count and cancelled flights in Solution class
        - calling flight_start from POV of plane and crew 

        To change: 2 and 4 harcoded as the number of needed pilots and attendants respectively
        '''
        if self.pilot is None or self.attendants is None:
            logging.info(f"For flight: {self.id}, crew assignment was performed.")
            self.assign_random_crew()
        # print("Start flight is called")
        logging.info(
            f"Choosing crew for the flight {self.id} from base {self.base_airport.id} to base {self.id}")

        # if the airport is not available - add a delay to the flight
        if self.base_airport.occupied:
            self.delay += DELAY_IF_AIRPORT_BUSY

        scheduler_instance = self.sol.get_scheduler_by_id(self.sol.id)
        current_time = scheduler_instance.current_simulation_time + self.delay
        self.simulation_time = current_time
        self.day_of_flight = int(current_time // DAY_LENGTH)

        if self.distance is None or self.duration is None:
            self.set_dist_and_dur()

        demand = self.sol.passenger_demand[self.base_airport.id -
                                           1][self.destination_airport.id - 1][self.day_of_flight - 1]
        self.passengers = min(demand, self.plane.capacity)
        self.sol.passengers_taken += self.passengers

        for pilot in self.pilots:
            pilot.flight_start(self.duration, self.destination_airport)

        for attendant in self.attendants:
            attendant.flight_start(self.duration, self.destination_airport)

        self.plane.flight_start(self.destination_airport)
        self.base_airport.airport_maintenance()

        self.base_airport.availability_log.flight_start_snapshot(
            self, current_time)
        logging.info(
            f"At hour {scheduler_instance.current_simulation_time:.2f}: Scheduled flight: {self}")
        scheduler_instance.schedule_event(self.duration, self.end_flight)

    def end_flight(self):
        self.status = "completed"
        self.plane.maintenance()
        for pilot in self.pilots:
            pilot.start_rest(min(12, self.duration))
        for attendant in self.attendants:
            attendant.start_rest(min(12, self.duration))
        self.destination_airport.airport_maintenance()

    def cancel_flight(self, sol, reason):
        self.status = "cancelled"
        sol.cancelled_flights.append(self)
        if reason == "pilots":
            logging.warning(
                f"Flight {self.id}: Not enough available pilots at airport {self.base_airport.id}, flight cancelled.")
        elif reason == "attendants":
            logging.warning(
                f"Flight {self.id}: Not enough available attendants at airport {self.base_airport.id}, flight cancelled.")
        elif reason == "planes":
            logging.warning(
                f"Flight {self.id}: Not enough available planes at airport {self.base_airport.id}, flight cancelled.")
        else:
            logging.warning(
                f"Flights {self.id}: Flight cancelled, reason unspecified.")
