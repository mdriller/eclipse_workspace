'''
Created on 27.05.2015

@author: maxdriller
'''

import argparse
import gzip


def filterBlastTab(blastIn, col, thresh, IdDict):
    for line in blastIn:
        splitted = line.split("\t")
        
        readID = splitted[0]
        bitscore = float(splitted[col])
        
        if bitscore >= thresh:
            IdDict[readID] = 1
 
 
            
def extractReads(IdDict, readsIn, outfile):
    
    write = False
    
    for line in readsIn:  
        if line.startswith("@"):
            rID = line[1:].strip()
            
            if IdDict.get(rID, "missing") == 1:
                #print "FOUND IT!!!"
                outfile.write(line)
                write = True
            else:
                write = False
        
        else:
            if write == True:
                outfile.write(line)

parser = argparse.ArgumentParser(description="Extract reads from BLASTed Contigs via bitscore", epilog="return reads in fasta/fastq format")
parser.add_argument("bIn", help="path and name of Blast tabular output", type=str)
parser.add_argument("threshold", help="threshold for Bitscore values >= read will be extracted", type=int)
parser.add_argument("reads", help="path and name of readfile in fastq-format", type=str)
parser.add_argument("out", help="path and name of outputfile in fastq-format", type=str)
parser.add_argument("-col", help="change the column of the bitScore not necessary if standard tab format (=6)", type=int, default=11)
parser.add_argument("-fa", help="enable if readfile is in fasta format, default is fastq", type=str)
parser.add_argument("--gz", help="activate if readfile is zipped", action="store_true")
parser.add_argument("--lower", help="activate if you want to extract reads with a Bitscore LOWER than the threashold", action="store_true")
args = parser.parse_args()

blastStream = open(args.bIn)
threshold = args.threshold
column = args.col

if args.gz:
    readStream = gzip.open(args.reads)
else:   
    readStream = open(args.reads)

outstream = open(args.out, "w")

geneDict = {}
filterBlastTab(blastStream, column, threshold, geneDict)

print str(len(geneDict)) + " Reads fit the threshold and will be extracted..."
extractReads(geneDict, readStream, outstream)