from src.simulation import Simulation
import sys

def main():
    print(sys.path)
    sim = Simulation()
    sim.generate_structs()
    # sim.print_structures()
    sim.run_simulation()
    # sim.print_structures()

if __name__ == "__main__":
    main()