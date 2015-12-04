'''
Created on 02.04.2015

@author: maxdriller
'''
import sys
    
from sys import argv

if len(sys.argv) != 3:
    print "wrong call - not the right amount of arguments"
    print "please call: _.py [input] [output]"
    exit() 

datastream = open(argv[1])


genedict = {}


for line in datastream:
    splitted = line.split("\t")
    
    gene_name = splitted[1]
    p_val = float(splitted[6])
    #print p_val
    
    if genedict.get(gene_name, "missing") == "missing":
        genedict[gene_name] = p_val
        
    else:
        #print "gene already there"
        if p_val < genedict[gene_name]:
            #print "new p_val"
            genedict[gene_name] = p_val
            
datastream.close()

datastream = open(argv[1])
outstream = open(argv[2], "w")

for line in datastream:
    splitted = line.split("\t")
    
    gene_name = splitted[1]
    p_val = float(splitted[6])
    
    if genedict[gene_name] == p_val:
        print "found it!!! - now writing the line..."
        outstream.write(line)
    
    
print len(genedict)    
    
outstream.close()
datastream.close()        
    