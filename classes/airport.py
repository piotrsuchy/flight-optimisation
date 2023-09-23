'''
For consideration:
- slot restrictions - restrictions on the
number of take offs and landings the airport
can handle in any given time frame due to capacity
'''

MAINTENANCE_TIME = 1

class Airport:
    def __init__(self):
        self.x = None
        self.y = None
        self.id = None
        self.occupied = False

    def __repr__(self):
        return f"Airport ID: {self.id}, X: {self.x}, Y: {self.y}"

    def __str__(self):
        return self.__repr__()

    def release(self):
        self.occupied = False

    def airport_maintenance(self, event_scheduler):
        self.occupied = True
        event_scheduler.schedule_event(MAINTENANCE_TIME, self.release)