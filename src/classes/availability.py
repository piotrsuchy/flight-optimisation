from .crew_member import Pilot


class Availability:
    '''
    Class that implements the logic needed for mutation and crossing etc.
    It takes a "snapshot" of an airport at event's start or end to later be able
    to check the availability of the resources when mutating / crossing
    Each instance of this class is tied to the airport and to the specific time in simulation
    '''
    def __init__(self, airport, simulation_time, available_pilots, available_attendants, available_planes):
        self.airport = airport
        self.airport_id = airport.id
        self.simulation_time = simulation_time
        self.pilots = set(available_pilots)
        self.attendants = set(available_attendants)
        self.planes = set(available_planes)

    def remove_flight(self, flight):
        for pilot in flight.pilots:
            self.pilots.remove(pilot)
        for attendant in flight.attendants:
            self.attendants.remove(attendant)
        self.planes.remove(flight.plane)

    def copy(self):
        copy_of_instance = Availability(self.airport, self.simulation_time, self.pilots, self.attendants, self.planes)
        return copy_of_instance

class AvailabilityLog:
    '''
    Class that stores instances of Availability class for a given Airport.
    This acts as a log to keep track of the availability of resources at the airport over time.
    '''
    def __init__(self, airport):
        self.airport = airport
        self.log = []

    def add_snapshot(self, simulation_time):
        '''
        Adds a new snapshot of availability at the given simulation time by checking
        the availability of pilots, attendants and planes at the airport
        '''
        available_pilots = self.airport.get_eligible_pilots()
        available_attendants = self.airport.get_eligible_attendants()
        available_planes = self.airport.get_available_planes()
        availability = Availability(self.airport, simulation_time, available_pilots, available_attendants, available_planes)
        self.log.append(availability)

    def flight_start_snapshot(self, flight, stimulation_time):
        '''
        Creates a new snapshot based on the last one and modifies it according to the flight parameters.
        '''
        if not self.log:
            self.add_snapshot(flight.start_time) 

        last_availability = self.log[-1]
        new_availability = last_availability.copy()
        new_availability.simulation_time = stimulation_time

        new_availability.remove_flight(flight)

        self.log.append(new_availability)

    def rest_end_snapshot(self, person, simulation_time):
        '''
        Adds a new snapshot after a person's rest period ends.
        '''
        last_availability = self.log[-1]
        new_availability = last_availability.copy()
        new_availability.simulation_time = simulation_time

        if isinstance(person, Pilot):
            new_availability.pilots.add(person)
        else:
            new_availability.attendants.add(person)

        self.log.append(new_availability)

    def plane_maintenance_snapshot(self, plane, simulation_time):
        '''
        Adds a new snapshot after plane maintenance period ends.
        '''
        last_availability = self.log[-1]
        new_availability = last_availability.copy()
        new_availability.simulation_time = simulation_time

        new_availability.planes.add(plane)
        self.log.append(new_availability)
        
    def get_availability(self, simulation_time):
        '''
        Returns the availability at the given simulation time. 
        If there is no snapshot at exactly that time, it returns the most recent one before it.
        '''
        if not self.log:
            raise ValueError("No availability snapshot available!")
        
        # Sort the log based on simulation time:
        self.log.sort(key=lambda availability: availability.simulation_time)

        for availability in reversed(self.log):
            if availability.simulation_time <= simulation_time:
                return availability

        # if all snapshots in the future - return the first one
        return self.log[0]

    def __str__(self):
        return f"AvailabilityLog(airport_id={self.airport.id})"