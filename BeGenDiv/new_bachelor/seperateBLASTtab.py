'''
Created on 04.02.2016

@author: maxdriller
'''

import argparse
import os

parser = argparse.ArgumentParser(description="seperate BLAST tab by queries")
parser.add_argument("inFile", help="path and infile (blast tab)", type=str)
parser.add_argument("outPath", help="outpath", type=str)

args = parser.parse_args()

oldname =""
write = False
for line in open(args.inFile):
    name = line.split("\t")[0]
    
    if name != oldname:
        if write == True:
            outwriter.close()
        
        filename = args.outPath + "/" + name + ".blast6"
          
        outwriter = open(filename, "w")
        outwriter.write(line)
        write = True
        
    else:
        outwriter.write(line)
    oldname = name
    
    
    