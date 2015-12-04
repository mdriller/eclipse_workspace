'''
Created on 17.02.2015

@author: maxdriller
'''

from Bio import SeqIO
import argparse
import gzip


parser = argparse.ArgumentParser(description="Convert a file to a different format, check for supported formats at: http://biopython.org/wiki/SeqIO")
parser.add_argument("input", help="path and name of input file")
parser.add_argument("infmt", help="format of the inputfile")
parser.add_argument("output", help="name and path to output file")
parser.add_argument("outfmt", help="format for your output file")
parser.add_argument("-g", "--gzip", help="activate if file is zipped", action="store_true")

args = parser.parse_args()

#try:
if args.gzip:
    SeqIO.convert(gzip.open(args.input), args.infmt, args.output, args.outfmt)
else:
    SeqIO.convert(args.input, args.infmt, args.output, args.outfmt)
#except: 
#    print "Error - unable to open file..."