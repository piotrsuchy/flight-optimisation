'''
For consideration:
- airtworthiness check - regular inspections etc
- enough fuel to reach the airport, alternate airport
plus an additional buffer.
'''
from .scheduler_singleton import scheduler_instance

MAINTENANCE_TIME = 2

class Plane:
    _next_id = 1

    def __init__(self, capacity, pilots_needed, attendants_needed, speed, base):
        self.id = Plane._next_id
        Plane._next_id += 1
        self.base = base
        self.capacity = capacity 
        self.pilots_needed = pilots_needed
        self.attendants_needed = attendants_needed
        self.speed = int(speed)
        self.is_available = True

    def __repr__(self):
        return f"Plane ID: {self.id}, capacity: {self.capacity}, speed: {self.speed}, base: {self.base}"

    def __str__(self):
        return self.__repr__()

    def flight_start(self, destination):
        self.base.remove_plane(self)
        destination.add_plane(self)
        self.base = destination
        self.occupy()
    
    def is_available(self):
        return self.is_available

    def occupy(self):
        self.is_available = False
        scheduler_instance.schedule_event(MAINTENANCE_TIME, self.release)

    def release(self):
        self.is_available = True