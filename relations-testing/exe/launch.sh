#!/bin/bash

# File to run tester.py against oracles


USAGE="Usage: $0 nums..."

if [ "$#" == "0" ]; then
    echo "$USAGE"
    exit 1
fi

TESTSITE=code01.fit.edu                      # andrew.cs.fit.edu
TESTPATH=/udrive/faculty/kgallagher/public_html/sampleprogs/                                   # public_html/sampleprogs/

GENERATORS=(
            func
            reflex
            onetoone
            onto
           )
TARGETS=(
            func
            reflex
            onetoone
            onto
        )

echo generator 
for ((II=0; II < ${#GENERATORS[@]}; ++II)) do
    echo $TESTSITE $TESTPATH${GENERATORS[II]} $1 $2
    ssh $TESTSITE $TESTPATH${GENERATORS[II]} $1 $2
    ##  ssh $TESTSITE $TESTPATH${GENERATORS[II]} $1 $2  |
    /usr/bin/time --verbose  ./${TARGETS[II]} 
done
