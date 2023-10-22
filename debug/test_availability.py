from src.decorators import timing_decorator

@timing_decorator
def test_availability(evol_algo):
    print(f"Checking the availability_log object for airport 1:")
    sol_1 = evol_algo.population[0][0]
    first_airport = sol_1.structures.airports[0]
    availability_log = first_airport.availability_log

    simulation_times = [0, 100, 700]
    for sim_time in simulation_times:
        try:
            availability = availability_log.get_availability(sim_time)
            print(f"Availability at simulation time {sim_time}:")
            print(f"  Pilots: {len(availability.pilots)}")
            print(f"  Attendants: {len(availability.attendants)}")
            print(f"  Planes: {len(availability.planes)}")
        except ValueError as e:
            print(f"Error at simulation time {sim_time}: {e}")