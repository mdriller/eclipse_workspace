'''
Created on 11.05.2015

@author: maxdriller
'''

from Bio.Alphabet import generic_dna
from Bio.Seq import Seq
from Bio import SeqIO
import argparse
import gzip


parser = argparse.ArgumentParser(description="Convert a file to a different format, check for supported formats at: http://biopython.org/wiki/SeqIO")
parser.add_argument("input", help="path and name of input file containing multiple sequences, which should be assembled to one")
parser.add_argument("format", help="format of the inputfile")
parser.add_argument("out", help="path and name of output file")
parser.add_argument("-g", "--gzip", help="activate if file is zipped", action="store_true")

args = parser.parse_args()

if args.gzip:
    #instream = (args.input)
    print "I'll do that later!!! exiting"
    exit()
else:
    inseqs = SeqIO.parse(args.input, args.format)
    
concatenated = Seq("", generic_dna) 

seqcount = 0
for seq in inseqs:
    seqcount += 1
    concatenated += seq
    
    if seqcount % 100 == 0:
        print seqcount
print seqcount
   
SeqIO.write(concatenated, args.out, "fasta")
    
print "All done " + str(seqcount) + " seqs in " + args.format + "-format merged"
