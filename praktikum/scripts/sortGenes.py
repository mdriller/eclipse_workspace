'''
Created on 23.03.2015

@author: maxdriller
'''


stream = open("/home/maxdriller/Schreibtisch/0.5/ethanol_genenames.bed")
stream2 = open("/home/maxdriller/Schreibtisch/0.5/ethanol_final.bed", "w")

for line in stream:
    splitted = line.split("\t")
    
    if splitted[14].split("_")[0] == "NM":
        stream2.write(line)

    