'''
Created on 26.03.2015

@author: maxdriller
'''
import argparse


def getGeneNames(instream, genelist):
    for line in instream:
            splitted = line.split("\n")
            genelist.appen


parser = argparse.ArgumentParser(description="edit file for ANNOTATE(tRap)")
parser.add_argument("tRAPinput", help="path and name of input file from tRAP")
parser.add_argument("annotationIn", help="path and name of annotation input file")
parser.add_argument("output", help="path and name of output file")
args = parser.parse_args()

try:
    instream = open(args.tRAPinput)
    instream2 = open(args.annotationIn)
    output = open(args.output)
    
except:
    print "Error - unable to open files"
    
