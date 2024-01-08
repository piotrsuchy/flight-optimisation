# Flight Optimisation - Crew assignment optimization using approximate algorithms

This repository contains code for an engineering thesis which implements an evolutionary algorithm that optimizes crew assignment for an immutable flight schedule. The objective of this optimization is to minimize the operational costs and the penalties associated with wrong assignments, overtime work etc.

Lines of Code: ~2300

## Two Approaches

I have implemented two approaches to solve this optimization problem. The basis of the first one is an event-based simulation which utilizes object oriented programming. The second uses a matrix like solutions and most of the computation is done in the calculate_fitness function which takes care of tracking the location and availability of the crew members.

The first approach has more code, which can be found in the src/ directory, while the second approach is a bit simpler and demanded less lines of code. The location of the second approach - also called unallowed_approach is the src/unallowed_approach directory.

To run the programs locally, clone / download the repository, create a venv, source it and download the dependencies using pip and requirements.txt. Afterwards to run the optimization using the first approach run:

```bash
python main.py --log
```

Or skip --log flag if you don't want print statements in your terminal.

To run the second approach use the command:

```bash
python src/unallowed_approach/imp_evol_algo.py 
```

Or chmod one of the two already created bash scripts and use it: ./run_with_logs.sh or ./src/unallowed_approach/scripts/run_with_penalty_logs.sh

## Crew Assignment Problem - Theory

Often divided into two subproblems (description taken from [Modeling and solving a Crew Assignment Problem in air transportation](https://www.sciencedirect.com/science/article/abs/pii/S0377221705003760#:~:text=Introduction%20For%20airline%20companies%2C%20the,costs%20and%20fuel%20consumption%20costs)):

- **Crew Pairing Problem** - it consists in generating a set of minimal cost crew pairings covering all the planned flight segments. A crew pairing is a sequence of flight segments separated by connections or rest periods, operated by crew leaving and returning to the same crew home base.
- **Working Schedules Construction Problem** - it aims at constructing working schedules for crew members by assigning them pairings, resulting from the above subproblem, training periods, annual leaves etc.

Those two subproblems are usually formulated as Set Partitioning or Set Covering problems, where variables are possible pairings and feasible working schedules respectively.

The drawback of such a formulation is that in a standard model and formulation of the problem it is assumed that the crew for given flight services in a given pairing is the same - that is, none of the members of the crew change during the pairing, which can lead to some inflexibility.

## Some abstract objects (classes) that I am using and what is their purpose

1. **EvolutionaryAlgorithm** - the highest level class in the hierarchy. Serves as an interface through which the evolutionary algorithm's processes are called.
2. **Solution** - has its own scheduler assigned.
3. **Airport** - main building block of the structures. Strict and unchangeable for a simulation. Each solution at the beginning has the same airports, with the same pilots, planes and attendants. Has a structure called AvailabilityLog to log availability of different objects during the simulation.
4. **Flight** - the main event that happens during the simulation. A number of flights are scheduled for each of the solutions in the algorithms' population. Each flight has following properties: base, destination, plane, pilots (2), attendants (4), status, day of flight etc. Flight is assigned to a solution.
5. **AvailabilityLog** - connected to a given airport (and unique for each solution). Contains Availability objects which are snapshots of availibility of planes, pilots and attendants at a given airport at the time of some event of the simulation - e.g. a start of the flight or end of a rest period of a crew member.

## Mutations

First mutation that is being implemented is a choice of a different available pilot or attendant of a random flight in a solution. This happens with a given probability of course.
The trick with mutations in my implementation of the algorithm and simulation is the need for resimulation of the events after the mutation. Each event with a property simulation_time of the mutated flight should be resimulated - because the assignment of pilots and crew members (and planes as well) impacts the possibility of assignment in the future.

## Important parameters for tests

1. **N_AIRPORTS** - this tells the probability of wrong assignment in the second approach (the % being: 1/N_AIRPORTS*100%). For the first approach there are memory limitations which should be taken into account.
2. **The ratio of N_FLIGHTS / N_AIRPORTS \* N_ATTENDANTS_F_A \* N_PILOTS_F_A** - this tells us how much the crew members will have to work. The bigger the ratio, the more the crew will have to work and the more flights will have to be cancelled.
