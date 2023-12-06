import heapq
from .event import Event


class EventScheduler():
    def __init__(self, events=None):
        # Initialize an empty priority queue
        if events is None:
            self.events = []
        else:
            self.events = events
        self.current_simulation_time = 0

    def get_events(self):
        return self.events

    def schedule_event(self, delay, function, *args):
        """Add an event to the queue."""
        if function is None:
            print("Function is None!")
        event_time = self.current_simulation_time + delay
        # print(f"Scheduling for time: {event_time}")
        event = Event(event_time, function, *args)
        heapq.heappush(self.events, event)

    def process_next_event(self):
        """Process the next event"""
        try:
            if self.has_events:  # if there are events to process
                # Get the event with the smallest time
                next_event = heapq.heappop(self.events)
                # print(f"Processing event: {next_event}")
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

    def peek_all_events(self):
        for event in self.events:
            print(event)

    def run_until_no_events(self):
        """Run until all events are processed."""
        while self.has_events():
            self.process_next_event()

    def set_time(self, time):
        self.current_simulation_time = time
