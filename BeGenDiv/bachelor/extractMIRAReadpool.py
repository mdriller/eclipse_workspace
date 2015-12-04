'''
Created on 27.05.2015

@author: maxdriller
'''

import argparse
import gzip


def createReadDict(readpool, idDict):
    for line in readpool:  
        if not line.startswith("#"):
            
            
            splitted = line.split("\t")
            
            rID = splitted[1].strip("\n")
            #print rID
                
            if rID.endswith("/1") or rID.endswith("/2"):
                rID = rID[0:-2]
                    
                '''
                if rID.endswith("/1"):
                     rID = rID.strip("/1")
                elif rID.endswith("/2"):
                    rID = rID.strip("/2")
                '''
                #print rID
                    
                idDict[rID] = 9

def getReads(readInR1, readInR2, direct, idDict, readOutR1, readOutR2):
    
    write = False
    readcount = 0
    linecount = 0

    for line in readInR1:
        line2 = readInR2.readline()
        if linecount % 4 == 0:
            splitted = line.split(" ")
            splitted2 = line2.split(" ")
            
            rID = splitted[0][1:].strip("\n")
            rID2 = splitted2[0][1:].strip("\n")
            #print line
            #print rID
            if rID != rID2:
                exit(0)
            
            if idDict.get(rID, "missing") != "missing":                
                idDict[rID] = direct
                
                #print "found id"
                write = True
                readOutR1.write(line)
                readOutR2.write(line2)
               
                readcount += 1
            else:
                write = False
        else:
            if write == True:
                readOutR1.write(line)
                readOutR2.write(line2)
                
        linecount += 1
        
def getReadsExMode(readInR1, readInR2, direct, idDict, readOutR1, readOutR2):
    
    write = False
    readcount = 0
    linecount = 0

    for line in readInR1:
        line2 = readInR2.readline()
        if linecount % 4 == 0:
            splitted = line.split(" ")
            splitted2 = line2.split(" ")
            
            rID = splitted[0][1:].strip("\n")
            rID2 = splitted2[0][1:].strip("\n")
            #print line
            #print rID
            if rID != rID2:
                exit(0)
            
            if idDict.get(rID, "missing") == "missing":                
                idDict[rID] = direct
                
                #print "found id"
                write = True
                readOutR1.write(line)
                readOutR2.write(line2)
               
                readcount += 1
            else:
                write = False
        else:
            if write == True:
                readOutR1.write(line)
                readOutR2.write(line2)
                
        linecount += 1
      
def getReadsOneFile(readIn, direct, idDict, readOutR1, readOutR2):
    
    write1 = False
    write2 = False
    readcount = 0
    linecount = 0

    for line in readIn:
        if linecount % 4 == 0:
            splitted = line.split(" ")
            
            rID = splitted[0][1:].strip("\n")
            #print rID[0:-2]
            
            if idDict.get(rID[0:-2], "missing") != "missing":                
                idDict[rID] = direct
                
                #print "found id"
                if rID.endswith("/1"):  
                    #print "hello 1"
                    write1 = True
                    readOutR1.write(line)
                elif rID.endswith("/2"): 
                    write2 = True
                    readOutR2.write(line)
               
                readcount += 1
            else:
                write1 = False
                write2 = False
        else:
            if write1 == True:
                readOutR1.write(line)
            elif write2 == True:
                readOutR2.write(line)
                
        linecount += 1
                
    #if direct == 1:
       # print "Extracting of forward reads done - " + str(readcount) + " reads written"
    #elif direct == 2:
       # print "Extracting of reverse reads done - " + str(readcount) + " reads written"
                
parser = argparse.ArgumentParser(description="Divide readpool into forard and reverse files", epilog="return reads in fasta/fastq format")
parser.add_argument("readpool", help="path and name of MIRA contigreadlist", type=str)
parser.add_argument("readsR1", help="path and name of input full forward reads")
parser.add_argument("readsR2", help="path and name of input full reverse reads")
parser.add_argument("outR1", help="path and name of output readpool forward read file", type=str)
parser.add_argument("outR2", help="path and name of output readpool reverse read file", type=str)
parser.add_argument("--gz", help="activate if readfiles are zipped", action="store_true")
parser.add_argument("--ex", "-except", help="change mode if --ex it will extract all but the reads in the list, otherwise only extract reads in list", action="store_true")

args = parser.parse_args()

poolIn = open(args.readpool)
r1out = open(args.outR1, "w")
r2out = open(args.outR2, "w")

if args.gz:
    r1In = gzip.open(args.readsR1)
    r2In = gzip.open(args.readsR2)
else:
    r1In = open(args.readsR1)
    r2In = open(args.readsR2)

readDict = {}

createReadDict(poolIn, readDict)

print "The readpool contains: " + str(len(readDict)) + " paired end reads"

# for forward and reverse reads
if args.ex == True:
    getReadsExMode(r1In, r2In, 1, readDict, r1out, r2out)
else:
    getReads(r1In, r2In, 1, readDict, r1out, r2out)

#getReadsOneFile(r1In, 1, readDict, r1out, r2out)

#for r in readDict:
    
    #if readDict[r] != 2:
        #print r

