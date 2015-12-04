'''
Created on 14.01.2015

@author: maxdriller
'''
import sys
from Bio import SeqIO

def splitLine(inStream):
    for line in inStream:
        if line.startswith("@SRR866928") | line.startswith("+SRR866928"):
           reads1.write(line)
           reads2.write(line)
        else:
            reads1.write(line[0:100])
            reads1.write("\n")
            reads2.write(line[100:])
           # reads2.write("\n")



if len(sys.argv) < 2:
    print "ERROR - please give filename"
else:
    input_fastq = open(sys.argv[1], "r")
    reads1 = open("splitreads1.fastq", "w")
    reads2 = open("splitreads2.fastq", "w")
    splitLine(input_fastq)
    
    