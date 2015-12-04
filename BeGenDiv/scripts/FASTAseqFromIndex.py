'''
Created on 15.04.2015

@author: maxdriller
'''

from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser(description="this script will write a seq from a certain point")
parser.add_argument("input", help="path and name of input file")
parser.add_argument("out", help="")
parser.add_argument("index", help="point from where the seq should e written if = 0 wholeseq will be written", type=int)
args = parser.parse_args()

fastaseq = SeqIO.read(args.input, "fasta")
print fastaseq.seq[args.index:]
SeqIO.write(fastaseq[args.index:], args.out, "fasta")