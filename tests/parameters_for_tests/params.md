---
17.12.2023
last_commit_hash = commit 01294ef4ceeaead5eb766fe56a51228be2307cf7 
---

{
    "algo": {
        "POPULATION_SIZE": 10,
        "N_ITERATIONS": 100,
        "CROSSOVER_RATE": 0,
        "MUTATION_RATE": 1,
        "SELECTION_RATE": 0.5
    },
    "sim": {
        "SIM_LEN": 720,
        "PLANE_OPERATIONAL_COST_PER_HOUR": 2000,
        "PILOT_COST_PER_HOUR": 120,
        "ATTENDANT_COST_PER_HOUR": 80,
        "MAX_WEEKLY_HOURS": 60,
        "OVERWORK_PENALTY_PER_HOUR": 240,
        "N_FLIGHTS": 100
    },
    "pen": {
        "LOCATION_PENALTY": 10000,
        "CANCEL_PENALTY": 1000000,
        "REST_PENALTY": 500
    },
    "structs": {
        "SEED_1": 43,
        "SEED_2": 20,
        "PILOTS_PER_PLANE": 2,
        "ATTEND_PER_PLANE": 4,
        "N_AIRPORTS": 10,
        "N_ATTENDANTS_F_A": 10,
        "N_PILOTS_F_A": 5,
        "PLANE_SPEED": 700
    }
}

// for allowed_approach - from 8-9 cancelled to
// 5 - 6 cancelled