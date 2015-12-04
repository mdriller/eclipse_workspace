'''
Created on 15.04.2015

@author: maxdriller
'''
import argparse


parser = argparse.ArgumentParser(description="")
parser.add_argument("inblast1", help="")
parser.add_argument("inblast2", help="")
parser.add_argument("out", help="")
args = parser.parse_args()

try:
    blast1 = open(args.inblast1)
    blast2 = open(args.inblast2)
    outstream = open(args.out, "w")
except:
    print "Error - unable to open files"
    exit()

readdict = {}
doubles1 = 0
for line in blast1:
    splitted = line.split("\t")
    id = splitted[0].split("-")[1]

    
    if readdict.get(id, "missing") == "missing":
        readdict[id] = 1
        
    elif readdict.get(id, "missing") == 1:
        print "double id 1"
        doubles1 += 1
    
doubles2 = 0
for line in blast2:
    splitted = line.split("\t")
    id = splitted[0].split("-")[1]

    if readdict.get(id, "missing") == "missing":
        readdict[id] = 2
    elif readdict.get(id, "missing") == 1:
        readdict[id] = 12

    elif readdict.get(id, "missing") == 2 or readdict.get(id, "missing") == 12:
        print "double id 2"
        doubles2 += 1   
        
print "doubles in 1: " + str(doubles1)
print "doubles in 2: " + str(doubles2)
        
for rid in readdict:
    outstream.write(rid + "\t" + str(readdict[rid]) + "\n")
