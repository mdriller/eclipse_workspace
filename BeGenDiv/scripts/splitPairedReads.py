'''
Created on 06.02.2015

@author: maxdriller
'''


import argparse

def splitReads(instream, out1, out2):
    
    count = 0
    curoutstr = 0

    
    for line in instream:
        if line.startswith("@SRR857604"):
            id = line.split(" ")[0].split("/")[1]
            
            print id
            
            if id == '1':
                outstr1.write(line)
                count = 3
                curoutstr = 1
            else:
                outstr2.write(line)
                count = 3
                curoutstr = 2            
            
        else:
            if count > 0:
                if curoutstr == 1:
                    outstr1.write(line)
                    count -= 1
                else:
                    outstr2.write(line)
                    count -= 1



parser = argparse.ArgumentParser(description="split Paired-end Reads in 2 files")
parser.add_argument("inputfile", help="path to input-file with both paired end reads", type=str)
parser.add_argument("out1", help="path and name of the 1. outputfile with /1 reads", type=str)
parser.add_argument("out2", help="path and name of the 1. outputfile with /2 reads", type=str)

args = parser.parse_args()                    
                    
                    


instream = open(args.inputfile, "r")

outstr1 = open(args.out1, "w")

outstr2 = open(args.out2, "w")

splitReads(instream, outstr1, outstr2)

instream.close()
outstr1.close()
outstr2.close()
