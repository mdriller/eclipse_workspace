'''
Created on Dec 9, 2015

@author: maxdriller
'''

import os
    
def doStuff(tempPath, inFile, outDir):
    
    if os.path.isdir(outDir) == False:
        os.mkdir(outDir)
    
    sample = False
    clusterCount = 1
    seqDict = {}
    
    for line in inFile:
        if line.startswith(">"):
            
            splitted  = line.strip().split(" ")
            name = splitted[0][1:]
            seq = str(splitted[-1])           

            seqDict[name]  = seq
                
        if line.startswith("//"):
            
            outwriter = open(outDir + "/" + "cluster" + str(clusterCount) + ".arp", "w")
            
            template = open(tempPath)
            
            for line2 in template:
                                
                
                if line2.startswith("\tSampleData={"):
                    outwriter.write(line2)
                    sample = True
                
                elif line2.startswith("}"):
                    outwriter.write(line2)
                    sample = False
                
                
                elif sample == True:
                    splitted = line2.split("\t")
                    outwriter.write(splitted[0] + "\t" + "1" + "\t" + seqDict[splitted[0]] + "\n")
                    
                else:
                    outwriter.write(line2)
            outwriter.close()
            
            clusterCount += 1
            template.close()        
         
        

 
if __name__ == "__main__":
    
    import argparse 
    
    
    parser = argparse.ArgumentParser(description="creates a arlequin input file out of a 'cluster file (.loci)', needs an example arlequin file to know the structure, header, seqnames, etc.")
    parser.add_argument("template", help="arlequin input file as reference, f.e. you can use the one for the 1. cluster as an example so the code knows the structure of the header, the names of the samples etc.", type=str)
    parser.add_argument("lociIn", help="input file for example: '5_samples.loci", type=str)
    parser.add_argument("outDir", help="directory where fasta files will be created", type=str)
    args = parser.parse_args()
    
    
    doStuff(args.template, open(args.lociIn), args.outDir)
    