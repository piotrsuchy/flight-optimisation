class Event:
    def __init__(self, time, function, *args):
        self.time = time
        self.function = function
        self.args = args

    def __str__(self):
        return f"{self.function} at time: {self.time}"

    def __lt__(self, other):
        return self.time < other.time
