'''
Created on 09.03.2015

@author: maxdriller
'''
import argparse

def editFile(instream, outstream):
    
    for line in instream:
        chrom = line.split("\t")[0]
        genename = line.split("\t")[3]
        id = line.split("\t")[5]
        if id == "-":
            start1 = int(line.split("\t")[2]) - 1000
            start2 = start1 + 2000
        else:
            start1 = int(line.split("\t")[1]) - 1000
            start2 = start1 + 2000
        hae = line.split("\t")[9]
      
        
        if genename.startswith("NM"):
            outstream.write(chrom + "\t" + str(start1) + "\t" + str(start2)  + "\t" + genename + "\t" + hae + "\t" + id +"\n")
            
parser = argparse.ArgumentParser(description="edit file for ANNOTATE(tRap)")
parser.add_argument("input", help="path and name of input file")
parser.add_argument("output", help="path and name of output file")
args = parser.parse_args()

try:
    stream1 = open(args.input)
    outstr = open(args.output, "w")
except:
    print "Error - unable to open files"

editFile(stream1, outstr)