'''
Created on 22.01.2015

@author: maxdriller
'''

import argparse
import gzip

def getRNames(instreamR1, instreamR2, idList, name):
    
    print "Getting readnames of the blast inputs..."
    print "Starting with R1..."
    
    for line in instreamR1:
        #(queryId, subjectId, percIdentity, alnLength, mismatchCount, gapOpenCount, queryStart, queryEnd, subjectStart, subjectEnd, eVal, bitScore) = line.split("\t")
        splitted = line.split("\t")
        rID = int(splitted[0].split(".")[1])
        #print rID
        if idList.get(rID, "missing") == "missing":
            idList[rID] = 1
    
    
    print "Finished R1 now starting with R2..."
    
    for line in instreamR2:
        splitted = line.split("\t")
        rID = int(splitted[0].split(".")[1])
        #print rID
        if idList.get(rID, "missing") == "missing":
            idList[rID] = 1
            
    print "Finished all readsnames are extracted"

def extractReads(r1stream, r2stream, idList, outstrR1, outstrR2):
    
    counter = 0
    
    print "Now starting to extract reads from original full readset"
    print "Starting with R1..."
    
    write = False 
    
    for line in r1stream:
        if line.startswith(name):
            splitted = line.split(" ")
            rID = int(splitted[0].split(".")[1])
            
            if idList.get(rID, "missing") != "missing":
                counter += 1
                
                write = True
                outstrR1.write(line)
            else:
                write = False
            
        else:
            if write == True:
                outstrR1.write(line)          
    
    print "Finished R1 now starting with R2..."
    
    for line in r2stream:
        if line.startswith(name):
            splitted = line.split(" ")
            rID = int(splitted[0].split(".")[1])
                
            if idList.get(rID, "missing") != "missing":
                counter += 1
                
                write = True
                outstrR2.write(line)
            else:
                write = False
                
        else:
            if write == True:
                outstrR2.write(line) 
                
    print "Finished extracting and writing of BLASTED reads"
    
    return counter

    
parser = argparse.ArgumentParser(description="extracts reads that are in a BLAST tab file")
parser.add_argument("blastOUTr1", help="path and name of BLAST-output file in tab-format(format 6) for forward reads")
parser.add_argument("blastOUTr2", help="path and name of BLAST-output file in tab-format(format 6) for reverse reads")
parser.add_argument("readsR1", help="file containing the forward reads")
parser.add_argument("readsR2", help="file containing the reverse reads")
parser.add_argument("outfileR1", help="path and name of file for outputs of forward reads")
parser.add_argument("outfileR2", help="path and name of file for outputs of reverse reads")
parser.add_argument("-g", "--gzip", help="activate if file is zipped", action="store_true")

args = parser.parse_args()

#find name/identifier
blastr1 = open(args.blastOUTr1)
name = "@" + blastr1.readline().split("\t")[0].split(".")[0]
print name
blastr1.close()


blastr1 = open(args.blastOUTr1)
blastr2 = open(args.blastOUTr2)
    
outR1 = open(args.outfileR1, "w")
outR2 = open(args.outfileR2, "w")
    
if args.gzip:
    readsR1 = gzip.open(args.readsR1)
    readsR2 = gzip.open(args.readsR2)         
        
else:
    readsR1 = open(args.readsR1)
    readsR2 = open(args.readsR2)

iddict = {}

getRNames(blastr1, blastr2, iddict, name)  
        
blastr1.close()
blastr2.close()

print "Anzahl der reads: " + str(len(iddict))

readcount = extractReads(readsR1, readsR2, iddict, outR1, outR2)

readsR1.close()
readsR2.close()

outR1.close()
outR2.close()


print "ALL DONE - " + str(readcount) + " Reads written in total, " + str(readcount/2) + " in each paired end file"