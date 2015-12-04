'''
Created on 12.04.2015

@author: maxdriller
'''
import random
import argparse
import gzip
from datetime import datetime

# changed the fkt because checking if seqcount in list will take lots of time for big samples
def writeSubset(instream, outstream, randnums, rDict):

    linecount = 0
    seqcount = 1
    for line in instream:
        # old way by checking the list directly --> long time for bigsamples
        '''
        if seqcount in randnums:
            #print line
            outstream.write(line)
        '''
        if rDict.has_key(seqcount):
            outstream.write(line) 
            
        linecount += 1
        if linecount % 4 == 0:
            seqcount += 1
            #print "new seqs # = " + str(seqcount)

def writeSubset2(instream1, outstream1, instream2, outstream2, randnums, rDict):

    linecount = 0
    seqcount = 1
    for line1 in instream1:
        # old way by checking the list directly --> long time for bigsamples
        '''
        if seqcount in randnums:
            #print line
            outstream.write(line)
        '''
        
        line2 = instream2.readline()

        if rDict.has_key(seqcount):
            outstream1.write(line1)
            outstream2.write(line2)
            
        linecount += 1
        if linecount % 4 == 0:
            seqcount += 1
            #print "new seqs # = " + str(seqcount)

parser = argparse.ArgumentParser(description= "erstellt ein subset von paired-end reads")
parser.add_argument("size", help="groesse des subsamples in Prozent",type=float)
parser.add_argument("inputR1",help="erste inputdatei R1")
parser.add_argument("inputR2",help="zweite inputdatei R2")
parser.add_argument("outputR1",help="erste outputdatei R1")
parser.add_argument("outputR2",help="zweite outputdatei R2")
parser.add_argument("-g","--gzip",help="Option mit gezippten Dateien",action="store_true")

args = parser.parse_args()

starttime = datetime.now()

if(args.gzip) == True:
    print "opening file R1 with gzip..."
    r1stream = gzip.open(args.inputR1)
else:
    print "opening file R1..."
    r1stream = open(args.inputR1)

# get the number of sequences in fastq file
totallength = 0
print "file R1 opened - now counting the number of sequences"
for line in r1stream:
    totallength += 1

r1stream.close()
# calculate number of fastq-seqs = (number of lines)/4
totallength = totallength/4
print "total number of seqs: " + str(totallength)

readpercent = int((totallength/100)*args.size)
print str(args.size) + "% of the reads = " + str(readpercent)

# create list of random numbers in range of number of seqs
randlist = random.sample(range(1, totallength), readpercent)
#print randlist
# creating an idDict because checking every enntry in a list will take forever for big samples
# --> more preprocessing but will be faster in the end
idDict = {}
for randnr in randlist:
    idDict[randnr] = None




# open files again for extraction of subsets
if(args.gzip) == True:
    print "opening files with gzip"
    r1stream = gzip.open(args.inputR1)
    r2stream = gzip.open(args.inputR2)
else:
    r1stream = open(args.inputR1)
    r2stream = open(args.inputR2)
    print "opening files..."
    
r1out = open(args.outputR1, "w")
r2out = open(args.outputR2, "w")


print "Writing subset to new file for R1 & R2"
writeSubset2(r1stream, r1out, r2stream, r2out, randlist, idDict)


print "All done"
r1stream.close
r1out.close()

r2stream.close()
r2out.close()

endtime = datetime.now()

elapsed_time = endtime - starttime

print "elapsed time: " + str(elapsed_time) + " [h:min:sec:milisec]"