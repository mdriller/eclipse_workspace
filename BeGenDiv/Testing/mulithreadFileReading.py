'''
Created on 08.02.2015

@author: maxdriller
'''

import threading
import thread
import time


class myThread(threading.Thread):
    def __init__(self, threadID, name, filepath):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.filepath = filepath
                
    def run(self):
                
        print "Starting: " + self.name 
        
        lock1.acquire()
        for line in self.filepath:
            
            if self.threadID == 1:
                
                list1.append(line)
            else:
                list2.append(line)
            #with lock:
            #writeLines(line, self.name, self.threadID)
            #lock.release()
            #print  "%s - %s" % (self.name, "ready for more") 
        
        lock1.release()
        
        print "Ending: " + self.name
        
def writeLines(line, tname, tID):
    
    #lock.acquire()
    #print  "%s - %s" % (tname, "is printing")
    outstr.write(line)
    
    #if tID == 1:
        #t2event.clear()
        #t2event.set()
        #t1event.wait()
        #condition2.acquire()
        #condition2.notify()
        #condition2.release()
        
        #condition1.acquire()
        #condition1.wait()
        #condition1.release()
    #else:
        #t1event.set()
        #t1event.clear()
        #t1event.set()
        #t2event.wait() 
        #condition1.acquire()
        #condition1.notify()
        #condition1.release()
        
        #condition2.acquire()
        #condition2.wait()
        #condition2.release()
    
    print "next pls"
    

stream1 = open("/home/maxdriller/Schreibtisch/test1.fastq")
stream2 = open("/home/maxdriller/Schreibtisch/test2.fastq")
outstr = open("/home/maxdriller/Schreibtisch/testout.fastq", "w")


list1 =[]
list2=[]

threadlist = []
      
thread1 = myThread(1, "thread1", stream1)
thread2 = myThread(2, "thread2", stream2)

lock1 = threading.Lock()
lock2 = threading.Lock()
t1event = threading.Event()
t2event = threading.Event()

condition1 = threading.Condition(lock1)
condition2 = threading.Condition(lock2)

threadlist.append(thread1)
threadlist.append(thread2) 

thread1.start()
thread2.start()

# waiting for all thraeds to finish
for t in threadlist:
    t.join()
    
print "Exiting Main Thread"
#print threading.active_count() 

stream1.close()
stream2.close()
#outstr.close()


for line in list1:
    outstr.write(line)
    
for line in list2:
    outstr.write(line)
   
    
