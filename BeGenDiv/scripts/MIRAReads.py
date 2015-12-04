'''
Created on 19.01.2015

@author: maxdriller
'''
import argparse
import datetime
import threading


class threadClass(threading.Thread):
    def __init__(self, id, readinput, pattern, output):
        threading.Thread.__init__(self)
        self.id = id
        self.readinput = readinput
        self.pattern = pattern
        self.output = output 
        
    def run(self):
        x = 0        
        for line in self.readinput:
            
            if line.startswith("@"+self.pattern) | line.startswith("+"+self.pattern):    
                line = line.replace(".1 ", "/1 ")
            
            self.output.write(line)
            x += 1
        
        print "Thread " + self.id + " is done - " + str(x/4) + " reads written"


parser = argparse.ArgumentParser(description="get paired end reads in the right format from .1 and .2 to /1 and /2")
parser.add_argument("readfile1", help="path to read-file(forward) in FASTQ-format", type=str)
parser.add_argument("readfile2", help="path to read-file(reversed) in FASTQ-format", type=str)
parser.add_argument("pattern", help="the pattern that follows every @ and + in the 1. and 3. line of every read in fastq-format. [example: SRR857898]")
parser.add_argument("out1", help="path and name of 1. output(+.fastq)", type=str)
parser.add_argument("out2", help="path and name of 2. output(+.fastq)", type=str)

args = parser.parse_args()

start_time = datetime.datetime.now()
print "Started at: " + str(start_time)

input_fastq1 = open(args.readfile1, "r")
input_fastq2 = open(args.readfile2, "r")
  
out_reads1 = open(args.out1, "w")
out_reads2 = open(args.out2, "w")

threadlist = []

th1 = threadClass("1", input_fastq1, args.pattern, out_reads1)
th2 = threadClass("2", input_fastq2, args.pattern, out_reads2)

threadlist.append(th1)
threadlist.append(th2)

th1.start()
th2.start()

for t in threadlist:
    t.join()
    
print "Exiting Main Thread"

end_time = datetime.datetime.now()
print "Finished at: " + str(end_time)

input_fastq1.close()
input_fastq2.close()
out_reads1.close()
out_reads2.close()