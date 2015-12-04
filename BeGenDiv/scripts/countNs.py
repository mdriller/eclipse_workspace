'''
Created on 10.03.2015

@author: maxdriller
'''
import argparse


def checkforNs(stream):
    ncount = 0
    lettercount = 0
    for line in stream:
        if line.startswith(">") == False:
            for char in line:
                lettercount += 1
                if char == "n" or char == "N":
                    ncount += 1
    
    print "seq length: " + str(lettercount)
    print "#Ns: " + str(ncount)
    print "%N: " + str(float(ncount)/float(lettercount))
                

parser = argparse.ArgumentParser(description="checks")
parser.add_argument("input", help="input file")
args = parser.parse_args()

try:
    stream = open(args.input)
except:
    print "Error - unable to open files"
        

