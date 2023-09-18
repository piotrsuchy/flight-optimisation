import random
from classes.airport import Airport
from classes.crew_member import Pilot, FlightAttendant
from classes.flight import Flight
from classes.plane import Plane
from classes.eventscheduler import EventScheduler

# Initialize the EventScheduler
scheduler = EventScheduler()

# Create 5 airports at random locations
airports = []
for i in range(5):
    airport = Airport()
    airport.x = random.randint(0, 100)
    airport.y = random.randint(0, 100)
    airport.id = i + 1
    airports.append(airport)

# Create 10 planes
planes = []
for i in range(10):
    capacity = random.randint(50, 200)  # Random capacity between 50 and 200
    pilots_needed = 2  # Assuming each plane needs 2 pilots
    speed = random.uniform(500, 800)  # Speed between 500 to 800 km/h
    planes.append(Plane(capacity, pilots_needed, speed))

# Create 10 pilots and 10 flight attendants
pilots = [Pilot(random.choice(airports)) for _ in range(10)]
attendants = [FlightAttendant(random.choice(airports)) for _ in range(10)]

# Schedule 10 flights
for i in range(10):
    base = random.choice(airports)
    destination = random.choice(airports)
    while base == destination:  # Make sure we don't pick the same airport
        destination = random.choice(airports)
    
    plane = random.choice(planes)
    pilot_list = random.sample(pilots, plane.pilots_needed)
    attendant_list = random.sample(attendants, 2)  # Assuming 2 attendants per flight
    
    flight = Flight(base, destination, plane, pilot_list, attendant_list)
    
    # Start the flight after a random delay
    delay = random.uniform(0.1, 1)  # Delay between 0.1 to 1 hour
    scheduler.schedule_event(delay, flight.start_flight)

# Run the simulation until all events are processed
scheduler.run_until_no_events()

print("Simulation completed!")
