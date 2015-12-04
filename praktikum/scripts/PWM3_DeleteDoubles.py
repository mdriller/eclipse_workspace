'''
Created on 02.04.2015

@author: maxdriller
'''
import sys
from sys import argv

#datastream = open("/home/maxdriller/Schreibtisch/UNI/SoftwarePraktikum-2015/analysis/PWM-Genome-Scan/2000bp-promoter-seqs-FINAL.bed")
#outstream = open("/home/maxdriller/Schreibtisch/UNI/SoftwarePraktikum-2015/analysis/PWM-Genome-Scan/2000bp-promoter-seqs-FINAL_NO_DOUBLES.bed", "w")


if len(sys.argv) != 3:
    print "wrong call - not the right amount of arguments"
    print "please call: _.py [input] [output]"
    exit() 
    
    
else:
    infile = argv[1]
    outfile = argv[2]
    
    datastream = open(infile)
    outstream = open(outfile, "w") 

genedict = {}

for line in datastream:
    splitted = line.split("\t")
    gene_name = splitted[9]
    #print gene_name

    if genedict.get(gene_name, "missing") == "missing":
        genedict[gene_name] = 1
        print "adding gene to dict and writing line"
        outstream.write(line)
        
    else:
        print "gene already in list not writing"
        
datastream.close()
outstream.close() 
    