'''
Created on 13.05.2015

@author: maxdriller
'''

import argparse
import gzip

parser = argparse.ArgumentParser(description="Extract reads from BLASTed Contigs")
parser.add_argument("R1ScaffoldList", help="path and name of file containing the id of one scaffold to be extracted per line", type=str)
parser.add_argument("R2ScaffoldList", help="path and name of file containing the id of one scaffold to be extracted per line", type=str)
parser.add_argument("ScafFasta", help="path and name of file containing the scaffolds in fasta format", type=str)
parser.add_argument("output", help="path and name of outputfile(.fasta)", type=str)

args = parser.parse_args()


scafIDstreamR1 = open(args.R1ScaffoldList)
scafIDstreamR2 = open(args.R2ScaffoldList)
fastastream = open(args.ScafFasta)
outstream = open(args.output, "w")


scafList = []

for line in scafIDstreamR2:
    if not line.startswith("#"):
        splitted = line.split("\t")
        if int(splitted[1]) > 100:
            scafList.append(splitted[0])

for line in scafIDstreamR1:
    if not line.startswith("#"):
        splitted = line.split("\t")
        if int(splitted[1]) > 100:
            if not splitted[0] in scafList:
                scafList.append(splitted[0])
 
print "ScafList created, containing " + str(len(scafList)) + " scaffold-IDs"


write = False
for line in fastastream:
    if line.startswith(">"):
        splitted = line.split(",")
        scafID = splitted[0].split(" ")[8][8:]
        #print scafID
        if scafID in scafList:
            outstream.write(line)
            write = True
        else:
            write = False
    else:
        if write == True:
            outstream.write(line)