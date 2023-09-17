import heapq
from event import Event

class Simulation:
    def __init__(self):
        self.current_time = 0
        self.event_queue = []

    def scheule_event(self, delay, function, *args):
        event_time = self.current_time + delay
        event = Event(event_time, function, *args)
        heapq.heappush(self.event_queue, event)

    def run(self):
        while self.event_queue:
            event = heapq.heappop(self.event_queue)
            self.current_time = event.time
            event.function(*event.args)