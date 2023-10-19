class Availability:
    '''
    Class that implements the logic needed for mutation and crossing etc.
    It takes a "snapshot" of an airport at event's start or end to later be able
    to check the availability of the resources when mutating / crossing
    Each instance of this class is tied to the airport and to the specific time in simulation
    '''
    def __init__(self, airport, simulation_time, available_pilots, available_attendants, available_planes):
        self.airport_id = airport.id
        self.simulation_time = simulation_time
        self.pilots = available_pilots
        self.attendants = available_attendants
        self.planes = available_planes

    def add_flight(self, flight):
        self.pilots -= {pilot for pilot in flight.pilots if pilot.is_available}
        self.attendants -= {attendant for attendant in flight.attendants if attendant.is_available}
        self.planes -= {plane for plane in [flight.plane] if plane.is_available}

    def remove_flight(self, flight):
        self.pilots |= {pilot for pilot in flight.pilots if pilot.is_available}
        self.attendants |= {attendant for attendant in flight.attendants if attendant.is_available}
        self.planes |= {plane for plane in [flight.plane] if plane.is_available}
