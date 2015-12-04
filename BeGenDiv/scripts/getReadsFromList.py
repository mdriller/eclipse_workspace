'''
Created on 20.02.2015

@author: maxdriller
'''

import argparse

def getReadIDs(instream, idList):
    
    if args.info:
        print "Getting ReadIDs from file..."
    
    for line in instream:
        
        id = line.split("-")[1].split(" ")[0]
        
        if id not in idList:
            
            idList.append(id)
    
    if args.info:
        print "Done. " + str(len(idList)) + " reads in the list"


def writeReads(instream, idList, outstream):
    
    if args.info:
        print "Write reads in new file..."
    
    write = False
    countReads = 0
    
    for line in instream:
        
        if line.startswith(">"):
            id = line.split("-")[1].split(" ")[0]
            
            if id in idList:
                outstream.write(line)
                write = True
                countReads += 1    
            else:
                write = False
        else:
            if write == True:
                outstream.write(line)
    
    if args.info:            
        print "Done. "+ str(countReads) + " reads written."
                
parser = argparse.ArgumentParser(description="get Readids from list and then extract these reads from the original readpool")
parser.add_argument("readlist", help="path and name of the readlist file containing the ids of the reads you want extracted")
parser.add_argument("readpool", help="path and name of readpool")
parser.add_argument("output", help="path and name of outputfile")
parser.add_argument("-i", "--info", help="enable terminal info on the status while the programm is running", action="store_true")
    
args = parser.parse_args()

print "Starting programm"
if args.info:
    print "Information enabled"
    
try:
    readlist = open(args.readlist)
    readpool = open(args.readpool)
    output = open(args.output, "w")
    idList = []
except:
    print "Error - unable to open files"
    exit(0)
    
getReadIDs(readlist, idList)
writeReads(readpool, idList, output)        