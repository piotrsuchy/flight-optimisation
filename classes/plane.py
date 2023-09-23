'''
For consideration:
- airtworthiness check - regular inspections etc
- enough fuel to reach the airport, alternate airport
plus an additional buffer.
'''


class Plane:
    _next_id = 1

    def __init__(self, capacity, pilots_needed, speed):
        self.id = Plane._next_id
        Plane._next_id += 1
        self.capacity = capacity 
        self.pilots_needed = pilots_needed
        self.speed = int(speed)

    def __repr__(self):
        return f"Plane ID: {self.id}, capacity: {self.capacity}, speed: {self.speed}"

    def __str__(self):
        return self.__repr__()