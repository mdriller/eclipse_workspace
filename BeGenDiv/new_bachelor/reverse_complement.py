'''
Created on 02.02.2016

@author: maxdriller
'''
from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser(description="reverse complement fasta")
parser.add_argument("In", help="path and infile", type=str)
parser.add_argument("out", help="outfile", type=str)

args = parser.parse_args()

inFasta = SeqIO.read(args.In, "fasta")

inFasta.seq = inFasta.seq.reverse_complement()

SeqIO.write(inFasta, args.out, "fasta")