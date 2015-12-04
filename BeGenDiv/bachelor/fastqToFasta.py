'''
Created on 24.08.2015

@author: maxdriller
'''
import argparse
import gzip

parser = argparse.ArgumentParser(description= "converts a fastq file to fasta file")
parser.add_argument("fastq", help="fastqfile")
parser.add_argument("output", help="fasta output")
parser.add_argument("-g","--gzip",help="enable if fastq file is zipped",action="store_true")

args = parser.parse_args()

if args.gzip:
    fastqstream = gzip.open(args.fastq)
else:
    fastqstream = open(args.fastq)

outstream = open(args.output, "w")

linecount = 0
seqcount = 1
for line in fastqstream:

    if linecount == 4:
        seqcount += 1
        linecount = 0
        
    if linecount == 0:
        #print ">" + line[1:]
        outstream.write(">" + line[1:])
    elif linecount == 1:
        #print line
        outstream.write(line)
        
    linecount += 1
    
outstream.close()
fastqstream.close()

print str(seqcount) + " reads converted to fasta"
    
