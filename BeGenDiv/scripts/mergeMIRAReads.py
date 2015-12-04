'''
Created on 12.02.2015

@author: maxdriller
'''

'''
Created on 19.01.2015

@author: maxdriller
'''
import argparse
import datetime


def orderReads1(stream, outstr):
    for line in stream:
        #if line.startswith("@SRR866928") | line.startswith("+SRR866928"):
        #if line.startswith("@SRR857572") | line.startswith("+SRR857572"):
        if line.startswith("@"+args.pattern) | line.startswith("+"+args.pattern):    
            line = line.replace(".1 ", "/1 ")
            
        outstr.write(line)


def orderReads2(stream, outstr):
    for line in stream:
        #if line.startswith("@SRR866928") | line.startswith("+SRR866928"):
        #if line.startswith("@SRR857572") | line.startswith("+SRR857572"):
        if line.startswith("@"+args.pattern) | line.startswith("+"+args.pattern):   
            line = line.replace(".2 ", "/2 ")
                  
        outstr.write(line)




parser = argparse.ArgumentParser(description="Extract reads from BLASTed Contigs")
parser.add_argument("readfile1", help="path to read-file(forward) in FASTQ-format", type=str)
parser.add_argument("readfile2", help="path to read-file(reversed) in FASTQ-format", type=str)
parser.add_argument("pattern", help="the pattern that follows every @ and + in the 1. and 3. line of every read in fastq-format. [example: SRR857898]")
parser.add_argument("out", help="path and name of 1. output(+.fastq)", type=str)


args = parser.parse_args()

start_time = datetime.datetime.now()
print "Started at: " + str(start_time)

input_fastq = open(args.readfile1, "r")
input_fastq2 = open(args.readfile2, "r")
  
out_reads = open(args.out, "w")

    
orderReads1(input_fastq, out_reads)
print "1/2 is done!"
orderReads2(input_fastq2, out_reads)

end_time = datetime.datetime.now()
print "Finished at: " + str(end_time)

