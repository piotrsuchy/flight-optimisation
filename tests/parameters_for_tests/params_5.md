For unallowed approach with update (to be compared to without update)

{
    "algo": {
        "POPULATION_SIZE": 20,
        "N_ITERATIONS": 200,
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


--- PRINTING FITNESS SCORES FOR ITER: 199 ---
Sol: 0, fit_score: 14482000
Sol: 1, fit_score: 13806000
Sol: 2, fit_score: 13996000
Sol: 3, fit_score: 13997000
Sol: 4, fit_score: 13956000
Sol: 5, fit_score: 14046000
Sol: 6, fit_score: 14193000
Sol: 7, fit_score: 14107000
Sol: 8, fit_score: 14149000
Sol: 9, fit_score: 14042000
Sol: 10, fit_score: 14234000
Sol: 11, fit_score: 14175000
Sol: 12, fit_score: 14547000
Sol: 13, fit_score: 14219000
Sol: 14, fit_score: 14115000
Sol: 15, fit_score: 10332000
Sol: 16, fit_score: 14346000
Sol: 17, fit_score: 14341000
Sol: 18, fit_score: 14310000
Sol: 19, fit_score: 14130000
Initial fitness values: [14584000, 14951000, 14151000, 14598000, 14532000, 14283000, 15002000, 14221000, 14260000, 14453000, 14145000, 14300000, 15014000, 14408000, 14552000, 13568000, 14573000, 13849000, 14099000, 14021000]

Another example:

--- PRINTING FITNESS SCORES FOR ITER: 199 ---
Sol: 0, fit_score: 9746000
Sol: 1, fit_score: 9498000
Sol: 2, fit_score: 9348000
Sol: 3, fit_score: 9267000
Sol: 4, fit_score: 9558000
Sol: 5, fit_score: 9591000
Sol: 6, fit_score: 9668000
Sol: 7, fit_score: 9551000
Sol: 8, fit_score: 9476000
Sol: 9, fit_score: 9645000
Sol: 10, fit_score: 9820000
Sol: 11, fit_score: 9771000
Sol: 12, fit_score: 9777000
Sol: 13, fit_score: 9783000
Sol: 14, fit_score: 9778000
Sol: 15, fit_score: 9523000
Sol: 16, fit_score: 10068000
Sol: 17, fit_score: 9821000
Sol: 18, fit_score: 9625000
Sol: 19, fit_score: 5952000
Initial fitness values: [10955000, 10056000, 10397000, 9839000, 10175000, 9611000, 10691000, 9803000, 9634000, 9995000, 9910000, 10475000, 10260000, 10056000, 9362000, 9202000, 9166000, 9259000, 9827000, 9022000]

With updates and parameters:
{
    "algo": {
        "POPULATION_SIZE": 20,
        "N_ITERATIONS": 200,
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
