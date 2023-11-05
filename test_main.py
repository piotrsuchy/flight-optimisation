from src.structures import Structures
from src.schedule import Schedule

def main():
    initial_structures = Structures()
    schedule = Schedule()
    schedule.create_random_schedule(airports=initial_structures.airports, flights_q=30, simulation_length=720)
    print(schedule)
    
    
main()