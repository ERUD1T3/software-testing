tester: 
	g++ -Wall -o ./bin/tester main.cpp \
						packages/utils.test.cpp \
						packages/func.test.cpp \
						packages/one2one.test.cpp \
						packages/onto.test.cpp \
						packages/reflex.test.cpp \
						packages/symm.test.cpp \
						packages/trans.test.cpp 

run:	tester
	./bin/tester

clean: tester
	rm ./bin/tester



