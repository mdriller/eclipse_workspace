'''
Created on 03.11.2015

@author: maxdriller
'''


def getIndices(indiStream, r1In, r2In, outDir):

    namelist=[]
    for line in indiStream:
        
        if len(line) > 10:
            splitted = line.strip("\n").split("\t")
            
            
            for i, idx in enumerate(splitted):
                if i == 0:
                    print idx
                
                else:
                    rDict[idx] = splitted[0]  
                    
                    if not splitted[0] in namelist:
                        namelist.append(splitted[0])
    print namelist
    
    #namesr1 = [""]*len(namelist)
    #namesr2 = [""]*len(namelist)
    for i, name in enumerate(namelist):
        #namesr1[i-1] = open("/home/maxdriller/Schreibtisch/test/" + name + "_R1.fastq", "w")
        #namesr2[i-1] = open("/home/maxdriller/Schreibtisch/test/" + name + "_R2.fastq", "w")
        
        open(outDir + "/" + name + "_R1.fastq", "w").close()
        open(outDir + "/" + name + "_R2.fastq", "w").close()
    
    linecount = 0
    readcount = 1    
     
    write = False 
        
    for line in r1In:
        line2 = r2In.readline()
        
        linecount += 1
        
        if rDict.get(str(readcount), "missing") != "missing":
            name = rDict[str(readcount)]
            write = True
            #print "found it"
            open(outDir + "/" + name + "_R1.fastq", "a").write(line)
            open(outDir + "/" + name + "_R2.fastq", "a").write(line2)
            
    
        if linecount == 4:
            readcount += 1
            linecount = 0 
            write = False
            
            

if __name__ == "__main__":
    
    import argparse
    import gzip
    
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("indices", help="", type=str)
    parser.add_argument("r1In", help="", type=str)
    parser.add_argument("r2In", help="", type=str)
    parser.add_argument("outPath", help="", type=str)
    #parser.add_argument("r1Out", help="", type=str)
    #parser.add_argument("r2Out", help="", type=str)
    
    args = parser.parse_args()
        
    indicesIn = open(args.indices)
    forwardIn = gzip.open(args.r1In)
    reverseIn = gzip.open(args.r2In)
    
    outPath = args.outPath
    
    rDict = {}

    
    getIndices(indicesIn, forwardIn, reverseIn, outPath)
    