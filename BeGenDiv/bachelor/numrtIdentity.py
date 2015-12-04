'''
Created on 02.11.2015

@author: maxdriller
'''
# script reads out blast6 output of numt_to_numt blasting and creates an table identity overview

import argparse

parser = argparse.ArgumentParser(description="")
parser.add_argument("blast6", help="", type=str)
parser.add_argument("outfile", help="", type=str)

args = parser.parse_args()

blastIn = open(args.blast6)
outfile = open(args.outfile, "w")

outfile.write("\t")
for i in range(1,76):
    numt = "numt" + str(i)
    outfile.write(numt + "\t") 
outfile.write("\n")

for i in range(1,76):
    numt = "numt" + str(i)
    outfile.write(numt + "\t")
    
    ilist = [0]*75
    
    blastIn = open(args.blast6)
    for line in blastIn:
        cur_numt = line.split("\t")[0].split("_")[0]
        if cur_numt == numt:
            print "FOUND IT"
            other_numt = line.split("\t")[1].split("_")[0]
            idx = int(other_numt[4:])
            ilist[idx-1] = line.split("\t")[2]
    
    for i in ilist:             
        outfile.write(str(i) + "\t")    
    outfile.write("\n")
    blastIn.close()
    