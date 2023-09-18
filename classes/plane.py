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
        _next_id += 1
        self.capacity = capacity 
        self.pilots_needed = pilots_needed
        self.speed = speed