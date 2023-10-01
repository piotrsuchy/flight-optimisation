import numpy as np
from scipy.spatial import distance


class DataGeneration:
    def __init__(
        self,
        num_of_airports=10,
        min_fleet=3,
        max_fleet=25,
        min_pilots=3,
        max_pilots=40,
        min_steward=10,
        max_steward=80,
        min_demand=20,
        max_demand=1000,
        min_capacity=20,
        max_capacity=300,
        sim_length=120,
    ):
        self.num_of_airports = num_of_airports
        self.min_fleet = min_fleet
        self.max_fleet = max_fleet
        self.min_pilots = min_pilots
        self.max_pilots = max_pilots
        self.min_steward = min_steward
        self.max_steward = max_steward
        self.min_demand = min_demand
        self.max_demand = max_demand
        self.min_capacity = min_capacity
        self.max_capacity = max_capacity
        self.sim_length = sim_length

        self.airports_list = []
        self.airport_coordinates = {}
        self.distance_matrix = {}
        self.fleet_information = {}
        self.crew_information = {}
        self.passenger_demand = {}

    def generate_data(self):
        self._create_airports_list()
        self._generate_distance_matrix()
        self._generate_crew()
        self._generate_fleet()
        self._generate_passengers_demand()

    def _create_airports_list(self):
        self.airports_list = [f"Airport_{i}" for i in range(self.num_of_airports)]

    def _generate_distance_matrix(self):
        # Generate random coordinates for each airport on a 100x100 grid
        coordinates = np.random.randint(0, 100, (len(self.airports_list), 2))
        self.airport_coordinates = {
            self.airports_list[i]: coordinates[i] for i in range(self.num_of_airports)
        }

        distance_matrix = distance.cdist(coordinates, coordinates, "euclidean")
        np.fill_diagonal(distance_matrix, 0)
        self.distance_matrix = {
            (self.airports_list[i], self.airports_list[j]): distance_matrix[i][j]
            for i in range(self.num_of_airports)
            for j in range(self.num_of_airports)
        }

    def _generate_fleet(self):
        airplane_names = [f"Plane_{i}" for i in range(50)]
        fleet_size = np.random.randint(
            self.min_fleet, self.max_fleet, len(self.airports_list)
        )

        # Populate fleet information
        for i in range(len(self.airports_list)):
            airport = self.airports_list[i]
            fleet_at_airport = np.random.choice(
                airplane_names, fleet_size[i], replace=False
            )
            airplane_capacity = np.random.randint(
                self.min_capacity, self.max_capacity, len(fleet_at_airport)
            )

            self.fleet_information[airport] = [
                {
                    "Airplane": fleet_at_airport[j],
                    "Airplane_Capacity": airplane_capacity[j],
                }
                for j in range(len(fleet_at_airport))
            ]

    def _generate_crew(self):
        # Crew information for each airport
        num_pilots = np.random.randint(
            self.min_pilots, self.max_pilots, self.num_of_airports
        )
        num_stewardesses = np.random.randint(
            self.min_steward, self.max_steward, self.num_of_airports
        )

        for i in range(self.num_of_airports):
            self.crew_information[self.airports_list[i]] = {
                "Pilots": num_pilots[i],
                "Stewardesses": num_stewardesses[i],
            }

    def _generate_passengers_demand(self):
        # Generate a 30-day passenger demand between each pair of airports
        passenger_demand = np.random.randint(
            self.min_demand,
            self.max_demand,
            (self.num_of_airports, self.num_of_airports, self.sim_length),
        )

        for day in range(self.sim_length):
            np.fill_diagonal(passenger_demand[:, :, day], 0)

        for i in range(passenger_demand.shape[0]):
            for j in range(passenger_demand.shape[1]):
                for k in range(passenger_demand.shape[2]):
                    self.passenger_demand[
                        (self.airports_list[i], self.airports_list[j], k)
                    ] = passenger_demand[i, j, k]
