
#!/bin/bash

start_time=`date +%s` #used to get the script runtime

# clears runtime files
> runtimes.txt 

USER=jmoukpe2016                    #tracks username   
TESTSITE=$USER@code01.fit.edu       #full server site domain 
TESTPATH=kgallagher/sampleprogs/    #path to sample programs
TARGETPATH=kgallagher/oracles/      # path to oracles 

GENERATORS=$(ssh $TESTSITE ls $TESTPATH)
# TARGETS=$(ssh $TESTSITE ls $TARGETPATH)

# target oracles to test against
TARGETS=(
    onto
    onetoone
    reflex
    sym
    trans
    func
    eq
)

# display testsite
echo Server: $TESTSITE

# run test args for progs
for j in {0..5000..500} 
    do

    # looping through all the sample progs
    for i in $GENERATORS 
        do
        echo ''
	    echo Runs: $TESTPATH$i $j

        # run sample progs then pipe their output to oracles, then to tester.py program
            ssh $TESTSITE $TESTPATH$i $j | tee >(
                /usr/bin/time --quiet -o runtimes.txt -a -f 'Oracles Onto runtime: %e' ssh $TESTSITE $TARGETPATH${TARGETS[0]}
            ) >(
                /usr/bin/time --quiet -o runtimes.txt -a -f 'Oracles Onetoone runtime: %e' ssh $TESTSITE $TARGETPATH${TARGETS[1]}
            ) >(
                /usr/bin/time --quiet -o runtimes.txt -a -f 'Oracles Reflex runtime: %e' ssh $TESTSITE $TARGETPATH${TARGETS[2]}
            ) >(
                /usr/bin/time --quiet -o runtimes.txt -a -f 'Oracles Sym runtime: %e' ssh $TESTSITE $TARGETPATH${TARGETS[3]}
            ) >(
                /usr/bin/time --quiet -o runtimes.txt -a -f 'Oracles Trans runtime: %e' ssh $TESTSITE $TARGETPATH${TARGETS[4]}
            ) >(
                /usr/bin/time --quiet -o runtimes.txt -a -f 'Oracles Func runtime: %e' ssh $TESTSITE $TARGETPATH${TARGETS[5]}
            ) >(
                /usr/bin/time --quiet -o runtimes.txt -a -f 'Oracles Eq runtime: %e' ssh $TESTSITE $TARGETPATH${TARGETS[6]}
            ) >(
                /usr/bin/time --quiet -o runtimes.txt -a -f 'Tester runtime: %e' python3 tester.py
            ) >/dev/null
        sleep .5
    done
done

# total runtime of test
echo Total Test Runtime: $(expr `date +%s` - $start_time) s