'''
Created on Feb 26, 2016

@author: maxdriller
'''


from Bio import SeqIO
import gzip 
import argparse


parser = argparse.ArgumentParser(description="")
parser.add_argument("fastq_file", help="", type=str)
#parser.add_argument("outFile", help="", type=str)
parser.add_argument("--gz", "-gzip", action="store_true")

args = parser.parse_args()

if args.gz:
    fastqParser = SeqIO.parse(gzip.open(args.fastq_file), "fastq")
else:
    fastqParser = SeqIO.parse(args.fastq_file, "fastq")

totalsum = 0
totalreads = 0
for fastq in fastqParser:
    totalreads += 1
    #print len(fastq.letter_annotations["phred_quality"])
    #print sum(fastq.letter_annotations["phred_quality"])
    
    totalsum += float(sum(fastq.letter_annotations["phred_quality"]))/len(fastq.letter_annotations["phred_quality"])
    
print totalsum/totalreads