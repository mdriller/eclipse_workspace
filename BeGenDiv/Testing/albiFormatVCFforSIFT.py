'''
Created on 23.02.2015

@author: maxdriller
'''

import argparse

def orderFile(instream, oustream):
    for line in instream:
        a0, a1, a2, a3, a4, a5, a6, a7, a8, a9 = line.split("\t")
        #a0 = a0.strip("chr")
        
        #oustream.write(a0 + "," + a1 + "," + "1," + a3 + "/" + a4 + "\n")
        oustream.write(a0 + ":" + a1 + "\t" + a3 + "/" + a4 + "\n")
        

parser = argparse.ArgumentParser(description="order file for albi")
parser.add_argument("input", help="name and path of input file")
parser.add_argument("output", help="name and path of output file")
args = parser.parse_args()


try:
    stream = open(args.input)
    oustr = open(args.output, "w")
except:
    print "Error - unable to open files"

orderFile(stream, oustr)