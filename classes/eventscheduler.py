import heapq
from event import Event

class EventScheduler:
    def __init__(self):
        # Initialize an empty priority queue
        self.events = []
        self.current_simulation_time = 0 

    def schedule_event(self, delay, function, *args):
        """Add an event to the queue."""
        event_time = self.current_simulation_time + delay
        event = Event(event_time, function, *args)
        heapq.heappush(self.events, event)

    def process_next_event(self):
        """Process the next event"""
        if self.events:  # if there are events to process
            next_event = heapq.heappop(self.events)  # Get the event with the smallest time
            self.current_simulation_time = next_event.time
            next_event.function(*next_event.args)  # Call the event's function with its arguments

    def has_events(self):
        """Check if there are more events to process."""
        return bool(self.events)

    def peek_next_event_time(self):
        """Return the time of the next event without processing it."""
        if self.events:
            return self.events[0].time
        return None

    def run_until_no_events(self):
        """Run until all events are processed."""
        while self.has_events():
            self.process_next_event()
