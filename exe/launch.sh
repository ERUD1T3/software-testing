
#!/bin/bash

start_time=`date +%s` #used to get the script runtime

> output #empties the output file so that only new input is written to it

USAGE="Usage: $0 nums..."
if [ "$#" == "0" ]; then
    echo "$USAGE" please enter Username and arguments
    exit 1
fi

USER=$1
TESTSITE=$USER@code01.fit.edu 
TESTPATH=kgallagher/sampleprogs/
TARGETPATH=kgallagher/oracles/

GENERATORS=$(ssh $TESTSITE ls $TESTPATH)
TARGETS=$(ssh $TESTSITE ls $TARGETPATH)


for i in $GENERATORS
do
    for j in {0..5000..500}
    do
        sleep 1
        echo''
        echo $TESTSITE $TESTPATH$i $j
	      echo $TESTPATH$i $j
        ssh $TESTSITE $TESTPATH$i $j | tee >(/usr/bin/time -o output -a -f 'Target process info:\nElapsed time: %e, Memory use(KB): %K, Process Size(KB): %t' ssh $TESTSITE $TARGETPATH$i) >(/usr/bin/time -o output -a -f 'Local Process info:\nElapsed time: %e, Memory Use(KB): %K, Process Size(KB): %t' python3 tester.py) >/dev/null
        sleep 1
        echo''
    done
done

echo script total runtime is $(expr `date +%s` - $start_time) s