'''
For consideration:
days off,
rest periods,
flight duty period - pre-flight, post-flight etc.
'''
from .eventscheduler import EventScheduler

class Pilot:
    _next_id = 1

    def __init__(self, base):
        self.id = Pilot._next_id
        Pilot._next_id += 1
        self.is_available = True
        self.base = base 
        self.current_base = base
        self.day_worked_hs = 0
        self.week_worked_hs = 0
        self.month_worked_hs = 0

    def __repr__(self):
        return f"Pilot ID: {self.id}, BASE: {self.current_base.id}, worked hs: {self.week_worked_hs}"

    def is_free(self):
        return self.is_available

    def occupy(self):
        self.is_available = False

    def release(self):
        self.is_available = True

    def start_rest(self, hours):
        self.occupy()
        # Scheduling an event for the end of rest
        EventScheduler.schedule_event(hours, self.release)
    
    def flight_start(self, duration, destination):
        self.current_base = destination
        self.day_worked_hs += duration
        self.week_worked_hs += duration
        self.month_worked_hs += duration

class FlightAttendant:
    _next_id = 1
    
    def __init__(self, base):
        self.id = FlightAttendant._next_id
        FlightAttendant._next_id += 1
        self.is_available = True
        self.base = base
        self.current_base = base
        self.day_worked_hs = 0
        self.week_worked_hs = 0
        self.month_worked_hs = 0
        self.rest_period = 0

    def __repr__(self):
        return f"Attendant ID: {self.id}, BASE: {self.current_base.id}, worked hs: {self.week_worked_hs}"

    def is_free(self):
        return self.is_available

    def occupy(self):
        self.is_available = False

    def release(self):
        self.is_available = True

    def start_rest(self, hours):
        self.occupy()
        # Scheduling an event for the end of rest
        EventScheduler.schedule_event(hours, self.release)

    def flight_start(self, duration, destination):
        self.current_base = destination
        self.day_worked_hs += duration
        self.week_worked_hs += duration
        self.month_worked_hs += duration
