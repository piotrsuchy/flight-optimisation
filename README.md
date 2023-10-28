# Flight Optimisation

## After a review by my thesis supervisor I have decided to focus on mostly one topic

Crew management, crew assignment, taking into account a strict schedule that should not be changed.

## Some abstract objects (classes) that I am using and what is their purpose

1. **EvolutionaryAlgorithm** - the highest level class in the hierarchy. Serves as an interface through which the evolutionary algorithm's processes are called.
2. **Solution** - has its own scheduler assigned.
3. **Airport** - main building block of the structures. Strict and unchangeable for a simulation. Each solution at the beginning has the same airports, with the same pilots, planes and attendants. Has a structure called AvailabilityLog to log availability of different objects during the simulation.
4. **Flight** - the main event that happens during the simulation. A number of flights are scheduled for each of the solutions in the algorithms' population. Each flight has following properties: base, destination, plane, pilots (2), attendants (4), status, day of flight etc. Flight is assigned to a solution.
5. **AvailabilityLog** - connected to a given airport (and unique for each solution). Contains Availability objects which are snapshots of availibility of planes, pilots and attendants at a given airport at the time of some event of the simulation - e.g. a start of the flight or end of a rest period of a crew member.

## Mutations

First mutation that is being implemented is a choice of a different available pilot or attendant of a random flight in a solution. This happens with a given probability of course.
The trick with mutations in my implementation of the algorithm and simulation is the need for resimulation of the events after the mutation. Each event with a property simulation_time of the mutated flight should be resimulated - because the assignment of pilots and crew members (and planes as well) impacts the possibility of assignment in the future.

## Crossovers

TBA

## Creation of a new population

TBA

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

### Time performance analysis for different parameters

For basis parameters like this:

```python
BASELINE_PARAMS = {
    'N_AIRPORTS': 10,
    'N_FLIGHTS': 300,
    'N_PILOTS_F_A': 6,
    'N_ATTENDANTS_F_A': 12,
    'N_PLANES_F_A': 4
}
```

With logging on:

{'param': 'N_AIRPORTS', 'factor': 100, 'duration': 0.03007817268371582}
{'param': 'N_AIRPORTS', 'factor': 1000, 'duration': 0.24370408058166504}
{'param': 'N_FLIGHTS', 'factor': 1, 'duration': 0.013833761215209961}
{'param': 'N_FLIGHTS', 'factor': 10, 'duration': 0.1171109676361084}
{'param': 'N_FLIGHTS', 'factor': 100, 'duration': 1.002060890197754}
{'param': 'N_FLIGHTS', 'factor': 1000, 'duration': 10.688832998275757}
{'param': 'N_PILOTS_F_A', 'factor': 1, 'duration': 0.013334035873413086}
{'param': 'N_PILOTS_F_A', 'factor': 10, 'duration': 0.014071941375732422}
{'param': 'N_PILOTS_F_A', 'factor': 100, 'duration': 0.02051520347595215}
{'param': 'N_PILOTS_F_A', 'factor': 1000, 'duration': 0.10367083549499512}
{'param': 'N_ATTENDANTS_F_A', 'factor': 1, 'duration': 0.012994766235351562}
{'param': 'N_ATTENDANTS_F_A', 'factor': 10, 'duration': 0.015036821365356445}
{'param': 'N_ATTENDANTS_F_A', 'factor': 100, 'duration': 0.027924776077270508}
{'param': 'N_ATTENDANTS_F_A', 'factor': 1000, 'duration': 0.2050337791442871}
{'param': 'N_PLANES_F_A', 'factor': 1, 'duration': 0.01307988166809082}
{'param': 'N_PLANES_F_A', 'factor': 10, 'duration': 0.013455867767333984}
{'param': 'N_PLANES_F_A', 'factor': 100, 'duration': 0.020437002182006836}
{'param': 'N_PLANES_F_A', 'factor': 1000, 'duration': 0.1170799732208252}
All 10x, flights 100x, duration: 43.92963194847107

With logging off:

{'param': 'N_AIRPORTS', 'factor': 1, 'duration': 0.005341768264770508}
{'param': 'N_AIRPORTS', 'factor': 10, 'duration': 0.007319927215576172}
{'param': 'N_AIRPORTS', 'factor': 100, 'duration': 0.021706104278564453}
{'param': 'N_AIRPORTS', 'factor': 1000, 'duration': 0.24149513244628906}
{'param': 'N_FLIGHTS', 'factor': 1, 'duration': 0.005631923675537109}
{'param': 'N_FLIGHTS', 'factor': 10, 'duration': 0.032450199127197266}
{'param': 'N_FLIGHTS', 'factor': 100, 'duration': 0.1964428424835205}
{'param': 'N_FLIGHTS', 'factor': 1000, 'duration': 2.2318060398101807}
{'param': 'N_PILOTS_F_A', 'factor': 1, 'duration': 0.00457310676574707}
{'param': 'N_PILOTS_F_A', 'factor': 10, 'duration': 0.00556492805480957}
{'param': 'N_PILOTS_F_A', 'factor': 100, 'duration': 0.011811971664428711}
{'param': 'N_PILOTS_F_A', 'factor': 1000, 'duration': 0.0934140682220459}
{'param': 'N_ATTENDANTS_F_A', 'factor': 1, 'duration': 0.004324197769165039}
{'param': 'N_ATTENDANTS_F_A', 'factor': 10, 'duration': 0.006437063217163086}
{'param': 'N_ATTENDANTS_F_A', 'factor': 100, 'duration': 0.019613981246948242}
{'param': 'N_ATTENDANTS_F_A', 'factor': 1000, 'duration': 0.1790308952331543}
{'param': 'N_PLANES_F_A', 'factor': 1, 'duration': 0.0044498443603515625}
{'param': 'N_PLANES_F_A', 'factor': 10, 'duration': 0.005507707595825195}
{'param': 'N_PLANES_F_A', 'factor': 100, 'duration': 0.01198887825012207}
{'param': 'N_PLANES_F_A', 'factor': 1000, 'duration': 0.1057891845703125}
All 10x, flights 100x, duration: 41.32940483093262
