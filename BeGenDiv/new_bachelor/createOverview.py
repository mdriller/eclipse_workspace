'''
Created on 07.02.2016

@author: maxdriller
'''
import argparse

parser = argparse.ArgumentParser(description="Extract reads from BLASTed Contigs")
parser.add_argument("NUMTinfo", help="path and name of blastfile in tab format", type=str)
parser.add_argument("out", help="path and name of Scaffolds in fasta format", type=str)
parser.add_argument("--l", "-latex", help="creates the table for latex", action="store_true")
args = parser.parse_args()





outwriter = open(args.out, "w")
outwriter.write("ID" + "\t" + "ScafID" + "\t" + "Length" + "\t" + "orientation" + "\t" + "scafIndex" + "\t" + "mtIndex" + "\t" + "identity\n")
for line in open(args.NUMTinfo):
    if not line.startswith("#"):
        print line
        splitted = line.split("\t")
        if int(splitted[3]) < int(splitted[4]):
            ori = "forward"
        else:
            ori = "reverse"
                
        scafI = splitted[3] + "-" + splitted[4]
        mtI = splitted[5] + "-" + splitted[6]   
        outwriter.write(splitted[0]  + "\t" + splitted[1] + "\t" + splitted[2] + "\t" + ori + "\t" + scafI + "\t" + mtI + "\t" + splitted[7] + "\n")
            
outwriter.close()