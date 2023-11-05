'''
for consideration:
- airtworthiness check - regular inspections etc
- enough fuel to reach the airport, alternate airport
plus an additional buffer.
'''
from src.solution import solution

maintenance_time = 1


class plane:
    _next_id = 1

    def __init__(self, capacity, pilots_needed, attendants_needed, speed, base, sol_id=none):
        self.id = plane._next_id
        plane._next_id += 1
        self.base = base
        self.capacity = capacity
        self.pilots_needed = pilots_needed
        self.attendants_needed = attendants_needed
        self.speed = int(speed)
        self.is_available = true
        self.sol_id = sol_id

    def __repr__(self):
        return f"plane id: {self.id}, capacity: {self.capacity}, speed: {self.speed}, base: {self.base}"

    def __str__(self):
        return self.__repr__()

    def set_sol_id(self, sol_id):
        self.sol_id = sol_id

    def flight_start(self, destination):
        self.occupy()
        self.base.remove_plane(self)
        destination.add_plane(self)
        self.base = destination

    def occupy(self):
        self.is_available = false

    def release(self):
        self.is_available = true

    def maintenance(self):
        self.occupy()
        scheduler_instance = solution.get_scheduler_by_id(self.sol_id)
        scheduler_instance.schedule_event(maintenance_time, self.release)
        simulation_time = scheduler_instance.current_simulation_time + maintenance_time
        scheduler_instance.schedule_event(
            maintenance_time, self.base.availability_log.plane_maintenance_snapshot, self, simulation_time)
