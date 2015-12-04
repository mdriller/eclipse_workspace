'''
Created on 23.01.2015

@author: maxdriller
'''

import argparse
import datetime


def handleBLASTtab(stream):
    for line in stream:
        tab = line.split("\t")
        
        if tab[0].split("_")[3][0] == "c":
            list1.append(tab[0].split("_")[3][1:])
        else:
            list1.append(tab[0].split("_")[3])
            

def checkContigReadList(stream):
    for line in stream:

        if line.startswith("#") == False:
            tab = line.split("\t")
            
            
            #print tab[0].split("_")[2]
            
            if tab[0].split("_")[2] == "rep":
                id1 = tab[0].split("_")[3][1:]
            else:
                id1 = tab[0].split("_")[2][1:]
            
            #print id1
            
            if id1 in list1:
                
                #outfile.write(tab[1].split("-")[1].split("/")[0] + "\n")
                list2.append(tab[1].split("-")[1].split("/")[0])
                #print tab[1].split(":")[6].split("/")[0]
                
                
def checkReads(readStream, outStream):
    x = 0
    curreads = len(list2)
    
    for line in readStream:
        
        if line.startswith("@M01271"):
            id2 = line.split("-")[1].split(" ")[0]
            #print id2
                
            if id2 in list2:
                #print line
                outStream.write(line)
                #list2.remove(id2)
                x = 3
                
                #if args.info:
                    #curreads = curreads - 1 
                    #print str(curreads) + "/" + str(totalreads) + " Reads left"             
                
        elif x > 0:
            #print line
            outStream.write(line)
            x -= 1


parser = argparse.ArgumentParser(description="Extract reads from BLASTed Contigs")
parser.add_argument("tabBLASTOutput", help="path to BLAST-output file in tab format", type=str)
parser.add_argument("MIRAcontigReadList", help="path to contigReadList of MIRA-info output", type=str)
parser.add_argument("readsFASTQ", help="path to reads file in FASTQ format", type=str)
parser.add_argument("output", help="path and name of output(+.fastq)", type=str)
#parser.add_argument("-i", "--info", help="prints out the number of used reads and the current process", action="store_true")

args = parser.parse_args()            


start_time = datetime.datetime.now()
print "Started at: " + str(start_time)

list1=[]
list2=[]

#resultBLAST = open("data/results", "r")
resultBLAST = open(args.tabBLASTOutput)
handleBLASTtab(resultBLAST)

resultBLAST.close()


print "Total number of blasted contigs: " + str(len(list1))

#if args.info:
    #print list1
    #print "Total number of blasted contigs: " + str(len(list1))


contigReadlist = open(args.MIRAcontigReadList)
checkContigReadList(contigReadlist)

contigReadlist.close()
#outfile.close()


#if args.info:
    #totalreads = len(list2)
    #print "Total number of reads: " + str(totalreads)


#outfile = open("data/output_Readnrs.txt", "r")
#readstream = open("data/testReads.fasta", "r")

#readstream = open("/home/maxdriller/Schreibtisch/Praktikum/Azza/S15trimmed.fastq", "r")
readstream = open(args.readsFASTQ)
#outreads = open("data/out_READS.fasta", "w")
outreads = open(args.output, "w")

checkReads(readstream, outreads)

end_time = datetime.datetime.now()
print "Finished at: " + str(end_time)

readstream.close()
outreads.close()

