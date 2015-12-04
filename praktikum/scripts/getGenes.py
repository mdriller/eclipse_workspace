'''
Created on 20.03.2015

@author: maxdriller
'''
import argparse

def createGenList(instream, genelist):
    print "Starting Creating Gene list"
    for line in instream:
        genename = line.split("\t")[3]
        genelist.append(genename)
    print "Finished Creating Gene list"
    
    
def createIDListAndFilter(instream, idList, distance):
    print "Starting Creating ID list"
    counter = 0
    for line in instream:
        splitted = line.split("\t")
        distance[counter][0] = splitted[7]
        distance[counter][1] = splitted[3]
        distance[counter][2] = splitted[5]
        counter += 1
    
    print "Finished Creating ID list"
    print "Test: " + str(distance[counter])
    print "Filtering only biggest peaks for each gene"
    print "Test(Counter) = " + str(counter)
    for n in range(counter-1):
        p = distance[n][0]
        w = distance[n][1]
        t = distance[n][2]
        for i in range(counter-1):
            if p == distance[i][0]:
                if w <= distance[i][1]:
                    w = distance[i][1]
                    p = distance[i][0]
                    t = distance[i][2]
        #outstream.write(t + "\n")
        if t == 0:
            break
        if t not in idList:
            idList.append(t)
    print "Finished Filtering"
    
    
def printOutput(instream, idList, geneList):
    print "Starting output printing"
    count2 = 0
    for line in macsstream2:
        splitted = line.split("\t")
        print splitted[5]
        count2 += 1
        print count2 
        
        if splitted[0] != "MT":
            if splitted[5] in idList:
                print "found ID!!! printing line " + str(count2)
                outstream.write(line.strip("\n") + "\t" + geneList[int(splitted[7])-1] + "\n") 
    print "Finished output printing" 


    
parser = argparse.ArgumentParser(description="check if there is a gene next to a peak")
parser.add_argument("macsout", help="bedfile from macs")
parser.add_argument("annotation", help="file that contains the annotation of the genome")
parser.add_argument("output", help="path and name of output file")                

args = parser.parse_args()


#pprint.pprint(distance)


#try:
macsstream = open(args.macsout)
outstream = open(args.output, "w")
hg19stream = open(args.annotation)
macsstream2 = open(args.macsout)
    
genelist = []
idlist = []
    
m = 58402
distance = [[0 for k in xrange(3)] for i in xrange(m)]
    
createGenList(hg19stream, genelist)
print "Gene-list contains: " + str(len(genelist)) + " Genes"
createIDListAndFilter(macsstream, idlist, distance)
print "ID-list contains: " + str(len(idlist)) + " IDs"
printOutput(macsstream2, idlist, genelist)
    
macsstream.close()
hg19stream.close()
macsstream2.close()
outstream.close()
    
#except:
 #   print "Error - unable to open file"
    
