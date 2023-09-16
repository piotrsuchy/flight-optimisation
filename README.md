# Flight Optimisation

## This repository will contain code for an engineering thesis about flight optimisation

With things like:

- pairing
- crew assignment
- schedule optimisation
etc. using an evolutionary algorithm.

## Plans

1. **Schedule Optimalisation** - based on time, plane and path choice:
    - need data about the fleet for each airport (to be able to choose planes)
    - have a basic view of demand for flights from airport to airport - based on that we could start the simulation and fit the solutions, based on how many passengers were transported (ideally with time)
    - create a matrix with all the airport that I want to include in the simulation (airports for which I have data) and the distances between all of them
    - calculate costs of the travel for each path
2. **Crew Assignment**
    - will need data about the crew
    - will need data about the compensations and legal requirements connected to crew members
    - will need data on capacities of each plane in terms of crew
3. **Crew Pairing**
    - !! a pairing is a sequence of connectable flight legs, within the same fleet, that starts from and ends at the same crew base, where the crew actually lives (from 1 to 5 days) !!
    - ideas on how to implement this to a fitness function

## TODO steps

- find a dataset that will provide an overview of demand
- flight planning based on costs and profits
- download "DB1B Market (All Carriers)" database and use it for analysis of passangers

FLIGHT and PAS: These are likely to be units of measurement. "FLIGHT" could refer to the number of flights, while "PAS" likely refers to the number of passengers.

## Alternative approach

Instead of working with a real dataset to simulate demand I can create a fictional dataset with data that contains:

- airports
- fleet
- demand - passengers wanting to fly from one place to another

## Notes

- From Airlines' Crew Pairing Optimization: A Brief Review - Xugang Ye - John Hopkins University, 2007:
"As an important issue of airlines’ operational planning, crew pairing immediately follows fleet assignment phase and right precedes crew rostering phase. A pairing is a sequence of connectable flight legs, within the same fleet, that starts from and ends at the same crew base, where the crew actually lives. A pairing is sometimes called an itinerary for the crew assigned to this journey. It typically spans from one to five days."

## Optimisation by a Genetic Algorithm research

1. [Pseudocoevolutionary Genetic Algorithms for Power Electronic Circuits Optimization](https://web.archive.org/web/20110707025618/http://www.cs.sysu.edu.cn/~jzhang/papers/SMCC.pdf#)
2. [Genetic algorithm based airlines booking terminal open/close decision system](https://dl.acm.org/doi/abs/10.1145/2345396.2345426)
3. [An extensible Evolutionary Algorithm Example in Python](https://towardsdatascience.com/an-extensible-evolutionary-algorithm-example-in-python-7372c56a557b)
4. [Task scheduling Algorithm using CMA ES in Cloud Computing](https://jacet.srbiau.ac.ir/article_10641_f33706f4f318ee00b09343d530580343.pdf)
5. [Genetic Synthesis of Recurrent Neural Networks](http://arimaa.com/arimaa/about/Thesis/Thesis.pdf)
6. [Evolutionary algorithms and their applications to engineering problems](https://link.springer.com/article/10.1007/s00521-020-04832-8)

## Questions to think about

- what about a return flight after a period of time for passengers?
- what about planes being late, do I add that into the calculations?
- what about time zone considerations?
