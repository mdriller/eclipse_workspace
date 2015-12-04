'''
Created on 03.06.2015

@author: maxdriller
'''

import gzip

instream = gzip.open("/home/maxdriller/Schreibtisch/Praktikum/Bachelor/Choloepus_hoffmanni/raw/SRR857575_1.fastq.gz")

idDict = {}

for line in instream:
    if line.startswith("@SRR"):
        splitted = line.split(" ")
        #print splitted
        id = splitted[1]
        #print id
        
        if idDict.get(id, "missing") == "missing":
            idDict[id] = 1
            
        else:
            print "Found the same read id in two reads: " + id 