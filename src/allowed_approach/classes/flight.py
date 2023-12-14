import math
import random

DAY_LENGTH = 24
DELAY_IF_AIRPORT_BUSY = 0


class Flight:
    _next_id = 1

    def __init__(self, base_airport, destination_airport,
                 sol, simulation_time):
        self.id = Flight._next_id
        Flight._next_id += 1
        self.base_airport = base_airport
        self.destination_airport = destination_airport
        self.simulation_time = simulation_time
        self.pilots = None
        self.attendants = None
        self.distance = None
        self.duration = None
        self.status = ["started"]
        self.day_of_flight = None
        self.delay = 0
        self.sol = sol

    def __repr__(self):
        return f"ID: {self.id}, from airport {self.base_airport.id} to airport {self.destination_airport.id}, time of the flight: {self.simulation_time:.2f}, status: {self.status}"

    def calculate_distance(self):
        return math.sqrt((self.base_airport.x - self.destination_airport.x)**2 +
                         (self.base_airport.y - self.destination_airport.y)**2)

    def calculate_duration(self):
        return self.distance / 700

    def set_dist_and_dur(self):
        self.distance = self.calculate_distance()
        self.duration = self.calculate_duration()

    def get_available_crew(self):
        available_pilots = self.base_airport.get_eligible_pilots()
        if len(available_pilots) < 2:
            self.cancel_flight(self.sol, "pilots")
            return False

        available_attendants = self.base_airport.get_eligible_attendants()
        if len(available_attendants) < 4:
            self.cancel_flight(self.sol, "attendants")
            return False

        return available_pilots, available_attendants
        

    def assign_random_crew(self) -> bool:
        res = self.get_available_crew()
        if not res:
            return False
        else:
            available_pilots = res[0]
            available_attendants = res[1]
        
        # random heuristic - could be a different one
        self.pilots = random.sample(available_pilots, 2)
        self.attendants = random.sample(available_attendants, 4)
        return True

    def assign_crew(self) -> bool:
        res = self.get_available_crew()
        if not res:
            return False
        else:
            available_pilots = res[0]
            available_attendants = res[1]

        # Assign the crew
        self.pilots = available_pilots[:2]  # get the first 2 eligible pilots
        self.attendants = available_attendants[:4]  # get the first 4 eligible attendants

        # Log the information about the assignment
        # logging.info(f"Assigned pilots for flight {self.id}: {[pilot.id for pilot in self.pilots]}")
        # logging.info(f"Assigned attendants for flight {self.id}: {[attendant.id for attendant in self.attendants]}")
        # logging.info(f"Available pilots: {[pilot.id for pilot in available_pilots]}")
        # logging.info(f"Available attendants: {[attendant.id for attendant in available_attendants]}")

        return True
        

    def start_flight(self):
        '''
        This function starts the flight and handles:
        - assigning random crew if it has no pilot or attendant already assigned
        - incrementing total flights count and cancelled flights in Solution class
        - calling flight_start from POV of crew
        '''
        if self.pilots is None or self.attendants is None:
            possible_assignment = self.assign_random_crew()
            if not possible_assignment:
                return

        # if the airport is not available - add a delay to the flight
        if self.base_airport.occupied:
            self.delay += DELAY_IF_AIRPORT_BUSY

        self.day_of_flight = int(self.simulation_time // DAY_LENGTH)

        if self.distance is None or self.duration is None:
            self.set_dist_and_dur()

        for pilot in self.pilots:
            pilot.flight_start(self.duration, self.destination_airport)

        for attendant in self.attendants:
            attendant.flight_start(self.duration, self.destination_airport)

        self.base_airport.airport_maintenance()

        self.base_airport.availability_log.flight_start_snapshot(
            self, self.simulation_time)
        
        scheduler_instance = self.sol.get_scheduler_by_id(self.sol.id)
        scheduler_instance.schedule_event(self.duration, self.end_flight)

    def end_flight(self):
        self.status.append("completed")
        self.destination_airport.airport_maintenance()
        for pilot in self.pilots:
            pilot.start_rest(min(12, self.duration))
        for attendant in self.attendants:
            attendant.start_rest(min(12, self.duration))

    def cancel_flight(self, sol, reason):
        self.status.append("cancelled")

    def reset_state_after_mutation(self, sol):
        if self.status[-1] == "completed":
            # print(f"Resetting the state for flight: {self}")
            for pilot in self.pilots:
                pilot.reset_state_after_mutation(self)
            for attendant in self.attendants:
                attendant.reset_state_after_mutation(self)
            self.pilots = None
            self.attendants = None
        self.status.append("started")
        self.delay = 0