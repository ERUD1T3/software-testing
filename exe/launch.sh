#!/bin/bash

# File to run tester.py against oracles


USAGE="Usage: $0 nums..."

if [ "$#" == "0" ]; then
    echo "$USAGE"
    exit 1
fi

TESTSITE=code01.fit.edu                      # andrew.cs.fit.edu
TESTPATH=/udrive/student/jmoukpe2016/kgallagher/sampleprogs/
TARGETPATH=/udrive/student/jmoukpe2016/software-test/exe/                               # public_html/sampleprogs/
USER=jmoukpe2016
GENERATORS=(
            func
            reflex
            onetoone
            onto
           )
TARGETS=(
            tester.py
        )

echo generator 
for ((II=0; II < ${#GENERATORS[@]}; ++II)) do
    echo $TESTSITE $TESTPATH${GENERATORS[II]} $1 $2
    ssh $USER $TESTSITE $TESTPATH${GENERATORS[II]} $1 $2
    ##  ssh $TESTSITE $TESTPATH${GENERATORS[II]} $1 $2  |
    /usr/bin/time --verbose  ./${TARGETS[0]} 
done
