'''
for consideration:
- airtworthiness check - regular inspections etc
- enough fuel to reach the airport, alternate airport
plus an additional buffer.
'''
from src.solution import Solution

maintenance_time = 1


class Plane:
    _next_id = 1

    def __init__(self, capacity, pilots_needed,
                 attendants_needed, speed, base, sol_id=None):
        self.id = Plane._next_id
        Plane._next_id += 1
        self.base = base
        self.capacity = capacity
        self.pilots_needed = pilots_needed
        self.attendants_needed = attendants_needed
        self.speed = int(speed)
        self.is_available = True
        self.sol_id = sol_id
        self.flights_statuses = []

    def __repr__(self):
        return f"Plane ID: {self.id}, base: {self.base.id}"

    def __str__(self):
        return self.__repr__()

    def set_sol_id(self, sol_id):
        self.sol_id = sol_id

    def flight_start(self, destination, flight_status):
        self.occupy()
        self.base.remove_plane(self)
        destination.add_plane(self)
        self.flights_statuses.append(flight_status)
        self.base = destination

    def occupy(self):
        self.is_available = False

    def release(self):
        self.is_available = True

    def maintenance(self):
        self.occupy()
        scheduler_instance = Solution.get_scheduler_by_id(self.sol_id)
        scheduler_instance.schedule_event(maintenance_time, self.release)
        simulation_time = scheduler_instance.current_simulation_time + maintenance_time
        scheduler_instance.schedule_event(
            maintenance_time, self.base.availability_log.plane_maintenance_snapshot, self, simulation_time)

    def reset_state_after_mutation(self, flight):
        flight.destination_airport.remove_plane(self)
        flight.base_airport.add_plane(self)
        self.release()
        self.base = flight.base_airport