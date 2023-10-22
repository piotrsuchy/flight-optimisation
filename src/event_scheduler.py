import heapq
from .event import Event


class EventScheduler():
    def __init__(self):
        # Initialize an empty priority queue
        self.events = []
        self.current_simulation_time = 0

    def schedule_event(self, delay, function, *args):
        """Add an event to the queue."""
        if function is None:
            print("Function is None!")
        event_time = self.current_simulation_time + delay
        event = Event(event_time, function, *args)
        heapq.heappush(self.events, event)

    def process_next_event(self):
        """Process the next event"""
        try:
            if self.events:  # if there are events to process
                # Get the event with the smallest time
                next_event = heapq.heappop(self.events)
                self.current_simulation_time = next_event.time
                # Call the event's function with its arguments
                next_event.function(*next_event.args)
        except TypeError:
            print(f"The function: {next_event.function} had a type error")

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
