'''
Created on 02.02.2016

@author: maxdriller
'''

from Bio import SeqIO
import argparse
    
parser = argparse.ArgumentParser(description="change the annotation of the numts of phylogenetic analysis")
parser.add_argument("In", help="path and infile", type=str)
parser.add_argument("start", help="start of subseq", type=int)
parser.add_argument("end", help="end of subseq", type=int)
parser.add_argument("out", help="outfile", type=str)

args = parser.parse_args()

fastaseq = SeqIO.read(args.In, "fasta")

fastaseq.seq = fastaseq.seq[args.start:args.end]

SeqIO.write(fastaseq, args.out, "fasta")


