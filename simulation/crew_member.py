'''
For consideration:
days off,
rest periods,
flight duty period - pre-flight, post-flight etc.
'''

class Pilot:
    _next_id = 1

    def __init__(self):
        self.id = Pilot._next_id
        Pilot._next_id += 1
        self.home_airport = None
        self.day_worked_hs = None
        self.week_worked_hs = None
        self.month_worked_hs = None
        self.rest_period = None


class FlightAttendant:
    _next_id = 1
    
    def __init__(self):
        self.id = FlightAttendant._next_id
        FlightAttendant._next_id += 1
        self.home_airport = None
        self.day_worked_hs = None
        self.week_worked_hs = None
        self.month_worked_hs = None
        self.rest_period = None