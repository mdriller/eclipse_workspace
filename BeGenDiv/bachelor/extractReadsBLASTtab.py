'''
Created on 26.08.2015

@author: maxdriller
'''

import argparse
import gzip
from Bio import SeqIO

parser = argparse.ArgumentParser(description="extract Reads from Blast tab output")
parser.add_argument("blasttab", help="path and name of the blasttab output containing the ids of the reads you want extracted")
parser.add_argument("readpool", help="path and name of readpool")
parser.add_argument("output", help="path and name of outputfile")

args = parser.parse_args()

blastIn = open(args.blasttab)
fastqout = open(args.output, "w")
readdict = {}

for line in blastIn:
    rid = line.split("\t")[1]
    readdict[rid] = 1
    
print "Read-dictionary has been created now looking for reads in readpool."

if args.readpool.endswith(".gz"):
    with gzip.open(args.readpool, "rU") as fastQ:
        for rec in SeqIO.parse(fastQ, "fastq"):
            if readdict.get(rec.id, "missing") != "missing":
                SeqIO.write(rec, fastqout, "fastq")
        
else:
    with open(args.readpool, "rU") as fastQ:
        for rec in SeqIO.parse(fastQ, "fastq"):
            if readdict.get(rec.id, "missing") != "missing":
                SeqIO.write(rec, fastqout, "fastq")

print "All done!"
