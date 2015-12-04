'''
Created on 30.10.2015

@author: maxdriller
'''

#script to sort unassigned reads with one correct index to single files for analysis


def createIndexDict(sampleSheet):
   
    
    indices = 0
    
    for line in sampleSheet:
        if line.startswith("[Data]"):
            indices = 1
            #print "---> " + line
        elif indices == 1:
            indices = 2       
        
        elif indices == 2:
            splitted = line.strip("\n").split(",")
            name = splitted[0]
            p5idx = splitted[7] 
            p7idx = splitted[5]
            print name, p7idx, p5idx
            
            p5iDict[p5idx] = [name]
            p7iDict[p7idx] = [name]

def getReadIDs
(indexStream):
    
    linecount = 0
    readcount = 1
    
    #r1line = ""
    #r2line = ""
    
    write = False
    
    for line in indexStream:
        #r1line = r1In.readline()
        #r2line = r2In.readline()
        
        linecount += 1
        
        if linecount == 1:
            p7i = line.split(":")[-1].split("+")[0]
            p5i = line.split(":")[-1].split("+")[1].strip("\n")
        
            #print p7i, p5i
            
            if p7iDict.get(p7i, "missing") != "missing":
                #print "FOUND p7 " + p7iDict[p7i]
                write = True
                p7iDict[p7i].append(readcount)
            
            
            if p5iDict.get(p5i, "missing") != "missing":
                #print "FOUND p5 ", p5iDict[p5i]
                write = True
                p5iDict[p5i].append(readcount)
                        
        #if write == True:
            #print r1line.strip("\n")
            #print r2line
            
            #r1Out.write(r1line)
            #r2Out.write(r2line)
            
        
        
        if linecount == 4:
            readcount += 1
            linecount = 0 
            write = False
                      

if __name__ == "__main__":
    
    import argparse
    import gzip
    
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("SampleSheet", help="", type=str)
    parser.add_argument("undetIndices", help="", type=str)
    #parser.add_argument("indices2", help="", type=str)
    #parser.add_argument("r1", help="", type=str)
    #parser.add_argument("r2", help="", type=str)
    parser.add_argument("indicesP7Out", help="", type=str)
    parser.add_argument("indicesP5Out", help="", type=str)
    #parser.add_argument("r2Out", help="", type=str)
    
    args = parser.parse_args()
    
    sSheet = open(args.SampleSheet)
    p7indices = gzip.open(args.undetIndices)
    #r1Infile = gzip.open(args.r1)
    #r2Infile = gzip.open(args.r2)
    
    #r1Outfile = open(args.r1Out, "w")
    #r2Outfile = open(args.r2Out, "w")
    indicesP7Out = open(args.indicesP7Out, "w")
    indicesP5Out = open(args.indicesP5Out, "w")
    p5iDict = {}
    p7iDict = {}
    createIndexDict(sSheet)
    
    #print p7iDict
    
    getReadIDs(p7indices)
    
    print "\n"
    print "p7 Indices:\n"  
      
    for idx in p7iDict:
        indicesP7Out.write(idx + "\n")
        print p7iDict[idx][0] + " " + str(len(p7iDict[idx])-1)
        for i in p7iDict[idx]:
            indicesP7Out.write(str(i) + "\t")
            
        indicesP7Out.write("\n")
    
    print "\n\n"
    print "p5 Indices:\n"
    
    for idx in p5iDict:
        indicesP5Out.write(idx + "\n")
        print p5iDict[idx][0] + " " + str(len(p5iDict[idx])-1)
        for i in p5iDict[idx]:
            indicesP5Out.write(str(i) + "\t")
            
        indicesP5Out.write("\n")
    
    