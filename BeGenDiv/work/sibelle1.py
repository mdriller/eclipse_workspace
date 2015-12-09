'''
Created on 08.12.2015

@author: maxdriller
'''

import os

def doStuff(file):
    for line in file:
        if line.startswith(">"):
            
            splitted  = line.split("\t")
            name = splitted[0]
            seq = splitted[1]
            
            print name, seq 

if __name__ == "__main__":
    
    import argparse    
    
    parser = argparse.ArgumentParser(description="stuff for sibelle")
    parser.add_argument("inFile", help="", type=str)
    #parser.add_argument("outDir", help="directory where output files will be created", type=str)
    args = parser.parse_args()
    
    inFile = open(args.inFile)
    
    doStuff(inFile)
    
    
    
    