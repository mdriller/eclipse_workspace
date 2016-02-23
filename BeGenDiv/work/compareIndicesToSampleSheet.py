'''
Created on Feb 19, 2016

@author: maxdriller
'''

import argparse
import editdistance

parser = argparse.ArgumentParser(description="")
parser.add_argument("indices", help="", type=str)
parser.add_argument("samplesheet", help="", type=str)
parser.add_argument("outFile", help="", type=str)

args = parser.parse_args()


indicesIn = open(args.indices)
sampleSheet = open(args.samplesheet)

outWriter = open(args.outFile, "w")


indexDict = {}



data = False
for line in sampleSheet:
    
    if line.startswith("[Data]"):
        #print line
        data=True
        continue
        
    if data == True:
        if not line.startswith("Sample_ID"):
            #print line
            i5 = line.split(",")[5]
            i7 = line.split(",")[7]
            indCombi = i7 + "+" + i5
            
            sampleID = line.split(",")[1]
            
            
            indexDict[indCombi] = [sampleID]
        
    else:
        continue
    
print len(indexDict)


for line in indicesIn:
    idComb = line.split("\t")[0]
    count = line.split("\t")[1].strip("\n")
    
    if indexDict.get(idComb, "missing") != "missing":
        #print "FOUND IT"
        indexDict[idComb].append(count)
        
    
    
#print indexDict

for ind in indexDict:
    print indexDict[ind]
    outWriter.write(indexDict[ind][0] + "\t" + ind + "\t" +  indexDict[ind][1] + "\n")
    