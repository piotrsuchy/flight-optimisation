'''
For consideration:
- slot restrictions - restrictions on the
number of take offs and landings the airport
can handle in any given time frame due to capacity
'''
from eventscheduler import EventScheduler

MAINTENANCE_TIME = 1

class Airport:
    def __init__(self):
        self.x = None
        self.y = None
        self.id = None
        self.occupied = False

    def release(self):
        self.occupied = False

    def airport_maintenance(self):
        self.occupied = True
        EventScheduler(MAINTENANCE_TIME, self.release)