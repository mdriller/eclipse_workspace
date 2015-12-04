'''
Created on 29.10.2015

@author: maxdriller
'''

def createReadDict(samStream):
    
    readDict = {}
    
    for line in samStream:
        #ignore header lines
        if not line.startswith("@"):
            splitted = line.split("\t")
            
            readID = splitted[0]
            #print readID
            
            if readDict.get(readID, "missing"):
                readDict[readID] = 1
            
    return readDict


def getReads(readDict, rR1, rR2, outR1, outR2):
    write = False
    
    linecount = 0
    readcount = 1
    for line in rR1:
        line2 = rR2.readline()
        
        linecount += 1
        #get readID out of first line for each read
        if linecount == 1:
            rID = line.split(" ")[0].strip("@")
            #print rID
            rID2 = line2.split(" ")[0].strip("@")
            #print rID
            if readDict.get(rID, "missing") == 1:
                print "FOUND READ"
                write = True
            elif readDict.get(rID2, "missing") == 1:
                print "FOUND READ2"
                write = True
        
        if write == True:
            outR1.write(line)
            outR2.write(line2)    
            
        if linecount == 4:
            readcount += 1
            linecount = 0           
            write = False
            
            

if __name__ == "__main__":
    
    import argparse
    
    parser = argparse.ArgumentParser(description="Extract reads from SAM")
    parser.add_argument("sam", help="path to sam file.", type=str)
    parser.add_argument("r1", help="path to r1", type=str)
    parser.add_argument("r2", help="path to r2", type=str)
    parser.add_argument("r1out", help="path to new r1", type=str)
    parser.add_argument("r2out", help="path to new r2", type=str)


    args = parser.parse_args()
    
    samfile = open(args.sam)
    readR1 = open(args.r1)
    readR2 = open(args.r2)
    
    r1Out = open(args.r1out)
    r2Out = open(args.r2out)
        
    
    rDict = createReadDict(samfile)
    getReads(rDict, readR1, readR2, r1Out, r2Out)
    
    print rDict
    
    
    
