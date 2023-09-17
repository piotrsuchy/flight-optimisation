from simulation.datageneration import DataGeneration

def main():
    sim = DataGeneration()
    sim.generate_data()
    for airport in sim.airports_list:
        print(f"Information about the crew at the {airport}:")
        print((sim.crew_information[airport]))


if __name__ == "__main__":
    main()