import random
from src.allowed_approach.solution import Solution
from src.allowed_approach.classes.availability import AvailabilityLog

MAINTENANCE_TIME = 0


class Airport:
    _next_id = 1
    distance_matrix = []

    def __init__(self, x=None, y=None):
        self.x = x if x is not None else random.randint(0, 10000)
        self.y = y if y is not None else random.randint(0, 10000)
        self.id = Airport._next_id
        Airport._next_id += 1
        self.availability_log = AvailabilityLog(self)
        self.free = True
        self.pilots = []
        self.attendants = []
        self.sol_id = None
        self.occupied = False

    def __repr__(self):
        return f"Airport ID: {self.id}, X: {self.x}, Y: {self.y}"

    def __str__(self):
        return self.__repr__()

    @classmethod
    def set_distance_matrix(cls, matrix):
        cls.distance_matrix = matrix

    def get_distance_to(self, other_airport_id):
        return self.distance_matrix[self.id - 1][other_airport_id - 1]
        
    def test_equal(self, other):
        if self.x != other.x or self.y != other.y or self.id != other.id:
            return False
        for self_pilot, other_pilot in zip(self.pilots, other.pilots):
            if self_pilot != other_pilot:
                return False
        for self_attendant, other_attendant in zip(self.attendants, other.attendants):
            if self_attendant != other_attendant:
                return False
        return True

    def set_sol_id(self, sol_id):
        self.sol_id = sol_id

    def show_fleet_and_crew(self):
        print(f"FOR AIRPORT ID: {self.id}:")
        print(f"---PILOTS:---")
        for pilot in self.pilots:
            print(pilot)
        print(f"---ATTENDANTS:---")
        for attendant in self.attendants:
            print(attendant)

    def get_eligible_pilots(self, duration):
        return [pilot for pilot in self.pilots if pilot.is_eligible(duration)]

    def get_eligible_attendants(self, duration):
        return [attendant for attendant in self.attendants if attendant.is_eligible(duration)]

    def release(self):
        self.occupied = False

    def airport_maintenance(self):
        self.occupied = True
        scheduler_instance = Solution.get_scheduler_by_id(self.sol_id)
        scheduler_instance.schedule_event(MAINTENANCE_TIME, self.release)

    def add_pilot(self, pilot):
        self.pilots.append(pilot)

    def add_attendant(self, attendant):
        self.attendants.append(attendant)

    def remove_pilot(self, pilot):
        try:
            self.pilots.remove(pilot)
        except KeyError:
            print(f"Error in function remove_pilot() for airport {self.id}")

    def remove_attendant(self, attendant):
        try:
            self.attendants.remove(attendant)
        except ValueError:
            print(
                f"Error in function remove_attendant() for airport {self.id}")
        
    def check_consistency(self):
        for pilot in self.pilots:
            if pilot.current_base.id != self.id:
                print(f"Inconsistency found: Pilot {pilot.id} curr_base {pilot.current_base.id} doesn't match Airport {self.id}")
            
        for attendant in self.attendants:
            if attendant.current_base.id != self.id:
                print(f"Inconsistency found: Attendant {attendant.id} curr_base {attendant.current_base.id} doesn't match Airport {self.id}")
            
