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

## DATABASE abbreviations

The "tra_meas" abbreviations are related to different measurements of passenger traffic:

CAF_PAS: This refers to the "Capacity" in terms of "Passengers". It might indicate the total number of seats available on all flights.

CAF_PAS_ARR: This refers to the "Capacity" in terms of "Passengers Arriving". It might indicate the total number of seats available on all arriving flights.

CAF_PAS_DEP: This refers to the "Capacity" in terms of "Passengers Departing". It might indicate the total number of seats available on all departing flights.

PAS_BRD: This refers to "Passengers Boarded". It might indicate the total number of passengers who boarded flights.

PAS_BRD_ARR: This refers to "Passengers Boarded Arriving". It might indicate the total number of passengers who boarded and arrived at the destination.

PAS_BRD_DEP: This refers to "Passengers Boarded Departing". It might indicate the total number of passengers who boarded and departed from the origin.

PAS_CRD: This refers to "Passengers Carried". It might indicate the total number of passengers carried on all flights.

PAS_CRD_ARR: This refers to "Passengers Carried Arriving". It might indicate the total number of passengers carried on all arriving flights.

PAS_CRD_DEP: This refers to "Passengers Carried Departing". It might indicate the total number of passengers carried on all departing flights.

## Notes

- From Airlines' Crew Pairing Optimization: A Brief Review - Xugang Ye - John Hopkins University, 2007:
"As an important issue of airlines’ operational planning, crew pairing immediately follows fleet assignment phase and right precedes crew rostering phase. A pairing is a sequence of connectable flight legs, within the same fleet, that starts from and ends at the same crew base, where the crew actually lives. A pairing is sometimes called an itinerary for the crew assigned to this journey. It typically spans from one to five days."
