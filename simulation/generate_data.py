import numpy as np
import pandas as pd
from scipy.spatial import distance


def generate_distance_matrix(airports_list):
    # Generate random coordinates for each airport on a 100x100 grid
    coordinates = np.random.randint(0, 100, (len(airports_list), 2))

    df_coordinates = pd.DataFrame(coordinates, columns=['X', 'Y'], index=airports_list)
    df_coordinates.to_csv('../data/airport_coordinates.csv')
    distance_matrix = distance.cdist(coordinates, coordinates, 'euclidean')
    np.fill_diagonal(distance_matrix, 0)

    df_distance = pd.DataFrame(distance_matrix, columns=airports_list, index=airports_list)
    df_distance.to_csv('../data/distance_matrix.csv')

def generate_fleet(airports_list):
    airplane_names = [f'Plane_{i}' for i in range(50)]
    df_fleet = pd.DataFrame(columns=['Airport', 'Airplane', 'Airplane_Capacity'])
    fleet_size = np.random.randint(2, 10, len(airports_list))

    # Populate DataFrame for fleet information
    for i in range(len(airports_list)):
        airport = airports_list[i]
        fleet_at_airport = np.random.choice(airplane_names, fleet_size[i], replace=False)
        capacity_at_airport = np.random.randint(100, 300, len(fleet_at_airport))

        for j in range(len(fleet_at_airport)):
            df_fleet = df_fleet.append({
                'Airport': airport,
                'Airplane': fleet_at_airport[j],
                'Airplane_Capacity': capacity_at_airport[j]
            }, ignore_index=True)

    # Save DataFrame to CSV
    df_fleet.to_csv('fleet_information.csv')


def generate_crew(airports_list):
    # Crew information for each airport
    num_pilots = np.random.randint(4, 20, len(airports_list))
    num_stewardesses = np.random.randint(4, 20, len(airports_list))

    df_crew = pd.DataFrame({'Airport': airports_list, 'Pilots': num_pilots, 'Stewardesses': num_stewardesses})

    df_crew.to_csv('../data/crew_information.csv')

def generate_passengers_df(num_days, airports_list):
    # Generate a 30-day passenger demand between each pair of airports
    passenger_demand = np.random.randint(50, 300, (len(airports_list), len(airports_list), num_days))
    for day in range(num_days):
        np.fill_diagonal(passenger_demand[:, :, day], 0)
    # Creating an empty DataFrame
    df_passenger_demand = pd.DataFrame(columns=['Departure', 'Arrival', 'Day', 'Passengers'])

    # Populate DataFrame from 3D NumPy array
    for i in range(passenger_demand.shape[0]):
        for j in range(passenger_demand.shape[1]):
            for k in range(passenger_demand.shape[2]):
                df_passenger_demand = df_passenger_demand._append({
                    'Departure': airports_list[i],
                    'Arrival': airports_list[j],
                    'Day': k,
                    'Passengers': passenger_demand[i, j, k]
                }, ignore_index=True)

    # Set multi-index
    df_passenger_demand.set_index(['Departure', 'Arrival', 'Day'], inplace=True)
    df_passenger_demand.to_csv('../data/passenger_demand_30_days.csv')


def main():
    num_airports = 10
    num_days = 30
    airport_names = [f'Airport_{i}' for i in range(num_airports)]