'''
Created on 08.12.2015

@author: maxdriller
'''

import os

def getFastafromCluster(infile, outDir):
    
    
    if os.path.isdir(outDir) == False:
        os.mkdir(outDir)
    
    seqDict = {}
    
    for line in infile:
        if line.startswith(">"):
            
            splitted  = line.strip().split(" ")
            name = splitted[0]
            seq = str(splitted[-1])
            filename = name[1:] + ".fasta"
            
            if seqDict.get(name, "missing") == "missing":
                #print "adding seq to Dict"
                
                seqDict[name]  = 1
                #print filename, seq
                
                outwriter = open(outDir + "/" + filename, "w")
                outwriter.write(name + "\n")
                outwriter.write(seq)
                outwriter.close()
                
                
            else:
                #print "FOUND SEQ"
                seqDict[name]  += 1
                
                outwriter = open(outDir + "/" + filename, "a")
                outwriter.write(seq)
                outwriter.close()
          
          
    print seqDict

if __name__ == "__main__":
    
    import argparse    
    
    parser = argparse.ArgumentParser(description="extracts and concatinates the seqs for each sample out of all clusters and creates a fasta file for each concatinated seq")
    parser.add_argument("lociIn", help="input file for example: '5_samples.loci'", type=str)
    parser.add_argument("outDir", help="directory where fasta files will be created", type=str)
    args = parser.parse_args()
    
    inFile = open(args.lociIn)
    
    getFastafromCluster(inFile, args.outDir)
    
    
    
    