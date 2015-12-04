'''
Created on 22.04.2015

@author: maxdriller
'''
import sys
from sys import argv

def editFile(instream, outstream):
    
    for line in instream:
        chrom = line.split("\t")[0]
        genename = line.split("\t")[3]
        id = line.split("\t")[5]
        if id == "-":
            start1 = int(line.split("\t")[2]) - downsize
            start2 = start1 + (downsize+upsize)
        else:
            start1 = int(line.split("\t")[1]) - downsize
            start2 = start1 + (downsize+upsize)
        hae = line.split("\t")[9]
      
        
        if genename.startswith("NM"):
            outstream.write(chrom + "\t" + str(start1) + "\t" + str(start2)  + "\t" + genename + "\t" + hae + "\t" + id +"\n")


if len(sys.argv) != 5:
    print "wrong call - not the right amount of arguments"
    print "please call: _.py [input] [upstreamsize] [downstreamsize] [output]"
    exit() 
    
    
else:
    annoInput = argv[1]
    upsize = int(argv[2])
    downsize = int(argv[3])
    outfile = argv[4]
    print annoInput  + "  " + outfile
    print str(downsize) + "  " + str(upsize)

try:
    stream1 = open(annoInput)
    outstr = open(outfile, "w")
except:
    print "Error - unable to open files"

editFile(stream1, outstr)