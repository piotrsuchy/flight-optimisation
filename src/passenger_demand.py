import random
import numpy as np
# import seaborn as sns
import matplotlib.pyplot as plt


def generate_demand_array(airports, days=30):
    num_airports = len(airports)
    # Creating a 3D array with dimensions [num_airports][num_airports][days]
    demand_array = np.zeros((num_airports, num_airports, days), dtype=int)

    for day in range(days):
        for from_index, from_airport in enumerate(airports):
            for to_index, to_airport in enumerate(airports):
                if from_airport != to_airport:
                    demand_quantity = random.randint(100, 1000)
                    demand_array[from_index][to_index][day] = demand_quantity

    return demand_array


def visualize_demand(demand_array, airports):
    airport_ids = [airport.id for airport in airports]

    # Sum over the days to get the total demand between each airport pair
    # sum over the third dimension (days)
    summarized_demand = np.sum(demand_array, axis=2)

    sns.heatmap(summarized_demand, xticklabels=airport_ids,
                yticklabels=airport_ids, annot=True, cmap='YlGnBu')
    plt.xlabel('To Airport')
    plt.ylabel('From Airport')
    plt.title('Summarized Passenger Demand Heatmap')
    plt.show()


def visualize_demand_for_day(demand_array, airports, day):
    if day >= demand_array.shape[2]:
        raise ValueError(f"Invalid day specified. The demand")
    airport_ids = [airport.id for airport in airports]

    # choose just the specific day
    day_demand = demand_array[:, :, day]

    sns.heatmap(day_demand, xticklabels=airport_ids,
                yticklabels=airport_ids, annot=True, cmap='YlGnBu')
    plt.xlabel('To Airport')
    plt.ylabel('From Airport')
    plt.title('Summarized Passenger Demand Heatmap')
    plt.show()
