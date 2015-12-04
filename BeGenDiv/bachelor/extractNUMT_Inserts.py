'''
Created on 28.08.2015

@author: maxdriller
'''
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import argparse

def getINSERTinfo(infostream, NUMTdict):
    
    for line in infostream:
        if not line.startswith("#"):
            splitted = line.split("\t")
            sId = splitted[0]
            

            start = int(splitted[1])-1
            end = int(splitted[2])-1
            
            if NUMTdict.get(sId, "missing") == "missing":
                NUMTdict[sId] = [[start, end]]
            else:
                NUMTdict[sId].append([start, end])
                
def extractINS(inDict, scafsIN, outpath):
    
    for scaf in scafsIN:
        sId = scaf.description.split(" ")[8].strip(",")
        if inDict.get(sId, "missing") != "missing":
            inlist = inDict[sId]
        
            for idx, insert in enumerate(inlist):
                start = insert[0]
                end = insert[1] 
                
                if start < end:
                
                    filename = sId + "_" + str(start) + "-" + str(end) + ".fasta"
                    
                    newseq = SeqRecord("", "fasta")
                    newseq.id = scaf.description
                    newseq.description = sId + "probably a insertion - bases from: " + str(start) + "-" + str(end)     
                    newseq.seq = scaf.seq[start:end]
                   
                elif start > end:   
                
                    filename = sId + "_" + str(end) + "-" + str(start) + ".fasta"
                    
                    newseq = SeqRecord("", "fasta")
                    newseq.id = scaf.description
                    newseq.description = sId + "probably a insertion - bases from: " + str(end) + "-" + str(start)     
                    newseq.seq = scaf.seq[end:start]
                    
                #print newseq
                
                SeqIO.write(newseq, outpath + filename, "fasta")
                
parser = argparse.ArgumentParser(description="Extract reads from BLASTed Contigs")
parser.add_argument("InsertsInfo", help="path and name of blastfile in tab format", type=str)
parser.add_argument("ScaffFasta", help="path and name of Scaffolds in fasta format", type=str)
parser.add_argument("output", help="path where all folders and files will be created", type=str)

args = parser.parse_args()

#open files in readmode --> biopython for fasta-seqs(because its way more comfortable for working with subseqs)
infoNUMTs = open(args.InsertsInfo)
scaffs = SeqIO.parse(args.ScaffFasta, "fasta")
#get path for output folders & files
outpath = args.output
#create empty dictionaries
insertDict = {}

getINSERTinfo(infoNUMTs, insertDict)
extractINS(insertDict, scaffs, outpath)

