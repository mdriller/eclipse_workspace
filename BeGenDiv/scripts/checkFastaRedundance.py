'''
Created on 18.02.2015

@author: maxdriller
'''

import argparse

def checkRed(instream, idlist, outstream):
    
    count_redun = 0
    write = True
    
    for line in instream:
        if line.startswith(">"):
            id = line.split("|")[1]
            
            if id not in idlist:
                idlist.append(id)
                write = True
                #print "id appended"
            else:
                write = False
                count_redun += 1
                
        if write == True:
            outstr.write(line)
            
    print "total redundant seqs removed: " + str(count_redun)
    #print "total non-redundant seqs written in output: " + idlist

        


parser = argparse.ArgumentParser(description="deletes redundant reads from fasta file")
parser.add_argument("input", help="path and name of fasta input file")
parser.add_argument("output", help="path and name of fasta output file")
parser.add_argument("-i", "--info", help="get information while running", action="store_true")
args = parser.parse_args()

if args.info:
    print "info enabled"

listID = []

try:
    fastastream = open(args.input)
    outstr = open(args.output, "w")
except: 
    print "Error - unable to open files"
    exit(0)

checkRed(fastastream, listID, outstr)