'''
Created on 23.04.2015

@author: maxdriller
'''

import argparse

parser = argparse.ArgumentParser(description="extract Read from FASTQ read set")
parser.add_argument("readid", help="id of the reads you want extracted")
parser.add_argument("infile", help="path and name of inputfile")
parser.add_argument("outfile", help="path and name of outputfile")
args = parser.parse_args()

fastqstream = open(args.infile)
outstream = open(args.outfile, "w")

rID = args.readid

write = False
seqcount = 1

for line in fastqstream:
    
    if line.startswith(">"):
        splitted = line.split(" ")
        
        readid = splitted[0][1:]
        #print readid
        seqcount += 1
        
        if readid == rID:
            print "FOUND IT"
            write = True
            outstream.write(line)
        else:
            write = False
    else:
        if write == True:
            outstream.write(line)