'''
For consideration:
days off,
rest periods,
flight duty period - pre-flight, post-flight etc.
'''
from .scheduler_singleton import scheduler_instance

class Pilot:
    _next_id = 1

    def __init__(self, base):
        self.id = Pilot._next_id
        Pilot._next_id += 1
        self.base = base 
        self.current_base = base
        self.day_worked_hs = 0
        self.week_worked_hs = 0
        self.month_worked_hs = 0
        self.flights_taken = 0
        self.is_available = True

    def __repr__(self):
        return f"Pilot ID: {self.id}, BASE: {self.current_base.id} from BASE: {self.base.id}, worked hs: {self.week_worked_hs}, flights taken: {self.flights_taken}"

    def is_free(self):
        return self.is_available

    def occupy(self):
        self.is_available = False

    def release(self):
        # print(f"Released at hour {scheduler_instance.current_simulation_time}")
        self.is_available = True

    def start_rest(self, hours):
        self.occupy()
        # Scheduling an event for the end of rest
        scheduler_instance.schedule_event(hours, self.release)
    
    def flight_start(self, duration, destination):
        self.current_base.remove_pilot(self)
        destination.add_pilot(self)
        self.current_base = destination
        self.day_worked_hs += duration
        self.week_worked_hs += duration
        self.month_worked_hs += duration
        self.flights_taken += 1

class FlightAttendant:
    _next_id = 1
    
    def __init__(self, base):
        self.id = FlightAttendant._next_id
        FlightAttendant._next_id += 1
        self.base = base
        self.current_base = base
        self.day_worked_hs = 0
        self.week_worked_hs = 0
        self.month_worked_hs = 0
        self.rest_period = 0
        self.flights_taken = 0
        self.is_available = True

    def __repr__(self):
        return f"Attendant ID: {self.id}, BASE: {self.current_base.id} from BASE: {self.base.id}, worked hs: {self.week_worked_hs}, flights taken: {self.flights_taken}, status: {self.is_available}"

    def is_free(self):
        return self.is_available

    def occupy(self):
        self.is_available = False

    def release(self):
        # print(f"Released at hour {scheduler_instance.current_simulation_time}")
        self.is_available = True

    def start_rest(self, hours):
        self.occupy()
        # Scheduling an event for the end of rest
        scheduler_instance.schedule_event(hours, self.release)

    def flight_start(self, duration, destination):
        self.current_base.remove_attendant(self)
        destination.add_attendant(self)
        self.current_base = destination
        self.day_worked_hs += duration
        self.week_worked_hs += duration
        self.month_worked_hs += duration
        self.flights_taken += 1
