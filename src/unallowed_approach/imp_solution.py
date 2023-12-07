import random
import json

with open('parameters.json') as parameters_file:
    config = json.load(parameters_file)

class ImpossibleSolution:
    def __init__(self):
        self.n_airports = config['structs']['N_AIRPORTS']
        self.n_flights = config['sim']['N_FLIGHTS']
        self.n_pilots_pplane = config['structs']['PILOTS_PER_PLANE']
        self.n_attend_pplane = config['structs']['ATTEND_PER_PLANE']
        self.sim_len = config['sim']['SIM_LEN']
        self.n_flight_fields = self.n_pilots_pplane + self.n_attend_pplane + 3
        self.schedule = [[None for _ in range(self.n_flight_fields)] for _ in range(self.n_flights)]

    def __str__(self):
        print("---Flights in solution: ---")
        for flight in self.schedule:
            print(flight)

    def get_initial_schedule(self):
        self.assign_source_and_dest_to_flight()
        self.assign_timestamp_to_flight()
        return self.schedule


    def assign_source_and_dest_to_flight(self):
        for flight in self.schedule:
            selected_airports = random.sample([i for i in range(1, self.n_airports + 1)], 2)
            flight[0] = selected_airports[0]
            flight[1] = selected_airports[1]
    
    def assign_timestamp_to_flight(self):
        for flight in self.schedule:
            flight[-1] = int(random.uniform(0, self.sim_len))
        
    def print_schedule(self):
        for flight in self.schedule:
            print(flight)

            
def test_main_1():
    sol = ImpossibleSolution()
    sol.assign_source_and_dest_to_flight()
    sol.assign_timestamp_to_flight()
    
test_main_1()