'''
Created on 25.02.2015

@author: maxdriller
'''

import argparse
import gzip

def mergeReads(instreamR1, instreamR2, outstream):
    for line in instreamR1:
        if change == True:
            if line.startswith("@SRR857575") or line.startswith("+SRR857575"):
                splitted = line.split(" ")
                outstream.write(splitted[0] + "/1 " +splitted[1] +  "/1 " + splitted[2])
                #line = line.replace(".1 ", "/1 ")
                #outstream.write(line)
            else:
                outstream.write(line)
        else:
            outstream.write(line)
    for line in instreamR2:
        if change == True:
            if line.startswith("@SRR857575") or line.startswith("+SRR857575"):
                splitted = line.split(" ")
                outstream.write(splitted[0] + "/2 " + splitted[1] +  "/2 " +splitted[2])
                #line = line.replace(".2 ", "/2 ")
                #outstream.write(line)
            else:
                outstream.write(line)
        else:
            outstream.write(line)
        
        
parser = argparse.ArgumentParser(description="Extract reads from BLASTed Contigs")
parser.add_argument("readsR1", help="path to read-file(forward) in FASTQ-format", type=str)
parser.add_argument("readsR2", help="path to read-file(reversed) in FASTQ-format", type=str)
parser.add_argument("output", help="path and name of outputfile(.fastq)", type=str)
parser.add_argument("-g", "--gzip", help="activate if file is zipped", action="store_true")
parser.add_argument("-ca", "--changeanno", help="changes readnames to /1 /2 for paired end", action="store_true")

args = parser.parse_args()

try:
    if args.gzip:
        r1stream = gzip.open(args.readsR1)
        r2stream = gzip.open(args.readsR2)
    else:
        r1stream = open(args.readsR1)
        r2stream = open(args.readsR2)
    outstr = open(args.output, "w")
except:
    print "Error - unable to open files"
    
if args.changeanno:
    change = True
else:
    change = False

mergeReads(r1stream, r2stream, outstr)

r1stream.close()
r2stream.close()
outstr.close()