'''
Created on Feb 26, 2016

@author: maxdriller
'''
import argparse


def buildMSdict(msDict, misaPredicts):
    
    for line in misaPredicts:
        id = line.split("\t")[0]
        
        splitted = line.strip("\n").split("\t")
        
        start = splitted[5]
        end = splitted[6]
        ms = splitted[3]
        
        
        if msDict.get(id, "missing") == "missing":
            msDict[id] = [ms, start, end]
            print msDict[id]
    

parser = argparse.ArgumentParser(description="")
parser.add_argument("misaIn", help="misa output --> the <filename>.misa file", type=str)
#parser.add_argument("allele_file", help="clustS file", type=str)
#parser.add_argument("outFile", help="", type=str)

args = parser.parse_args()

microDict = {}

misaParser = open(args.misaIn)

buildMSdict(microDict, misaParser)

