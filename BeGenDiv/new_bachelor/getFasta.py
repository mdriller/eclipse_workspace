'''
Created on 03.02.2016

@author: maxdriller
'''

import argparse
from Bio import SeqIO


parser = argparse.ArgumentParser(description="reverse complement fasta")
parser.add_argument("In", help="path and infile", type=str)
parser.add_argument("id", help="", type=str)
parser.add_argument("out", help="outfile", type=str)

args = parser.parse_args()

fasta = SeqIO.parse(args.In, "fasta")

for seq in fasta:
    print seq.id.split("|")[3]
    if seq.id.split("|")[3] == args.id:
        SeqIO.write(seq, args.out, "fasta")
        print "FOUND IT"
