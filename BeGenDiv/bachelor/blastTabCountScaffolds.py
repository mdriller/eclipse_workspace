'''
Created on 12.05.2015

@author: maxdriller
'''

#import argparse
#parser = argparse.ArgumentParser(description="Extract reads from BLASTed Contigs")
#parser.add_argument("blastIn", help="path and name of Blast tabular output", type=str)
#parser.add_argument("col", help="columnNr of the blastIn to be counted(column of ", type=int)
#parser.add_argument("output", help="path and name of outputfile(.fastq)", type=str)
#args = parser.parse_args()


#blaststream = open(args.blastINn)

blaststream = open("/home/maxdriller/Schreibtisch/Praktikum/Bachelor/Choloepus_hoffmanni/scaffold_blasting/R2_refCH_FILTERED_SCAF_BLASTED.out")
outstream = open("/home/maxdriller/Schreibtisch/Praktikum/Bachelor/Choloepus_hoffmanni/scaffold_blasting/R2_Scaf_hits.txt", "w")

scafDict ={}

for line in blaststream:
    splitted = line.split("\t")
    scafID = splitted[12].split(" ")[7].strip(",")[8:]
    #scafID = splitted[12]
    
    if scafDict.get(scafID, "missing") == "missing":
        scafDict[scafID] = 1
    else:
        scafDict[scafID] += 1
        
outstream.write("#scaf" + "\t" + "#blasted Reads")      
for scaf in scafDict:
    outstream.write("\n")
    outstream.write(scaf + "\t" + str(scafDict[scaf]))

    