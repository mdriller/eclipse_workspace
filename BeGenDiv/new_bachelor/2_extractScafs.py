'''
Created on 09.06.2015

@author: maxdriller
'''

import argparse


def getScafIds(blastInfostream, ScafDict):
    
    for line in blastInfostream:
        if not line.startswith("#"):
            splitted = line.split("\t")
            sId = splitted[1]
            #print sId
            
            if ScafDict.get(sId, "missing") == "missing":
                ScafDict[sId] = splitted[0]
        
def extractScafs(scafstream, ScafDict, outstream):
    
    write = False
    for line in scafstream:
        if line.startswith(">"):
            splitted = line.split("|")
            sId = splitted[3].split(".")[0]
            
            if ScafDict.get(sId, "missing") != "missing":
                #print "found Scaf"
                
                write = True
                outstream.write(line.strip("\n") + " -" + ScafDict[sId] + "\n")
                
                ScafDict.pop(sId)

            elif ScafDict.get(sId, "missing") == "missing":
                write = False
                
        elif write == True:
            outstream.write(line)
            
            
parser = argparse.ArgumentParser(description="Extract reads from BLASTed Contigs")
parser.add_argument("blast6Info", help="path and name of modified blast6 Info file in tab format(script 1_blastedScafsInfo)", type=str)
parser.add_argument("ScafFasta", help="path and name of file containing the scaffolds in fasta format", type=str)
parser.add_argument("output", help="path and name of outputfile(.fasta)", type=str)

args = parser.parse_args()

blastIn = open(args.blast6Info)
scafIn = open(args.ScafFasta)
scafOut = open(args.output, "w")


ScafIds = {}

getScafIds(blastIn, ScafIds)

print str(len(ScafIds)) + " Scaffolds in Scaffold List"
extractScafs(scafIn, ScafIds, scafOut)
print str(len(ScafIds)) + " Scaffolds left in Scaffold List"
print "all done"