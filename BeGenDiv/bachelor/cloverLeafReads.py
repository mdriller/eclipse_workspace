'''
Created on 01.09.2015

@author: maxdriller
'''

import argparse
import gzip
from Bio import SeqIO

parser = argparse.ArgumentParser(description="get paired end fastq readfiles in cloverleaf format")
parser.add_argument("forwardR", help="", type=str)
parser.add_argument("reverseR", help="", type=str)
parser.add_argument("output", help="name of output file", type=str)

args = parser.parse_args()

if args.forwardR.endswith(".gz"):
    r1In = gzip.open(args.forwardR)
    r2In = gzip.open(args.reverseR)
else:
    r1In = open(args.forwardR)
    r2In = open(args.reverseR)
  
outwriter = open(args.output, "w")

seqcount = 1
linecount = 0
r1_line0_store = ""
r1_line1_store = ""
r1_line2_store = ""
r2_line0_store = ""
r2_line1_store = ""
r2_line2_store = ""

for line in r1In:
    line2 = r2In.readline()
    
    if linecount == 4:
        linecount = 0
        seqcount += 1
        
    if linecount == 0:
        r1_line0_store = line
        r2_line0_store = line2
        
    elif linecount == 1:
        r1_line1_store = line
        r2_line1_store = line2
        
    elif linecount == 2:
        r1_line2_store = line
        r2_line2_store = line2
        
    elif linecount == 3:
        outwriter.write(r1_line0_store)
        outwriter.write(r1_line1_store) 
        outwriter.write(r1_line2_store) 
        outwriter.write(line) 
        
        outwriter.write(r2_line0_store)
        outwriter.write(r2_line1_store) 
        outwriter.write(r2_line2_store) 
        outwriter.write(line2)
        
        
    linecount += 1