'''
For consideration:
- slot restrictions - restrictions on the
number of take offs and landings the airport
can handle in any given time frame due to capacity
'''
import random
from .scheduler_singleton import scheduler_instance

MAINTENANCE_TIME = 0.5

class Airport:
    _next_id = 1

    def __init__(self, x=None, y=None):
        self.x = x if x is not None else random.randint(0, 10000)
        self.y = y if y is not None else random.randint(0, 10000)
        self.id = Airport._next_id
        Airport._next_id += 1
        self.free = True
        self.planes = []
        self.pilots = []
        self.attendants = []

    def __repr__(self):
        return f"Airport ID: {self.id}, X: {self.x}, Y: {self.y}"

    def __str__(self):
        return self.__repr__()

    def is_available(self):
        return self.occupied

    def show_fleet_and_crew(self):
        print(f"FOR AIRPORT ID: {self.id}:")
        print(f"---PLANES:---")
        for plane in self.planes:
            print(plane)
        print(f"---PILOTS:---")
        for pilot in self.pilots:
            print(pilot)
        print(f"---ATTENDANTS:---")
        for attendant in self.attendants:
            print(attendant)

    def release(self):
        self.occupied = False

    def airport_maintenance(self):
        self.occupied = True
        scheduler_instance.schedule_event(MAINTENANCE_TIME, self.release)

    def add_plane(self, plane):
        self.planes.append(plane)

    def add_pilot(self, pilot):
        # print(f"Added pilot {pilot.id}, to the base {self.id}")
        self.pilots.append(pilot)

    def add_attendant(self, attendant):
        # print(f"Added attendant {attendant.id}, to the base {self.id}")
        self.attendants.append(attendant)

    def remove_plane(self, plane):
        try:
            self.planes.remove(plane)
        except KeyError:
            print(f"Error in function remove_plane() for airport {self.id}")

    def remove_pilot(self, pilot):
        try:
            self.pilots.remove(pilot)
        except KeyError:
            print(f"Error in function remove_pilot() for airport {self.id}")

    def remove_attendant(self, attendant):
        try:
            self.attendants.remove(attendant)
        except ValueError:
            print(f"Error in function remove_attendant() for airport {self.id}")