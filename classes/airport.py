'''
For consideration:
- slot restrictions - restrictions on the
number of take offs and landings the airport
can handle in any given time frame due to capacity
'''
import random

MAINTENANCE_TIME = 1

class Airport:
    _next_id = 1

    def __init__(self, x=None, y=None):
        self.x = x if x is not None else random.randint(0, 10000)
        self.y = y if y is not None else random.randint(0, 10000)
        self.id = Airport._next_id
        Airport._next_id += 1
        self.occupied = False
        self.planes = []
        self.pilots = []
        self.attendants = []

    def __repr__(self):
        return f"Airport ID: {self.id}, X: {self.x}, Y: {self.y}"

    def __str__(self):
        return self.__repr__()

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

    def airport_maintenance(self, event_scheduler):
        self.occupied = True
        event_scheduler.schedule_event(MAINTENANCE_TIME, self.release)

    def add_plane(self, plane):
        self.planes.append(plane)

    def add_pilot(self, pilot):
        self.pilots.append(pilot)

    def add_attendant(self, attendant):
        self.attendants.append(attendant)

    def remove_plane(self, plane):
        self.planes.remove(plane)

    def remove_pilot(self, pilot):
        self.pilots.remove(pilot)

    def remove_attendant(self, attendant):
        self.attendants.remove(attendant)