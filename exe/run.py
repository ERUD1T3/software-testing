import os
from random import randint
import time
import csv
import psutil

def compare(a, b):
    if (cmp(a, b) == 0):
        return 1
    else:
        return 0

def main():

    fields = ['Test Number', 'Generator', 'Value (U)', 'Oracles vs Mariam', 'Oracles vs Josias', 'Oracles Runtime(s)', 'Mariam Runtime(s)', 'Josias Runtime(s)', 'Oracles Memory', 'Mariam Memory', 'Josias Memory']
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
		        count += 1
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

                third_timer = time.time()
                cmd3 = startPath + sampleProgSite + word + ' ' + str(param)
                cmd3 += ' | ' + ' ' + 'python tester.py' + ' ' + word
                var3 = os.popen(cmd3).read()
                thirdRuntime = time.time() - third_timer

                mem_end3 = psutil.virtual_memory().used
                thirdMemory = (mem_end3) / 1024



                row = [count, word, param, compare(var1, var2), compare(var1, var3), oraclesRuntime, myRuntime, thirdRuntime, oraclesMemory, myMemory, thirdMemory]
                csvwriter.writerow(row)

	print("Done, data available at collectedData.csv")

main()
