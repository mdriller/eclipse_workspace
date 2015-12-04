'''
Created on 09.11.2015

@author: maxdriller
'''

def countIndices(fastqStream, indiDict, tabOut):
    
    linecount = 0
    readcount = 1  
    
    for line in fastqStream:
        linecount += 1  
        
        
        if linecount == 1:
            indices = line.strip("\n").split(" ")[1].split(":")[3]
            #print indices
            
            if indiDict.get(indices, "missing") == "missing":
                indiDict[indices] = 1
            else:
                indiDict[indices] += 1                 
            
        
        if linecount == 4:
            readcount += 1
            linecount = 0 
        
    
    for idx in indiDict:
        tabOut.write(str(idx) + "\t" + str(indiDict[idx]) + "\n")

if __name__ == "__main__":
    
    import argparse
    import gzip
    
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("indices", help="", type=str)
    parser.add_argument("outFile", help="", type=str)
    
    args = parser.parse_args()
    
    
    indicesIn = gzip.open(args.indices)
    
    outWriter = open(args.outFile, "w")
    
    indexDICT = {}
    
    countIndices(indicesIn, indexDICT, outWriter)
    
    print indexDICT
    
    
    

    