import math

class Flight:
    _next_id = 1

    def __init__(self, base_airport, destination_airport, plane):
        self.id = Flight._next_id
        Flight._next_id += 1
        self.base_airport = base_airport
        self.destination_airport = destination_airport
        self.plane = plane
        self.distance = self.calculate_distance()
        self.duration = self.calculate_duration()

    def calculate_distance(self):
        return math.sqrt((self.base_airport.x - self.destination_airport.x)**2 +
                         (self.base_airport.y - self.destination_airport.y)**2)

    def calculate_duration(self):
        return self.distance / self.plane.speed