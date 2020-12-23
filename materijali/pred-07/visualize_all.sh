#! /bin/bash -eu

RESULTS=../pred-06/prosti-brojevi/*.csv

for filename in $RESULTS; do
  poetry run python3 visualize.py $filename
done
