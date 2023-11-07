'''
For consideration:
days off,
rest periods,
flight duty period - pre-flight, post-flight etc.
on-duty, on-call - how to calculate this work hours
'''
from src.solution import Solution

MAX_DAILY_HOURS = 14
MAX_WEEKLY_HOURS = 60
MAX_MONTHLY_HOURS = 190


class Pilot:
    _next_id = 1

    def __init__(self, base):
        self.id = Pilot._next_id
        Pilot._next_id += 1
        self.base = base
        self.current_base = base
        self.day_worked_hs = 0
        self.week_worked_hs = 0
        self.month_worked_hs = 0
        self.flights_taken = 0
        self.is_available = True
        self.sol_id = None

    def __repr__(self):
        return f"Pilot ID: {self.id}, sol_id: {self.sol_id}, BASE: {self.current_base.id} from BASE: {self.base.id}, worked hs: {self.week_worked_hs}, flights taken: {self.flights_taken}"

    def set_sol_id(self, sol_id):
        self.sol_id = sol_id

    def is_eligible(self):
        return (self.is_available and
                self.day_worked_hs <= MAX_DAILY_HOURS and
                self.week_worked_hs <= MAX_WEEKLY_HOURS and
                self.month_worked_hs <= MAX_MONTHLY_HOURS)

    def occupy(self):
        self.is_available = False

    def release(self):
        self.is_available = True

    def start_rest(self, hours):
        self.occupy()
        # Scheduling an event for the end of rest
        scheduler_instance = Solution.get_scheduler_by_id(self.sol_id)
        scheduler_instance.schedule_event(hours, self.release)
        simulation_time_after_rest = scheduler_instance.current_simulation_time + hours
        scheduler_instance.schedule_event(
            hours, self.current_base.availability_log.rest_end_snapshot, self, simulation_time_after_rest)

    def decrement_hours(self, time, duration):
        if time == "day":
            self.day_worked_hs -= duration
        elif time == "week":
            self.week_worked_hs -= duration
        else:
            self.month_worked_hs -= duration

    def flight_start(self, duration, destination):
        self.current_base.remove_pilot(self)
        destination.add_pilot(self)
        self.current_base = destination
        self.day_worked_hs += duration
        self.week_worked_hs += duration
        self.month_worked_hs += duration
        self.flights_taken += 1
        self.occupy()
        # after a day decrement working hours
        scheduler_instance = Solution.schedulers[self.sol_id]
        # print(f"Solution.get_schedulers: {Solution.schedulers}")
        # print(f"Scheduler instance of pilot {self.id} is {scheduler_instance}")
        scheduler_instance.schedule_event(
            24, self.decrement_hours, "day", duration)
        # after a week decrement working hours
        scheduler_instance.schedule_event(
            7*24, self.decrement_hours, "week", duration)
        # after a month decrement working hours
        # scheduler_instance.schedule_event(30*24, self.decrement_hours, "month", duration)


class FlightAttendant:
    _next_id = 1

    def __init__(self, base):
        self.id = FlightAttendant._next_id
        FlightAttendant._next_id += 1
        self.base = base
        self.current_base = base
        self.day_worked_hs = 0
        self.week_worked_hs = 0
        self.month_worked_hs = 0
        self.rest_period = 0
        self.flights_taken = 0
        self.is_available = True
        self.sol_id = None

    def __repr__(self):
        return f"Attendant ID: {self.id}, BASE: {self.current_base.id} from BASE: {self.base.id}, worked hs: {self.week_worked_hs}, flights taken: {self.flights_taken}, status: {self.is_available}"

    def set_sol_id(self, sol_id):
        self.sol_id = sol_id

    def is_eligible(self):
        return (self.is_available and
                self.day_worked_hs <= MAX_DAILY_HOURS and
                self.week_worked_hs <= MAX_WEEKLY_HOURS and
                self.month_worked_hs <= MAX_MONTHLY_HOURS)

    def occupy(self):
        self.is_available = False

    def release(self):
        self.is_available = True

    def start_rest(self, hours):
        self.occupy()
        # Scheduling an event for the end of rest
        scheduler_instance = Solution.get_scheduler_by_id(self.sol_id)
        scheduler_instance.schedule_event(hours, self.release)
        simulation_time_after_rest = scheduler_instance.current_simulation_time + hours
        scheduler_instance.schedule_event(
            hours, self.current_base.availability_log.rest_end_snapshot, self, simulation_time_after_rest)

    def decrement_hours(self, time, duration):
        if time == "day":
            self.day_worked_hs -= duration
        elif time == "week":
            self.week_worked_hs -= duration
        else:
            self.month_worked_hs -= duration

    def flight_start(self, duration, destination):
        self.current_base.remove_attendant(self)
        destination.add_attendant(self)
        self.current_base = destination
        self.day_worked_hs += duration
        self.week_worked_hs += duration
        self.month_worked_hs += duration
        self.flights_taken += 1
        self.occupy()
        # after a day decrement working hours
        scheduler_instance = Solution.get_scheduler_by_id(self.sol_id)
        scheduler_instance.schedule_event(
            24, self.decrement_hours, "day", duration)
        # after a week decrement working hours
        scheduler_instance.schedule_event(
            7*24, self.decrement_hours, "week", duration)
        # after a month decrement working hours
        # scheduler_instance.schedule_event(30*24, self.decrement_hours, "month", duration)
