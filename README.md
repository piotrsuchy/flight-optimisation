# Flight Optimisation

## Classes and how they interact

- **Airport** - id, coordinates, lists of crew and fleet available at the given airport
- **Plane** - id, base, capacity, pilots_needed, attendants_needed, speed
- **Pilot** - id, base, cur_base, hours worked in a day, week and month, flights taken
- **Attendant** - id, base, cur_base, hours worked in a day, week and month, flights taken

All classes also have methods and fields connected with maintenance, rest times, checking availability etc.

## Simulation

1. Generate structures: Airports, Planes assigned to specific Airports, Pilots and Attendants assigned to specific Airports.
2. Generate table of flights - schedule random flights by choosing random delay time, random base airport and random destination airport.
3. Run the simulation, while checking for possibility of certain actions based on the regulations.

## Optimisation by Evolutionary Algorithm

Before optimising and evaluating I would like to create a data structure that would describe the passengers' demand.

1. Generate random initial population with 100 members.
2. Mutate and Cross the members of the population.
3. Evaluate with a fitness function and select the members of the next population based on some ranking (Selection types: Roulette, Tournament, Ranking)
4. Go back to step 2.

This process should be repeated many times - the number of repetitions will be n - number of iterations.

## Notes

- From Airlines' Crew Pairing Optimization: A Brief Review - Xugang Ye - John Hopkins University, 2007:
"As an important issue of airlines’ operational planning, crew pairing immediately follows fleet assignment phase and right precedes crew rostering phase. A pairing is a sequence of connectable flight legs, within the same fleet, that starts from and ends at the same crew base, where the crew actually lives. A pairing is sometimes called an itinerary for the crew assigned to this journey. It typically spans from one to five days."

### Optimisation by a Genetic Algorithm research

1. [Pseudocoevolutionary Genetic Algorithms for Power Electronic Circuits Optimization](https://web.archive.org/web/20110707025618/http://www.cs.sysu.edu.cn/~jzhang/papers/SMCC.pdf#)
2. [Genetic algorithm based airlines booking terminal open/close decision system](https://dl.acm.org/doi/abs/10.1145/2345396.2345426)
3. [An extensible Evolutionary Algorithm Example in Python](https://towardsdatascience.com/an-extensible-evolutionary-algorithm-example-in-python-7372c56a557b)
4. [Task scheduling Algorithm using CMA ES in Cloud Computing](https://jacet.srbiau.ac.ir/article_10641_f33706f4f318ee00b09343d530580343.pdf)
5. [Genetic Synthesis of Recurrent Neural Networks](http://arimaa.com/arimaa/about/Thesis/Thesis.pdf)
6. [Evolutionary algorithms and their applications to engineering problems](https://link.springer.com/article/10.1007/s00521-020-04832-8)

### Extra questions to think about

- what about a return flight after a period of time for passengers?
- what about planes being late, do I add that into the calculations?
- what about time zone considerations?
