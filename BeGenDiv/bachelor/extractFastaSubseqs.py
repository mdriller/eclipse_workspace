'''
Created on 19.08.2015

@author: maxdriller
'''

import argparse
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

parser = argparse.ArgumentParser(description="extract subsseqs from fasta files, subseqs must be described in a tab seperated info file")
parser.add_argument("ScafFasta", help="path and name of file containing the scaffolds with numts in fasta format", type=str)
parser.add_argument("infoFile", help="file containing the Scaffold name and indices of the subseq that needs to be extracted")
parser.add_argument("output", help="path where outfilesshould be created", type=str)

args = parser.parse_args()

fastaIn = SeqIO.parse(args.ScafFasta, "fasta")
infoIn = open(args.infoFile)

seqDict = SeqIO.to_dict(fastaIn)

for line in infoIn:
    if not line.startswith("#"):
        id, name, start, end = line.split("\t")
        
        start = int(start)
        end = int(end)  

        #print id, name, start, end       
        
        scaf = seqDict[id]
                
        if start < end:
            numt_seq = seqDict[id].seq[start:end]
        else:
            numt_seq = seqDict[id].seq[end:start]

        mergednumt = SeqRecord(numt_seq,id=scaf.id, description=scaf.description + " " + str(start) + "-" + str(end))
        
        SeqIO.write(mergednumt, args.output+"/"+name+"_"+str(start)+"_"+str(end)+".fasta", "fasta")
        
            
        
