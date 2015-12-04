'''
Created on 26.08.2015

@author: maxdriller
'''

import argparse
import gzip

parser = argparse.ArgumentParser(description="extract Reads from Blast tab output")
parser.add_argument("blasttab", help="path and name of the blasttab output containing the ids of the reads you want extracted")
parser.add_argument("readpool", help="path and name of readpool")
parser.add_argument("output", help="path and name of outputfile")

args = parser.parse_args()

blastIn = open(args.blasttab)
readIn = open(args.readpool)
fastqout = open(args.output, "w")
readdict = {}

for line in blastIn:
    rid = line.split("\t")[1]
    readdict[rid] = 1
    
print "Read-dictionary has been created now looking for reads in readpool."

linecount = 0
seqcount = 1
write = False
for line in readIn:
    
    if linecount == 4:
        linecount = 0
        seqcount += 1
        
    
    
    
    linecount += 1
    
    
    