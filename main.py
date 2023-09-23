from classes.datageneration import DataGeneration
from simulation import Simulation

def main():
    # sim = DataGeneration()
    # sim.generate_data()
    # for airport in sim.airports_list:
        # print(f"Information about the crew at the {airport}:")
        # print((sim.crew_information[airport]))

    sim = Simulation()
    sim.generate_structs()
    sim.run_simulation()

if __name__ == "__main__":
    main()