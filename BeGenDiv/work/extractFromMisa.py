'''
Created on Feb 26, 2016

@author: maxdriller
'''
import argparse
import os

def buildDIct(msDict, misaPredicts):
    
    
    for line in misaPredicts:
        
        id = line.split("\t")[0]
        
        if msDict.get(id, "missing") == "missing":
            msDict[id] = 1
        
        else:
            print "double"
  
    return msDict


def getClustS_seqs(msDict, clustS_in):
    
    #counter for clusters
    clustcount = 1
    #counts for two \\ lines so that clustercount gets increased correctly
    endcount = 0
    write = False
    
    for line in clustS_in:
        
        if line.startswith(">"):
            id = line.split(";")[0][1:]
            #print id
            
            if msDict.get(id, "missing") == 1:
                #print "found seq"
                write = True
                
                if not os.path.exists("test"):
                    os.mkdir("test")
                
                outWriter = open("test/" + "cluster" +str(clustcount)+".fa", "w")
                

        
        if line.startswith("//"):
            endcount += 1
            
            if write == True:
                outWriter.close()
                write = False
            
            if endcount == 2:
                endcount = 0
                clustcount += 1
        
        if write == True:
            outWriter.write(line)
            
            #print "new cluster"
            
        

parser = argparse.ArgumentParser(description="")
parser.add_argument("misaIn", help="misa output --> the <filename>.misa file", type=str)
parser.add_argument("clustS", help="clustS file", type=str)
parser.add_argument("outFile", help="", type=str)

args = parser.parse_args()

misaInput = open(args.misaIn)

clustSin = open(args.clustS)

misaDict = {}

misaDict = buildDIct(misaDict, misaInput)

print len(misaDict)

getClustS_seqs(misaDict, clustSin)