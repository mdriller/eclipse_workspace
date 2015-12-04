'''
Created on 13.05.2015

@author: maxdriller
'''

import argparse
import gzip

parser = argparse.ArgumentParser(description="Extract reads from BLASTed Contigs")
parser.add_argument("dirpath", help="", type=str)
parser.add_argument("output", help="", type=str)
parser.add_argument("-g", "--gzip", help="activate if file is zipped", action="store_true")
args = parser.parse_args()

if args.gzip:
    infile = gzip.open(args.dirpath)
else:
    infile = open(args.dirpath)
writer = open(args.output, "ab+")

for line in infile:
    writer.write(line)