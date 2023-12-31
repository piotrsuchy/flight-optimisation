# TODO

## Both approaches

- penalty tracking - initial vs final to add to the fitness scores
- maybe add days off in the same way as training overlap (?)

## Unallowed approach

- add informed mutation

## Allowed approach

- getting the solutions form from the simulation

## How to create common structures - DONE

File in .json format from the unallowed_approach will be used to generate the structs in allowed_approach.
The commonalities will have to be:

- each airport has the same distance to each other - this will be taken from distance_matrix
- each airport of a given location has the same amount of crew with the same training hours at the beginning of the simulation - this will be taken from pilots_status_pop and attend_status_pop
- all of the flights have the corresponding source and destination and timestamp - this will be taken from population
