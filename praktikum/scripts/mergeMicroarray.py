'''
Created on 30.03.2015

@author: maxdriller
'''
import sys
from sys import argv

if len(sys.argv) != 4:
    print "wrong call - not the right amount of arguments"
    print "please call: _.py [input] [input2] [output]"
    exit() 

probesstream = open(argv[1])
outstream = open(argv[3], "w")

xstream = open(argv[2])

genedict = {}

for line in xstream:
    splitted = line.split(" ")
    
    xid = splitted[0][1:].strip("\"")
    
    if genedict.get(xid, "missing") == "missing":
        genedict[xid] = splitted
        
    else:
        print "weird xid already there"
        
xstream.close()

for line in probesstream:
    splitted = line.split("\t")
    
    idend = splitted[0].find("at") + 2
    id = splitted[0][1:idend]
    
    if genedict.get(id, "missing") == "missing":
        print "id not there weird there must be a mistake"
    else:
        #outstream.write(line + " " + genedict[id]
        xsplitted = genedict[id]
        outstream.write(splitted[0][1:].strip("\"") + "\t" + splitted[1][1:].strip("\n").strip("\"") + "\t"+ str(xsplitted[1])  + "\t"+ str(xsplitted[2]) + "\t"+ str(xsplitted[3]) + "\t"+ str(xsplitted[4]) + "\t"+ str(xsplitted[5]) + "\t"+ str(xsplitted[6]))
        
        
outstream.close()
probesstream.close()