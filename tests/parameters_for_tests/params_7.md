# Description

unallowed_approach
last_commit_hash:

```bash
commit e24017381a8637f51dd9b622267bad8afb7a2d82 (HEAD -> add_informed_mutations_branch, origin/main, main)
Author: Piotr Suchy <piotrsuchy6@tlen.pl>
Date:   Tue Dec 19 17:55:11 2023 +0100

    Renaming of main files for both approaches

commit 78c9d63acb1ff08b55a900aa6848452475a61d09
Author: Piotr Suchy <piotrsuchy6@tlen.pl>
Date:   Tue Dec 19 16:36:44 2023 +0100

    Added penalty and best_score printing, fixed initial_gen_with_updates, QoL fixes
```

## Params

{
    "algo": {
        "POPULATION_SIZE": 30,
        "N_ITERATIONS": 500,
        "CROSSOVER_RATE": 0,
        "MUTATION_RATE": 1,
        "SELECTION_RATE": 0.5
    },
    "sim": {
        "SIM_LEN": 720,
        "MAX_WEEKLY_HOURS": 60,
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
        "N_AIRPORTS": 20,
        "N_ATTENDANTS_F_A": 8,
        "N_PILOTS_F_A": 4,
        "PLANE_SPEED": 700
    }
}

## Results

---PRINTING BEST FITNESS SCORE: 21508000
Initial sols: [21931000, 21813000, 21887000, 21808000, 21768000, 21794000, 21860000, 21769000, 21844000, 21702000, 21877000, 21803000, 21859000, 21871000, 21774000, 21782000, 21992000, 21783000, 21922000, 21726000, 21801000, 21781000, 21839000, 21760000, 21862000, 21786000, 21845000, 21808000, 21886000, 21908000]
--- PRINTING FITNESS SCORES FOR ITER: 499 ---
Sol: 0, fit_score: 21508000
Sol: 1, fit_score: 21508000
Sol: 2, fit_score: 21508000
Sol: 3, fit_score: 21508000
Sol: 4, fit_score: 21508000
Sol: 5, fit_score: 21508000
Sol: 6, fit_score: 21508000
Sol: 7, fit_score: 21508000
Sol: 8, fit_score: 21508000
Sol: 9, fit_score: 21508000
Sol: 10, fit_score: 21508000
Sol: 11, fit_score: 21508000
Sol: 12, fit_score: 21508000
Sol: 13, fit_score: 21508000
Sol: 14, fit_score: 21508000
Sol: 15, fit_score: 21669000
Sol: 16, fit_score: 21697000
Sol: 17, fit_score: 21681000
Sol: 18, fit_score: 21623000
Sol: 19, fit_score: 21835000
Sol: 20, fit_score: 21711000
Sol: 21, fit_score: 21764000
Sol: 22, fit_score: 21589000
Sol: 23, fit_score: 21635000
Sol: 24, fit_score: 21679000
Sol: 25, fit_score: 21811000
Sol: 26, fit_score: 21813000
Sol: 27, fit_score: 21663000
Sol: 28, fit_score: 21765000
Sol: 29, fit_score: 21908000
---PRINTING BEST FITNESS SCORE: 21508000
Initial sols: [21931000, 21813000, 21887000, 21808000, 21768000, 21794000, 21860000, 21769000, 21844000, 21702000, 21877000, 21803000, 21859000, 21871000, 21774000, 21782000, 21992000, 21783000, 21922000, 21726000, 21801000, 21781000, 21839000, 21760000, 21862000, 21786000, 21845000, 21808000, 21886000, 21908000]
Initial fitness values: [21931000, 21813000, 21887000, 21808000, 21768000, 21794000, 21860000, 21769000, 21844000, 21702000, 21877000, 21803000, 21859000, 21871000, 21774000, 21782000, 21992000, 21783000, 21922000, 21726000, 21801000, 21781000, 21839000, 21760000, 21862000, 21786000, 21845000, 21808000, 21886000, 21908000]
---Final penalties applied---
Sol: 0, Fit: 21508000 Loc: 136, Rest: 1128, Canc: 184, training overlap: 124, Prop. alloc: 2360
Sol: 1, Fit: 21508000 Loc: 136, Rest: 1128, Canc: 184, training overlap: 124, Prop. alloc: 2360
Sol: 2, Fit: 21508000 Loc: 136, Rest: 1128, Canc: 184, training overlap: 124, Prop. alloc: 2360
Sol: 3, Fit: 21508000 Loc: 136, Rest: 1128, Canc: 184, training overlap: 124, Prop. alloc: 2360
Sol: 4, Fit: 21508000 Loc: 136, Rest: 1128, Canc: 184, training overlap: 124, Prop. alloc: 2360
Sol: 5, Fit: 21508000 Loc: 136, Rest: 1128, Canc: 184, training overlap: 124, Prop. alloc: 2360
Sol: 6, Fit: 21508000 Loc: 136, Rest: 1128, Canc: 184, training overlap: 124, Prop. alloc: 2360
Sol: 7, Fit: 21508000 Loc: 136, Rest: 1128, Canc: 184, training overlap: 124, Prop. alloc: 2360
Sol: 8, Fit: 21508000 Loc: 136, Rest: 1128, Canc: 184, training overlap: 124, Prop. alloc: 2360
Sol: 9, Fit: 21508000 Loc: 136, Rest: 1128, Canc: 184, training overlap: 124, Prop. alloc: 2360
Sol: 10, Fit: 21508000 Loc: 136, Rest: 1128, Canc: 184, training overlap: 124, Prop. alloc: 2360
Sol: 11, Fit: 21508000 Loc: 136, Rest: 1128, Canc: 184, training overlap: 124, Prop. alloc: 2360
Sol: 12, Fit: 21508000 Loc: 136, Rest: 1128, Canc: 184, training overlap: 124, Prop. alloc: 2360
Sol: 13, Fit: 21508000 Loc: 136, Rest: 1128, Canc: 184, training overlap: 124, Prop. alloc: 2360
Sol: 14, Fit: 21508000 Loc: 136, Rest: 1128, Canc: 184, training overlap: 124, Prop. alloc: 2360
Sol: 15, Fit: 21669000 Loc: 152, Rest: 1124, Canc: 184, training overlap: 125, Prop. alloc: 2344
Sol: 16, Fit: 21697000 Loc: 154, Rest: 1132, Canc: 184, training overlap: 125, Prop. alloc: 2342
Sol: 17, Fit: 21681000 Loc: 153, Rest: 1131, Canc: 184, training overlap: 124, Prop. alloc: 2343
Sol: 18, Fit: 21623000 Loc: 148, Rest: 1123, Canc: 184, training overlap: 124, Prop. alloc: 2348
Sol: 19, Fit: 21835000 Loc: 169, Rest: 1125, Canc: 184, training overlap: 124, Prop. alloc: 2327
Sol: 20, Fit: 21711000 Loc: 156, Rest: 1131, Canc: 184, training overlap: 124, Prop. alloc: 2340
Sol: 21, Fit: 21764000 Loc: 162, Rest: 1124, Canc: 184, training overlap: 124, Prop. alloc: 2334
Sol: 22, Fit: 21589000 Loc: 144, Rest: 1129, Canc: 184, training overlap: 124, Prop. alloc: 2352
Sol: 23, Fit: 21635000 Loc: 148, Rest: 1130, Canc: 184, training overlap: 125, Prop. alloc: 2348
Sol: 24, Fit: 21679000 Loc: 153, Rest: 1129, Canc: 184, training overlap: 124, Prop. alloc: 2343
Sol: 25, Fit: 21811000 Loc: 167, Rest: 1121, Canc: 184, training overlap: 124, Prop. alloc: 2329
Sol: 26, Fit: 21813000 Loc: 166, Rest: 1133, Canc: 184, training overlap: 124, Prop. alloc: 2330
Sol: 27, Fit: 21663000 Loc: 152, Rest: 1128, Canc: 184, training overlap: 123, Prop. alloc: 2344
Sol: 28, Fit: 21765000 Loc: 161, Rest: 1125, Canc: 184, training overlap: 126, Prop. alloc: 2335
---Initial penalties applied---
Sol: 0, Fit: 21931000 Loc: 99, Rest: 1141, Canc: 190, train_ov: 160, Prop. alloc: 2361
Sol: 1, Fit: 21813000 Loc: 98, Rest: 1143, Canc: 190, train_ov: 138, Prop. alloc: 2362
Sol: 2, Fit: 21887000 Loc: 97, Rest: 1127, Canc: 190, train_ov: 158, Prop. alloc: 2363
Sol: 3, Fit: 21808000 Loc: 100, Rest: 1128, Canc: 190, train_ov: 136, Prop. alloc: 2360
Sol: 4, Fit: 21768000 Loc: 97, Rest: 1128, Canc: 190, train_ov: 134, Prop. alloc: 2363
Sol: 5, Fit: 21794000 Loc: 98, Rest: 1144, Canc: 190, train_ov: 134, Prop. alloc: 2362
Sol: 6, Fit: 21860000 Loc: 99, Rest: 1120, Canc: 190, train_ov: 150, Prop. alloc: 2361
Sol: 7, Fit: 21769000 Loc: 97, Rest: 1129, Canc: 190, train_ov: 134, Prop. alloc: 2363
Sol: 8, Fit: 21844000 Loc: 97, Rest: 1144, Canc: 190, train_ov: 146, Prop. alloc: 2363
Sol: 9, Fit: 21702000 Loc: 97, Rest: 1122, Canc: 190, train_ov: 122, Prop. alloc: 2363
Sol: 10, Fit: 21877000 Loc: 99, Rest: 1157, Canc: 190, train_ov: 146, Prop. alloc: 2361
Sol: 11, Fit: 21803000 Loc: 97, Rest: 1128, Canc: 190, train_ov: 141, Prop. alloc: 2363
Sol: 12, Fit: 21859000 Loc: 100, Rest: 1119, Canc: 190, train_ov: 148, Prop. alloc: 2360
Sol: 13, Fit: 21871000 Loc: 101, Rest: 1131, Canc: 190, train_ov: 146, Prop. alloc: 2359
Sol: 14, Fit: 21774000 Loc: 97, Rest: 1124, Canc: 190, train_ov: 136, Prop. alloc: 2363
Sol: 15, Fit: 21782000 Loc: 99, Rest: 1127, Canc: 190, train_ov: 133, Prop. alloc: 2361
Sol: 16, Fit: 21992000 Loc: 96, Rest: 1117, Canc: 190, train_ov: 183, Prop. alloc: 2364
Sol: 17, Fit: 21783000 Loc: 98, Rest: 1118, Canc: 190, train_ov: 137, Prop. alloc: 2362
Sol: 18, Fit: 21922000 Loc: 97, Rest: 1147, Canc: 190, train_ov: 161, Prop. alloc: 2363
Sol: 19, Fit: 21726000 Loc: 95, Rest: 1121, Canc: 190, train_ov: 131, Prop. alloc: 2365
Sol: 20, Fit: 21801000 Loc: 98, Rest: 1141, Canc: 190, train_ov: 136, Prop. alloc: 2362
Sol: 21, Fit: 21781000 Loc: 97, Rest: 1141, Canc: 190, train_ov: 134, Prop. alloc: 2363
Sol: 22, Fit: 21839000 Loc: 97, Rest: 1139, Canc: 190, train_ov: 146, Prop. alloc: 2363
Sol: 23, Fit: 21760000 Loc: 98, Rest: 1135, Canc: 190, train_ov: 129, Prop. alloc: 2362
Sol: 24, Fit: 21862000 Loc: 99, Rest: 1122, Canc: 190, train_ov: 150, Prop. alloc: 2361
Sol: 25, Fit: 21786000 Loc: 94, Rest: 1136, Canc: 190, train_ov: 142, Prop. alloc: 2366
Sol: 26, Fit: 21845000 Loc: 94, Rest: 1155, Canc: 190, train_ov: 150, Prop. alloc: 2366
Sol: 27, Fit: 21808000 Loc: 97, Rest: 1148, Canc: 190, train_ov: 138, Prop. alloc: 2363
Sol: 28, Fit: 21886000 Loc: 98, Rest: 1146, Canc: 190, train_ov: 152, Prop. alloc: 2362
Sol: 29, Fit: 21908000 Loc: 100, Rest: 1123, Canc: 190, train_ov: 157, Prop. alloc: 2360
