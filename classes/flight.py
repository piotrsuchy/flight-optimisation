import math
import logging

class Flight:
    _next_id = 1

    def __init__(self, base_airport, destination_airport, plane, pilot, crew):
        self.id = Flight._next_id
        Flight._next_id += 1
        self.base_airport = base_airport
        self.destination_airport = destination_airport
        self.plane = plane
        self.pilots = pilot
        self.crew = crew
        self.distance = self.calculate_distance()
        self.duration = self.calculate_duration()
        self.status = "started"

    def calculate_distance(self):
        return math.sqrt((self.base_airport.x - self.destination_airport.x)**2 +
                         (self.base_airport.y - self.destination_airport.y)**2)

    def calculate_duration(self):
        return self.distance / self.plane.speed

    def start_flight(self, event_scheduler):
        logging.info(f"At hour {event_scheduler.current_simulation_time:.2f}: Flight from {self.base_airport} to {self.destination_airport} has started! Duration: {self.duration:.2f}")

        if not all(pilot.is_available for pilot in self.pilots) or not all(attendant.is_available for attendant in self.crew):
            print("Not all crew members or pilots are available!")
            return

        for pilot in self.pilots:
            pilot.flight_start(self.duration, self.destination_airport)
            pilot.occupy()
        
        for attendant in self.crew:
            attendant.flight_start(self.duration, self.destination_airport)
            attendant.occupy()

        self.plane.flight_start(self.destination_airport)

        self.base_airport.airport_maintenance(event_scheduler)

    def end_flight(self):
        self.status = "completed"

        for pilot in self.pilots:
            pilot.start_rest(min(12, self.duration))

        for attendant in self.crew:
            attendant.start_rest(min(12, self.duration))

        self.destination_airport.airport_maintenance()