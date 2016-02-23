'''
Created on 19.01.2016

@author: maxdriller
'''

import argparse

parser = argparse.ArgumentParser(description="Extract reads from BLASTed Contigs")
parser.add_argument("ScafInfo", help="path and name of scaf info file (script: 3_getScafInfo)", type=str)
parser.add_argument("NUMTsInfo", help="path and name of modified blast6 Info file in tab format(script: 1_blastedScafsInfo)", type=str)
parser.add_argument("output", help="path and name of outputfile(=filtered NUMTsInfo)", type=str)
parser.add_argument("--bad", "-badout", help="optional creates an output file for the NUMTs on the bad scaffolds", action="store_true")

args = parser.parse_args()

scafInfo = open(args.ScafInfo)
badScafs = {}

for line in scafInfo:
    if not line.startswith("#"):
        splitted = line.split("\t")
        scafID = splitted[0].split(" ")[0]
        if len(splitted) == 7:
            
            badScafs[scafID] = splitted[6]
            
            
scafInfo.close()


numtInfo = open(args.NUMTsInfo)
outwriter = open(args.output, "w")

if args.bad:
    badwriter = open(args.bad, "w")

for line in numtInfo:
    if not line.startswith("#"):
        splitted = line.split("\t")
        scafID = splitted[0]
        
        # scaf not in list --> scaf good write hit down
        if badScafs.get(scafID, "missing") == "missing":
            outwriter.write(line)
        else:
            if args.bad:
                badwriter.write(line)
            
        
        
            