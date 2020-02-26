
#!/bin/bash

start_time=`date +%s` #used to get the script runtime

> runtimes.txt #empties the output file so that only new input is written to it

# USAGE="Usage: $0 nums..."
# if [ "$#" == "0" ]; then
#     echo "$USAGE" please enter Username as argument
#     exit 1
# fi

# USER=$1
USER=jmoukpe2016                    #tracks username   
TESTSITE=$USER@code01.fit.edu       #full server site domain 
TESTPATH=kgallagher/sampleprogs/    #path to sample programs
TARGETPATH=kgallagher/oracles/      # path to oracles 

GENERATORS=$(ssh $TESTSITE ls $TESTPATH)
# TARGETS=$(ssh $TESTSITE ls $TARGETPATH)
TARGETS=(
    onto
    onetoone
    reflex
    sym
    trans
    func
    eq
)

echo Server: $TESTSITE

for j in {0..5000..500} 
    do
    for i in $GENERATORS 
        do
        echo ''
	    echo Runs: $TESTPATH$i $j
        # ssh $TESTSITE $TESTPATH$i $j | tee >(/usr/bin/time -o runtimes.txt -a -f 'Target: Elapsed time: %e' ssh $TESTSITE $TARGETPATH$i) >(/usr/bin/time -o runtimes.txt -a -f 'Local: Elapsed time: %e' python3 tester.py) >/dev/null
        ssh $TESTSITE $TESTPATH$i $j | tee >(
            for ((II=0; II < ${#TARGETS[@]}; ++II))
                do
                echo ${TARGETS[II]} &>> runtimes.txt
                /usr/bin/time -o runtimes.txt -a -f 'Oracles Elapsed Time: %e' ssh $TESTSITE $TARGETPATH${TARGETS[II]}
                # sleep .5
            done
            ) >(/usr/bin/time -o runtimes.txt -a -f 'Tester Elapsed Time: %e' python3 tester.py) >/dev/null
        sleep .5
    done
done

echo Total Test Runtime: $(expr `date +%s` - $start_time) s