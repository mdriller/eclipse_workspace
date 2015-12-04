'''
Created on 25.08.2015

@author: maxdriller
'''
import argparse
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

parser = argparse.ArgumentParser(description="extract subsseqs from fasta files, subseqs must be described in a tab seperated info file")
parser.add_argument("fastaIn", help="path and name of file containing the scaffolds with numts in fasta format", type=str)
parser.add_argument("fastaOut", help="file containing the Scaffold name and indices of the subseq that needs to be extracted")
parser.add_argument("threshNs", help="threshold for max. amount of Ns in seq all seqs with more Ns will be discarded", type=int, default=30)
args = parser.parse_args()


output = open(args.fastaOut, "w")
threshold = args.threshNs

with open(args.fastaIn, "rU") as fastA:
    for rec in SeqIO.parse(fastA, "fasta"):
        n_count = rec.seq.upper().count("N")
        
        if n_count <= threshold:
            SeqIO.write(rec, output, "fasta")
        