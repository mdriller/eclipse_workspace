'''
Created on 16.01.2016

@author: maxdriller
'''

import argparse    
from Bio import SeqIO

parser = argparse.ArgumentParser(description="extracts contogs not in scafs from assembly statistic & fasta contig file")
parser.add_argument("asmStat", help="assembly statistic", type=str)
parser.add_argument("contigs", help="contigs in fasta", type=str)
parser.add_argument("outFile", help="", type=str)

args = parser.parse_args()

outWriter = open(args.outFile, "w")

contDict = {}
for line in open(args.asmStat):
    if not line.startswith("#"):
        scafId = line.split("\t")[4]
        contDict[scafId] = 1


for contig in SeqIO.parse(args.contigs, "fasta"):
    scafId = contig.id.split("|")[3]
    
    if contDict.get(scafId, "missing") != "missing":
        SeqIO.write(contig, outWriter, "fasta")

     
outWriter.close()
