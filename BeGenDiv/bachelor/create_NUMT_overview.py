'''
Created on 04.09.2015

@author: maxdriller
'''
import argparse
import os
from Bio import SeqIO

#def writeTable():

class scafInfo:
    def __init__(self, sID, sName, sLen, sNs):
            self.id = sID
            self.name = sName
            self.len = sLen
            self.Ns = sNs

def getScafInfo(scafIn, scafDict):
    
    for scaf in scafIn:
        scafName = scaf.description.split(" ")[8].strip(",")[8:]
        sInfo = scafInfo(scaf.id, scafName, len(scaf.seq), scaf.seq.count("N"))
        scafDict[scafName] = sInfo
        #print sInfo.name
        
#def getMergeInfo():
        

parser = argparse.ArgumentParser(description="get info on NUMTs like where they are, %of Scaffoldsize, %mt-genome-size...")
parser.add_argument("blastTab", help="path and name of file of the BLAST tab file(6)", type=str)
parser.add_argument("scafs", help="path and name of fasta file of the scaffolds", type=str)
parser.add_argument("output", help="path and name of outputfile for info on all NUMTs", type=str)
parser.add_argument("--m", "-merge", help="path and name of file which contain info on which numts are merged", type=str)

args = parser.parse_args()
#mt genome size of choloepus Hoffmanni
mtlen_CH = 16474

blaststream = open(args.blastTab)


scafStream = SeqIO.parse(args.scafs, "fasta")
scafDict = {}
#get Info about scafs from file and store it in a dictionary
getScafInfo(scafStream, scafDict)

# if there is a file containing info on numts on a scaf that need to be merged 
if args.m:
    mergeDict = {}

#open output
outstream = open(args.output, "w")
#write header line
outstream.write("#" + "\t" + "ScafId" + "\t" + "length" + "\t" + "orientation" +"\t" + "ScafIndex" + "\t" + "mtIndex" + "\t" + "pIdent_mt" + "\t" + "%numt/scaf" + "\t" + "%numt/mt" + "\n")

counter = 1
for line in blaststream:
    splitted = line.split("\t")
    sId = splitted[12].split(" ")[7].strip(",")[8:]
    
    scafInfo = scafDict[sId]
    #print scafInfo.name
    
    #calculate orientation(forward/reverse)
    if int(splitted[8]) < int(splitted[9]):
        orient = "forward"
    else:
        orient = "reverse"
    # the scafs that only consist of mtDNA and Ns are ignored
    #if sId != "17875" and sId != "260145" and sId != "24324":
    outstream.write(str(counter) + "\t" + sId + "\t" + splitted[3] + "\t" + orient + "\t" + splitted[8] + "-" + splitted[9] + "\t" + splitted[6] + "-" + splitted[7] + "\t" + splitted[2] + "\t" + str(float(splitted[3])/scafInfo.len*100) + "\t" + str(float(splitted[3])/mtlen_CH*100) + "\n")
    counter += 1


     
    
