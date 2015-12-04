'''
Created on 20.03.2015

@author: maxdriller
'''

import argparse


def getReadIDs(instream, idList):
    
    print "Getting ReadIDs from file..."
    
    for line in instream:   
        id = line.strip("\n").split("\t")[0].split("-")[1]
        
        if id not in idList:
            #print id 
            idList.append(id)
    
    print "Done. " + str(len(idList)) + " reads in the list"


def writeReads(instream, idList, outstream, identi): 

    print "Write reads in new file..."
    
    write = False
    countReads = 0
    
    for line in instream:
        
        if line.startswith(identi):
            id = line.split("\t")[0].split("-")[1].split(" ")[0]
            #print id
            
            if id in idList:
                outstream.write(line)
                write = True
                countReads += 1    
            else:
                write = False
        else:
            if write == True:
                outstream.write(line)
    
            
    print "Done. " + str(countReads) + " reads written."

parser = argparse.ArgumentParser(description="extract Reads from Blast tab output")
parser.add_argument("blasttab", help="path and name of the blasttab output containing the ids of the reads you want extracted")
parser.add_argument("readpool", help="path and name of readpool")
parser.add_argument("output", help="path and name of outputfile")
parser.add_argument("identifier", help="identification for each read = string at the beginning of the readID (first line in fastq format for read -> f.e. @M01271:)")

args = parser.parse_args()

print "Starting programm"
    
try:
    readlist = open(args.blasttab)
    readpool = open(args.readpool)
    output = open(args.output, "w")
    idList = []
except:
    print "Error - unable to open files"
    exit(0)
    
getReadIDs(readlist, idList)
writeReads(readpool, idList, output, args.identifier)        