'''
Created on 16.04.2015

@author: maxdriller
'''
import sys
from sys import argv


#tRAPstream = open("/home/maxdriller/Schreibtisch/UNI/SoftwarePraktikum-2015/analysis/PWM-Genome-Scan/2000bp-promoter-seqs-NEW-tRAP.bed")
#outstream = open("/home/maxdriller/Schreibtisch/UNI/SoftwarePraktikum-2015/analysis/PWM-Genome-Scan/2000bp-promoter-seqs-FINAL.bed", "w")
#hg19annostream = open("/home/maxdriller/Schreibtisch/UNI/SoftwarePraktikum-2015/SoftwarePraktikum/data/PWM-Genome-Scan/files-for-trap/hg19_annotation.bed")
 
if len(sys.argv) != 6:
    print "wrong call - not the right amount of arguments"
    print "please call: _.py [TRAPinput] [upstreamsize] [downstreamsize] [annotationFile] [output]"
    exit() 
    
    
else:
    tRAPinput = argv[1]
    upsize = int(argv[2])
    downsize = int(argv[3])
    annoInput = argv[4]
    outfile = argv[5]
    print annoInput  + "  " + outfile
    print str(downsize) + "  " + str(upsize)
    
    tRAPstream = open(tRAPinput)
    outstream = open(outfile, "w")
    hg19annostream = open(annoInput)
 
 
 
 
genedict = {}


for hg19line in hg19annostream:
    hg19splitted = hg19line.split("\t")

    if hg19splitted[5] == "-":
        start = (int(hg19splitted[2]) - downsize)   
            
    else:
        start = (int(hg19splitted[1]) - downsize)
        
    if genedict.get(start, "missing") == "missing":
        if hg19splitted[3].startswith("NM"):
            genedict[start] = hg19splitted[3]
        
for line in tRAPstream:
    if not line.startswith("#"):
        splitted = line.split("\t")
        
        start = int(splitted[0].split(":")[1].split("-")[0])
        end = int(splitted[0].split(":")[1].split("-")[1])
        
        if genedict.get(start, "missing") != "missing":
            outstream.write(line.strip("\n") + "\t" + genedict[start] + "\n")
            
            