---
17.12.2023
last commit_hash = commit 0d06d7f3ba702482076404ef90d3aa63180e2ef5 (HEAD -> unallowed_approach_training_sessions_branch)
Author: Piotr Suchy <piotrsuchy6@tlen.pl>
Date:   Sun Dec 17 19:51:11 2023 +0100

    Added training hours penalty into fitness calc
---
{
    "algo": {
        "POPULATION_SIZE": 20,
        "N_ITERATIONS": 2000,
        "CROSSOVER_RATE": 0.3,
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
        "N_FLIGHTS": 600
    },
    "pen": {
        "LOCATION_PENALTY": 10000,
        "CANCEL_PENALTY": 100000,
        "REST_PENALTY": 1000,
        "TRAINING_OVERLAP_PENALTY": 5000
    },
    "structs": {
        "SEED_1": 43,
        "SEED_2": 20,
        "PILOTS_PER_PLANE": 2,
        "ATTEND_PER_PLANE": 4,
        "N_AIRPORTS": 10,
        "N_ATTENDANTS_F_A": 30,
        "N_PILOTS_F_A": 15,
        "PLANE_SPEED": 700
    }
}


--- PRINTING FITNESS SCORES FOR ITER: 1999 ---
Sol: 0, fit_score: 29807000
Sol: 1, fit_score: 29861000
Sol: 2, fit_score: 29884000
Sol: 3, fit_score: 29275000
Sol: 4, fit_score: 29865000
Sol: 5, fit_score: 30085000
Sol: 6, fit_score: 29999000
Sol: 7, fit_score: 30196000
Sol: 8, fit_score: 29967000
Sol: 9, fit_score: 30043000
Sol: 10, fit_score: 30080000
Sol: 11, fit_score: 29998000
Sol: 12, fit_score: 30035000
Sol: 13, fit_score: 30102000
Sol: 14, fit_score: 29919000
Sol: 15, fit_score: 30056000
Sol: 16, fit_score: 30021000
Sol: 17, fit_score: 29908000
Sol: 18, fit_score: 30037000
Sol: 19, fit_score: 29937000
Initial fitness values: [33859000, 33814000, 33745000, 33819000, 33889000, 33920000, 33973000, 33848000, 33761000, 33840000, 33796000, 33808000, 34007000, 33806000, 33869000, 33832000, 33761000, 33833000, 33865000, 33656000]
