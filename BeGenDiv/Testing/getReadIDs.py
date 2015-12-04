'''
Created on 10.03.2015

@author: maxdriller
'''
import argparse
import threading


class myThread (threading.Thread):
    def __init__(self, threadID, name, stream, rlist):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.stream = stream
        self.rlist = rlist
    def run(self):
        print "Starting " + self.name
        # Get lock to synchronize threads
        getReadIDs(self.stream, self.rlist)
        # Free lock to release next thread



def getReadIDs(instream, readlist):
    for line in instream:
        if line.startswith("@M01271"):
            id = line.split("-")[1].strip("\n")
            #print id
            readlist.append(id)
            
def compareIDlists(list1, list2, sharedlist, outstr1, outstr2):

    for id in list1:
        if id in list2:
            sharedlist.append(id)
        else:
            outstr1.write(id + "\n")
    else:
        for id in list2:
            if id in list1:
                sharedlist.append(id)
            else:
                outstr2.write(id + "\n")
            
            

parser = argparse.ArgumentParser(description="get ad IDs and compare")
parser.add_argument("input", help="input file")
parser.add_argument("input2", help="second input file")
parser.add_argument("output", help="output file")
parser.add_argument("output2", help="second output file")
args= parser.parse_args()


try:
    stream1 = open(args.input)
    stream2 = open(args.input2)
    outstream1 = open(args.output, "w")
    outstream2 = open(args.output2, "w")
    readlist1 = []
    readlist2 = []
    threadlist = []
except:
    print "Error - unable to open file"



thread1 = myThread(1, "Thread-1", stream1, readlist1)
thread2 = myThread(2, "Thread-2", stream2, readlist2)
threadlist.append(thread1)
threadlist.append(thread2) 

thread1.start()
thread2.start()
    
# Wait for all threads to complete
for t in threadlist:
    t.join()


print "list lengths input1: " + str(len(readlist1))
print "list lengths input2: " + str(len(readlist2)) 

sharedIDlist =[]

compareIDlists(readlist1, readlist2, sharedIDlist, outstream1, outstream2)
print "sharedList length: " + str(len(sharedIDlist))
           