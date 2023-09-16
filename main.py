from simulation.simulation import Simulation

def main():
    sim = Simulation()
    sim.run_simulation()
    for airport in sim.airports_list:
        print(f"Information about the crew at the {airport}:")
        print((sim.crew_information[airport]))


if __name__ == "__main__":
    main()