#!/opt/homebrew/bin/bash

python src/unallowed_approach/imp_evol_algo.py | grep -E "Print in calc. fit.: |Penalties for sol: |Loc: |fit_score|START of|END of" > src/unallowed_approach/logs/prints.txt