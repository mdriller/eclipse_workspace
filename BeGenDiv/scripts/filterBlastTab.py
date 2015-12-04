'''
Created on 25.03.2015

@author: maxdriller
'''
import argparse

def filterPvalue(instream, outstr):
    for line in instream:
        
        if line.startswith("#") == False:
            splitted = line.split("\t")
            if splitted[10] != "0.0":
                #pid = int(splitted[10].split("-")[1])
                pid = float(splitted[colnr])
                if pid < thresh:
                    print splitted[0] + " "+ str(pid)
                    outstr.write(line)
                
        
parser = argparse.ArgumentParser(description="extract Reads from Blast tab output, filtered by the pvalue of each seq")
parser.add_argument("blasttab", help="path and name of the blasttab output containing the ids of the reads you want extracted")
parser.add_argument("column", help="the column for which you want to filter", type=int)
parser.add_argument("threshold", help="threshold for column while filtering (only takes values smaller than threshold)", type=int)
parser.add_argument("output", help="path and name of outputfile")
args = parser.parse_args()


blaststream = open(args.blasttab)
outstream = open(args.output, "w")
colnr = args.column
thresh = args.threshold


filterPvalue(blaststream, outstream)
    
blaststream.close()
outstream.close()




