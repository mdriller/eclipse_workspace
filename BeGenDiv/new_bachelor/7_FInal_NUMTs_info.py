'''
Created on 30.01.2016

@author: maxdriller
'''

import argparse

parser = argparse.ArgumentParser(description="Extract reads from BLASTed Contigs")
parser.add_argument("NUMTinfo", help="path and name of blastfile in tab format", type=str)
parser.add_argument("out", help="path and name of Scaffolds in fasta format", type=str)
parser.add_argument("--l", "-latex", help="creates the table for latex", action="store_true")
args = parser.parse_args()





if args.l:
    outwriter = open(args.out, "w")
    outwriter.write("ID" + "\t" + "ScafID" + "\t" + "Length" + "\t" + "orientation" + "\t" + "scafIndex" + "\t" + "mtIndex" + "\t" + "identity\n")
    for line in open(args.NUMTinfo):
        if not line.startswith("#"):
            splitted = line.split("\t")
            if int(splitted[4]) < int(splitted[5]):
                ori = "forward"
            else:
                ori = "reverse"
                
            scafI = splitted[4] + "-" + splitted[5]
            mtI = splitted[6] + "-" + splitted[7]   
            outwriter.write(splitted[0]  + "\t" + splitted[2]  + "\t" + splitted[3] + "\t" + ori + "\t" + scafI + "\t" + mtI + "\t" + splitted[10] + "\n")
            
    outwriter.close()
    
else:
    outwriter = open(args.out, "w")

    for line in open(args.NUMTinfo):
        if not line.startswith("#"):
            splitted = line.split("\t")
            if int(splitted[4]) < int(splitted[5]):
                ori = "forward"
            else:
                ori = "reverse"
            outwriter.write(line.strip("\n") + "\t" + ori + "\n")
            
    outwriter.close()