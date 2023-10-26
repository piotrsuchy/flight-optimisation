# Flight Optimisation

## After a review by my thesis supervisor I have decided to focus on mostly one topic

Crew management, crew assignment, taking into account a strict schedule that should not be changed.

## Classes and how they interact

- **Airport** - id, coordinates, lists of crew and fleet available at the given airport
- **Plane** - id, base, capacity, pilots_needed, attendants_needed, speed
- **Pilot** - id, base, cur_base, hours worked in a day, week and month, flights taken
- **Attendant** - id, base, cur_base, hours worked in a day, week and month, flights taken

All classes also have methods and fields connected with maintenance, rest times, checking availability etc.

## Solution

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
