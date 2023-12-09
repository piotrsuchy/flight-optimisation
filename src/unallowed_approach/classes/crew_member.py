import random

class Pilot:
    _next_id = 1

    def __init__(self) -> None:
        self.id = Pilot._next_id
        Pilot._next_id += 1
        self.training_day = int(random.uniform(1, self.sim_len // 24))


class FlightAttendant:
    _next_id = 1

    def __init__(self) -> None:
        self.id = FlightAttendant._next_id
        FlightAttendant._next_id += 1
        self.training_day = int(random.uniform(1, self.sim_len // 24))