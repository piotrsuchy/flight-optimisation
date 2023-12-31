from .crew_member import Pilot


class Availability:
    '''
    Class that implements the logic needed for mutation and crossing etc.
    It takes a "snapshot" of an airport at event's start or end to later be able
    to check the availability of the resources when mutating / crossing
    Each instance of this class is tied to the airport and to the specific time in simulation
    '''

    def __init__(self, airport, simulation_time, available_pilots,
                 available_attendants):
        self.airport = airport
        self.airport_id = airport.id
        self.simulation_time = simulation_time
        self.pilots = set(available_pilots)
        self.attendants = set(available_attendants)

    def __str__(self):
        return f"airport_id: {self.airport_id}, pilots: {self.pilots}, attendants: {self.attendants}"

    def remove_flight(self, flight):
        if flight.status[-1] != "cancelled":

            for pilot in flight.pilots:
                if pilot in self.pilots:
                    self.pilots.remove(pilot)

            for attendant in flight.attendants:
                if attendant in self.attendants:
                    self.attendants.remove(attendant)

    def copy(self):
        copy_of_instance = Availability(
            self.airport, self.simulation_time, self.pilots, self.attendants)
        return copy_of_instance


class AvailabilityLog:
    '''
    Class that stores instances of Availability class for a given Airport.
    This acts as a log to keep track of the availability of resources at the airport over time.
    '''

    def __init__(self, airport):
        self.airport = airport
        self.log = []

    def __str__(self):
        return f"AvailabilityLog(airport_id={self.airport.id})"

    def add_snapshot(self, simulation_time):
        '''
        Adds a new snapshot of availability at the given simulation time by checking
        the availability of pilots, attendants at the airport
        '''
        available_pilots = self.airport.get_eligible_pilots(0)
        available_attendants = self.airport.get_eligible_attendants(0)
        availability = Availability(
            self.airport, simulation_time, available_pilots, available_attendants)
        self.log.append(availability)

    def flight_start_snapshot(self, flight, stimulation_time):
        '''
        Creates a new snapshot based on the last one and modifies it according to the flight parameters.
        '''
        # print("FLIGHT START SNAPSHOT CREATED")
        if not self.log:
            self.add_snapshot(flight.start_time)

        last_availability = self.log[-1]
        new_availability = last_availability.copy()
        new_availability.simulation_time = stimulation_time

        # print(f"Removing flight: {flight.id} for simulation_time: {stimulation_time} and new_availability has time: {new_availability.simulation_time}")
        new_availability.remove_flight(flight)

        self.log.append(new_availability)

    def rest_end_snapshot(self, person, simulation_time):
        '''
        Adds a new snapshot after a person's rest period ends.
        '''
        # print("REST END SNAPSHOT CREATED")
        last_availability = self.log[-1]
        new_availability = last_availability.copy()
        new_availability.simulation_time = simulation_time
        # print(f"New availability: {new_availability}")

        if isinstance(person, Pilot):
            new_availability.pilots.add(person)
        else:
            new_availability.attendants.add(person)
        # print(f"To compare with new availability after modifications: {new_availability}")

        self.log.append(new_availability)

    def get_availability(self, simulation_time):
        '''
        Returns the availability at the given simulation time.
        If there is no snapshot at exactly that time, it returns the most recent one before it.
        '''
        if not self.log:
            print(f"No availability snapshot available!")
            raise ValueError("No availability snapshot available!")

        # Sort the log based on simulation time:
        self.log.sort(key=lambda availability: availability.simulation_time)

        for availability in reversed(self.log):
            if availability.simulation_time <= simulation_time:
                return availability

        # if all snapshots in the future - return the first one
        return self.log[0]

    def clear_logs_after_timestamp(self, timestamp):
        try:
            self.log = [snapshot for snapshot in self.log if snapshot.simulation_time <= timestamp]
        except TypeError:
            print(f"type(snapshot.simulation_time): {type(self.log[0].simulation_time)} type(timestamp): {timestamp}")