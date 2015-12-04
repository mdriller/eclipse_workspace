'''
Created on 09.06.2015

@author: maxdriller
'''

import argparse


def getScafIds(blaststream, ScafDict):
    
    for line in blaststream:
        splitted = line.split("\t")
        sId = splitted[12].split(" ")[7].strip(",")
        #print sId
        
        if ScafDict.get(sId, "missing") == "missing":
            ScafDict[sId] = 1
        
def extractScafs(scafstream, ScafDict, outstream):
    
    write = False
    for line in scafstream:
        if line.startswith(">"):
            splitted = line.split(" ")
            sId = splitted[8].strip(",")
            
            if ScafDict.get(sId, "missing") == 1:
                print "found Scaf"
                write = True
                outstream.write(line)
            elif ScafDict.get(sId, "missing") == "missing":
                write = False
                
        elif write == True:
            outstream.write(line)
            
            
parser = argparse.ArgumentParser(description="Extract reads from BLASTed Contigs")
parser.add_argument("blast6", help="path and name of blastfile in tab format", type=str)
parser.add_argument("ScafFasta", help="path and name of file containing the scaffolds in fasta format", type=str)
parser.add_argument("output", help="path and name of outputfile(.fasta)", type=str)

args = parser.parse_args()

blastIn = open(args.blast6)
scafIn = open(args.ScafFasta)
scafOut = open(args.output, "w")


ScafIds = {}

getScafIds(blastIn, ScafIds)

print str(len(ScafIds)) + " Scaffolds in Scaffold List"
extractScafs(scafIn, ScafIds, scafOut)
print "all done"