# Description
allowed approach

branch: allowed_fix_branch
commit fc2688ab393b6d4370d5991f2d86ed715129950b (HEAD -> allowed_fix_branch, origin/allowed_fix_branch)
Author: Piotr Suchy <piotrsuchy6@tlen.pl>
Date:   Fri Dec 22 00:35:58 2023 +0100

    Fixes and improvements for allowed method - two pop and with_init loops

commit c0acdb87f06376d32f68339a223591dd0283c699 (origin/main, main)
Author: Piotr Suchy <piotrsuchy6@tlen.pl>
Date:   Thu Dec 21 23:56:50 2023 +0100

    Added assignment to flights by worked hours heuristic


{
    "algo": {
        "POPULATION_SIZE": 16,
        "N_ITERATIONS": 300,
        "CROSSOVER_RATE": 0,
        "MUTATION_RATE": 1,
        "SELECTION_RATE": 0.5,
        "N_FLIGHTS_TO_MUT": 5
    },
    "sim": {
        "SIM_LEN": 720,
        "MAX_WEEKLY_HOURS": 60,
        "N_FLIGHTS": 60
    },
    "pen": {
        "LOCATION_PENALTY": 10000,
        "CANCEL_PENALTY": 100000,
        "REST_PENALTY": 1000,
        "TRAINING_OVERLAP_PENALTY": 5000
    },
    "structs": {
        "SEED_1": 32,
        "SEED_2": 38,
        "PILOTS_PER_PLANE": 2,
        "ATTEND_PER_PLANE": 4,
        "N_AIRPORTS": 10,
        "N_ATTENDANTS_F_A": 10,
        "N_PILOTS_F_A": 7,
        "PLANE_SPEED": 700
    }
}


{
    "algo": {
        "POPULATION_SIZE": 16,
        "N_ITERATIONS": 300,
        "CROSSOVER_RATE": 0,
        "MUTATION_RATE": 1,
        "SELECTION_RATE": 0.5,
        "N_FLIGHTS_TO_MUT": 5
    },
    "sim": {
        "SIM_LEN": 720,
        "MAX_WEEKLY_HOURS": 60,
        "N_FLIGHTS": 60
    },
    "pen": {
        "LOCATION_PENALTY": 10000,
        "CANCEL_PENALTY": 100000,
        "REST_PENALTY": 1000,
        "TRAINING_OVERLAP_PENALTY": 5000
    },
    "structs": {
        "SEED_1": 32,
        "SEED_2": 38,
        "PILOTS_PER_PLANE": 2,
        "ATTEND_PER_PLANE": 4,
        "N_AIRPORTS": 10,
        "N_ATTENDANTS_F_A": 10,
        "N_PILOTS_F_A": 7,
        "PLANE_SPEED": 700
    }
}

Po update:



## Wyniki 

---ITER: 298 ---Printing fitness scores---
WOAH
Sol ID: 13 Fit: 40000 Status: Mutated     Canc: 0, training_pen: 8.0
WOAH
Sol ID: 13 Fit: 40000 Status: Mutated     Canc: 0, training_pen: 8.0
WOAH
Sol ID: 13 Fit: 40000 Status: Mutated     Canc: 0, training_pen: 8.0
WOAH
Sol ID: 13 Fit: 40000 Status: Mutated     Canc: 0, training_pen: 8.0
Sol ID: 13 Fit: 160000 Status: Mutated     Canc: 1, training_pen: 12.0
Sol ID: 14 Fit: 160000 Status: Mutated     Canc: 1, training_pen: 12.0
Sol ID: 10 Fit: 180000 Status: Mutated     Canc: 1, training_pen: 16.0
Sol ID: 12 Fit: 180000 Status: Mutated     Canc: 1, training_pen: 16.0
Sol ID: 16 Fit: 190000 Status: Mutated     Canc: 1, training_pen: 18.0
Sol ID: 13 Fit: 195000 Status: Mutated     Canc: 1, training_pen: 19.0
Sol ID: 15 Fit: 200000 Status: Mutated     Canc: 1, training_pen: 20.0
Sol ID: 9 Fit: 205000 Status: Mutated     Canc: 1, training_pen: 21.0
Sol ID: 11 Fit: 210000 Status: Mutated     Canc: 1, training_pen: 22.0
Sol ID: 13 Fit: 355000 Status: Mutated     Canc: 3, training_pen: 11.0
Sol ID: 10 Fit: 475000 Status: Mutated     Canc: 4, training_pen: 15.0
Sol ID: 13 Fit: 775000 Status: Mutated     Canc: 7, training_pen: 15.0
---ITER: 299 ---Printing fitness scores---
WOAH
Sol ID: 13 Fit: 40000 Status: Mutated     Canc: 0, training_pen: 8.0
WOAH
Sol ID: 13 Fit: 40000 Status: Mutated     Canc: 0, training_pen: 8.0
WOAH
Sol ID: 13 Fit: 40000 Status: Mutated     Canc: 0, training_pen: 8.0
WOAH
Sol ID: 13 Fit: 40000 Status: Mutated     Canc: 0, training_pen: 8.0
Sol ID: 13 Fit: 145000 Status: Mutated     Canc: 1, training_pen: 9.0
Sol ID: 14 Fit: 155000 Status: Mutated     Canc: 1, training_pen: 11.0
Sol ID: 14 Fit: 165000 Status: Mutated     Canc: 1, training_pen: 13.0
Sol ID: 15 Fit: 165000 Status: Mutated     Canc: 1, training_pen: 13.0
Sol ID: 10 Fit: 170000 Status: Mutated     Canc: 1, training_pen: 14.0
Sol ID: 11 Fit: 175000 Status: Mutated     Canc: 1, training_pen: 15.0
Sol ID: 13 Fit: 175000 Status: Mutated     Canc: 1, training_pen: 15.0
Sol ID: 12 Fit: 180000 Status: Mutated     Canc: 1, training_pen: 16.0
Sol ID: 9 Fit: 185000 Status: Mutated     Canc: 1, training_pen: 17.0
Sol ID: 12 Fit: 200000 Status: Mutated     Canc: 1, training_pen: 20.0
Sol ID: 16 Fit: 220000 Status: Mutated     Canc: 1, training_pen: 24.0
Sol ID: 10 Fit: 400000 Status: Mutated     Canc: 3, training_pen: 20.0
----------------------------------------------------------------
WOAH
Sol ID: 13, fitness score: 40000, status: Mutated    , Total Flights: 60, Cancelled: 0, pil: 3, att: 4, train_pen: 8.0
WOAH
Sol ID: 13, fitness score: 40000, status: Mutated    , Total Flights: 60, Cancelled: 0, pil: 3, att: 4, train_pen: 8.0
WOAH
Sol ID: 13, fitness score: 40000, status: Mutated    , Total Flights: 60, Cancelled: 0, pil: 3, att: 4, train_pen: 8.0
WOAH
Sol ID: 13, fitness score: 40000, status: Mutated    , Total Flights: 60, Cancelled: 0, pil: 3, att: 4, train_pen: 8.0
Sol ID: 13, fitness score: 145000, status: Mutated    , Total Flights: 60, Cancelled: 1, pil: 3, att: 5, train_pen: 9.0
Sol ID: 14, fitness score: 155000, status: Mutated    , Total Flights: 60, Cancelled: 1, pil: 0, att: 4, train_pen: 11.0
Sol ID: 14, fitness score: 165000, status: Mutated    , Total Flights: 60, Cancelled: 1, pil: 0, att: 2, train_pen: 13.0
Sol ID: 15, fitness score: 165000, status: Mutated    , Total Flights: 60, Cancelled: 1, pil: 0, att: 2, train_pen: 13.0
Sol ID: 10, fitness score: 170000, status: Mutated    , Total Flights: 60, Cancelled: 1, pil: 0, att: 2, train_pen: 14.0
Sol ID: 11, fitness score: 175000, status: Mutated    , Total Flights: 60, Cancelled: 1, pil: 0, att: 2, train_pen: 15.0
Sol ID: 13, fitness score: 175000, status: Mutated    , Total Flights: 60, Cancelled: 1, pil: 0, att: 2, train_pen: 15.0
Sol ID: 12, fitness score: 180000, status: Mutated    , Total Flights: 60, Cancelled: 1, pil: 0, att: 2, train_pen: 16.0
Sol ID: 9, fitness score: 185000, status: Mutated    , Total Flights: 60, Cancelled: 1, pil: 0, att: 2, train_pen: 17.0
Sol ID: 12, fitness score: 200000, status: Mutated    , Total Flights: 60, Cancelled: 1, pil: 0, att: 4, train_pen: 20.0
Sol ID: 16, fitness score: 220000, status: Mutated    , Total Flights: 60, Cancelled: 1, pil: 0, att: 2, train_pen: 24.0
Sol ID: 10, fitness score: 400000, status: Mutated    , Total Flights: 60, Cancelled: 3, pil: 0, att: 6, train_pen: 20.0
