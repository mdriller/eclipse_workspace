'''
Created on 31.03.2015

@author: maxdriller
'''
import argparse

def buildDict(instream):
 
    
    idname = ""
    linedict = {}
    
    for line in instream: 
        if not line.startswith("#"):     
            splitted = line.split("\t")
        
            idname = splitted[0].split(":")[6]
            #print idname
            
            if linedict.get(idname, "missing") == "missing":
                newlist = []
                newlist.append(line)
                linedict[idname] = newlist
            else:
                linedict[idname].append(line)

    #for key in linedict:
    #    print key + " " + str(linedict[key])
        
    return linedict
        

def checkDict(outstream, linedict, identifier):
    
    collist = ["qseqid\t", "sgi\t", "pident\t", "length\t", "mismatch\t", "gapopen\t", "qstart\t", "qend\t", "sstart\t", "send\t", "evalue\t", "bitscore\t", "stitle", "\n#\n"]
    
    outstream.write("#")
    for ele in collist:
        outstream.write(ele)
    
    for key in linedict:
        write = False
        
        for line in linedict[key]:
            
            if args.filterfor:
                if not identifier in line:
                    write = True
            else:
                if identifier in line:
                    write = True
                
                
        if write == True:
            for line in linedict[key]:
                outstream.write(line)
                
            outstream.write("#\n")

parser = argparse.ArgumentParser(description="extract Reads from Blast tab output")
parser.add_argument("blasttab", help="path and name of the blasttab output containing the ids of the reads you want extracted")
parser.add_argument("identifier", help="identification --> f.e. Caretta caretta)")
parser.add_argument("output", help="path and name of outputfile")
parser.add_argument("-f", "--filterfor", help="if this option is set the programm will filter out only the values containing the identifier --> use everything else", action="store_true")
args = parser.parse_args()


try:
    blaststream = open(args.blasttab)
    outputstream = open(args.output, "w")
    identi = args.identifier
except:
    print "Error - unable to open files"
    exit()
    
    
readdict = buildDict(blaststream)

checkDict(outputstream, readdict, identi)


blaststream.close()
outputstream.close()