'''
For consideration:
- airtworthiness check - regular inspections etc
- enough fuel to reach the airport, alternate airport
plus an additional buffer.
'''


class Plane:
    _next_id = 1

    def __init__(self, capacity, pilots_needed, attendants_needed, speed, base):
        self.id = Plane._next_id
        Plane._next_id += 1
        self.ready = True
        self.capacity = capacity 
        self.pilots_needed = pilots_needed
        self.attendants_needed = attendants_needed
        self.speed = int(speed)
        self.base = base

    def __repr__(self):
        return f"Plane ID: {self.id}, capacity: {self.capacity}, speed: {self.speed}, base: {self.base}"

    def flight_start(self, destination):
        self.base.remove_plane(self)
        destination.add_plane(self)
        self.base = destination

    def __str__(self):
        return self.__repr__()