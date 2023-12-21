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
