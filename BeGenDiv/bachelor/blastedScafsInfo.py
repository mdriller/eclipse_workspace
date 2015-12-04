'''
Created on 09.06.2015

@author: maxdriller
'''
import argparse
            
parser = argparse.ArgumentParser(description="Extract reads from BLASTed Contigs")
parser.add_argument("blast6", help="path and name of blastfile in tab format", type=str)
parser.add_argument("output", help="path and name of outputfile(.fasta)", type=str)

args = parser.parse_args()

instream = open(args.blast6)
outstream = open(args.output, "w")

outstream.write("#ScafId" + "\t" + "length" + "\t" + "ScafStart"+ "\t" + "ScafEnd" + "\t" + "mt_Start" + "\t" + "mtEnd" + "\t" + "eval "+ "\t" + "BitScore" + "\t" + "pIdent" + "\n")

for line in instream:
        splitted = line.split("\t")
        sId = splitted[12].split(" ")[7].strip(",")
        outstream.write(sId + "\t" + splitted[3] + "\t" + splitted[8] + "\t" + splitted[9] + "\t" + splitted[6] + "\t" + splitted[7] + "\t" + splitted[10] + "\t" + splitted[11] + "\t" + splitted[2] + "\n")
