'''
Created on 27.02.2015

@author: maxdriller
'''

import argparse

def getReadIDs(liststream, cidlist):
    for line in liststream:
        id = line.split("_")[5].strip("\n")
        cidlist.append(id) 

def extractLcontigs(cidlist, contigstream, outstream):
    if args.info:
        i = 0
        
    write = False
    
    for line in contigstream:
        if line.startswith(">"):
            id = line.split("_")[4].strip("\n")
           
            if id == "rep":
                id = line.split("_")[5].strip("\n")
            
            if id in cidlist:
                write = True
                outstream.write(line)
                
                if args.info:
                    i += 1
                
            else:
                write = False
        
        else:
            if write:
                outstream.write(line)
    
    if args.info:
        print str(i) + " Large Contigs written in new file"


parser = argparse.ArgumentParser(description="extract large COntogs from MIRA denovo assembly")
parser.add_argument("Contiglist", help="name and path to MIRA ..._info_largecontigs.txt")
parser.add_argument("Contigs", help="name and path to MIRA denovo output")
parser.add_argument("Output",help="name and path (and format ending .fasta) to the outputfile this script will create")
parser.add_argument("-i", "--info", help="activate for extra Information", action="store_true")
args = parser.parse_args()

try:
    idlist = []
    liststream = open(args.Contiglist)
    contigstream = open(args.Contigs)
    outstream = open(args.Output, "w")
except:
    print "Error - unable to open files"
    
getReadIDs(liststream, idlist)
extractLcontigs(idlist, contigstream, outstream)
