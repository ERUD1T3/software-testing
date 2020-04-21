import os
from random import randint
import time
import csv
import psutil

def compare(var1, var2):
    if (cmp(var1, var2) == 0):
        return 1
    else:
        return 0

def main():

    fields = ['Test Number', 'Generator', 'Value (U)', 'Oracles Runtime(s)', 'My Runtime(s)', 'Test Accuracy', 'Oracles Memory', 'My Memory']
    filename = "collectedData.csv"

    startPath = '/udrive/faculty/kgallagher/public_html/'
    sampleProgSite = 'sampleprogs/'
    oraclesSite = 'oracles/'

    Generators = ["func", "reflex", "onetoone", "onto"]


    print("Collecting Data...")
    with open(filename, 'w') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(fields)

        count = 0
        while count < 100:
            for word in Generators:
		        count = count + 1
                param = randint(1, 200)

                first_timer = time.time()
                cmd1 = startPath + sampleProgSite + word + ' ' + str(param)
                cmd1 += ' | ' + startPath + oraclesSite + word
		        var1 = os.popen(cmd1).read()

                oraclesRuntime = time.time() - first_timer

                mem_end1 = psutil.virtual_memory().used

		        oraclesMemory = (mem_end1) / 1024

                second_timer = time.time()
                cmd2 = startPath + sampleProgSite + word + ' ' + str(param)
                cmd2 += ' | ' + ' ' + './main' + ' ' + word
                var2 = os.popen(cmd2).read()

                myRuntime = time.time() - second_timer

                mem_end2 = psutil.virtual_memory().used
		        myMemory = (mem_end2) / 1024

                row = [count, word, param, oraclesRuntime, myRuntime, compare(var1, var2), oraclesMemory, myMemory]
                csvwriter.writerow(row)

	print("Done, data available at collectedData.csv")

main()
