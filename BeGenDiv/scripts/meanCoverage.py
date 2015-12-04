'''
Created on 27.02.2015

@author: maxdriller
'''

import argparse
from Bio import SeqIO

def getRefLength(refstream):
    
    for seq in refstream:
        reflen= len(seq)
        
    return reflen

def calcMeanCoverage(instream, reflen):
    whole_cover = 0
    
    for line in instream:
        whole_cover += (float)(line.split("\t")[2])
    
    print "SummedCoverage: " + str(whole_cover)  
    print "AverageCoverage: " + str(whole_cover/reflen)
    print "length of the sequence: " + str(reflen)
    
parser = argparse.ArgumentParser(description="reads samtools depth output and calculates the mean coverage")  
parser.add_argument("input", help="name and path to samtools depth output")
parser.add_argument("refSeq", help="name and path to reference-genome to calculate the length || if you activate the -i option you just give the length of the sequence")
parser.add_argument("-i", "--int", help="activate if you know the length of the genome/sequence you mapped against - then just give a number instead of the reference-genome", action="store_true")
args = parser.parse_args()

try:
    stream = open(args.input)
    refstream = SeqIO.parse(args.refSeq, "fasta")
    reflen = len()
except:
    print "Error -unable to open file"

if args.int:  
    reflength = int(args.refSeq)
else:
    reflength = getRefLength(refstream)
    
calcMeanCoverage(stream, reflength)