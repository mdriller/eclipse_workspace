'''
Created on Mar 2, 2016

@author: maxdriller
'''

import argparse

parser = argparse.ArgumentParser(description="")
parser.add_argument("combFile", help="", type=str)
parser.add_argument("fastaOut", help="", type=str)

args = parser.parse_args()


outWriter = open(args.fastaOut, "w")


seqcount = 0 
clustcount = 1

for line in open(args.combFile):
    line = line.upper()
            

        
    if line.startswith(">"):
        
        id = line.split(" ")[0] + "_" + str(clustcount)
        seq = line.split(" ")[-1]
        outWriter.write(id + "\n")
        outWriter.write(seq)       
        
        
        seqcount += 1
        if seqcount == 2:
            clustcount += 1
            seqcount = 0
            
            

        
outWriter.close()
        
