'''
Created on Jan 22, 2016

@author: maxdriller
'''
import argparse
import matplotlib.pyplot as plt

def base_per_seq_content(readpath, maxLen, pathOut):  
        
    if args.readfile.endswith(".gz"):
        import gzip
        
        readfile = gzip.open(args.readfile)
    else:
        readfile = open(args.readfile)
    
    
    arrayA = [0]*maxLen
    arrayC = [0]*maxLen
    arrayG = [0]*maxLen
    arrayT = [0]*maxLen
    totalBases = [0]*maxLen
    
    linecount = 1
    readcount = 1
    for line in readfile:
        
        if linecount == 2:
            seq = line.strip("\n")
            
            for i, char in enumerate(seq.upper()):
                                
                if char == "A":
                    arrayA[i] += 1
                    totalBases[i] += 1
                elif char == "C":
                    arrayC[i] += 1
                    totalBases[i] += 1
                elif char == "G":
                    arrayG[i] += 1
                    totalBases[i] += 1
                elif char == "T":
                    arrayT[i] += 1
                    totalBases[i] += 1
                    
        linecount += 1
        if linecount == 5:
            linecount = 1
            readcount += 1
    
    
    for i in range(0, maxLen):
        
        if totalBases[i] != 0:
            arrayA[i] = float(arrayA[i])/totalBases[i]*100
            arrayC[i] = float(arrayC[i])/totalBases[i]*100
            arrayG[i] = float(arrayG[i])/totalBases[i]*100
            arrayT[i] = float(arrayT[i])/totalBases[i]*100
            
            #error checking:
            #if arrayA[i] + arrayC[i] +arrayG[i]+ arrayT[i] != 100:
                #print "ERROR at pos: " + str(i) + "   " +  str(arrayA[i] + arrayC[i] +arrayG[i]+ arrayT[i])
            
                        
    bases = range(0, maxLen)
                   
    plt.plot(bases, arrayA, color="green", label='%A')
    plt.plot(bases, arrayC, color="blue", label='%C')
    plt.plot(bases, arrayG, color="red", label='%G')
    plt.plot(bases, arrayT, color="black", label='%T')
    plt.axis([0, maxLen, 0, 100])
    plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)
    plt.title("Base per Sequence Content")
    
    plt.savefig(pathOut + '_basePerSeqContent.pdf')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="creates an more detailed plot of the overview of base per seq content of reads than fastQC")
    parser.add_argument("readfile", help="path to your readfile", type=str)
    parser.add_argument("maxReadLen", help="maximum length of your reads", type=int)
    parser.add_argument("--out", "-outpath", help="optional: path and name of the output plot, if not used the plot will be created where the readFile is and named after it")
    args = parser.parse_args()      
     
     
    if args.out:   
        base_per_seq_content(args.readfile, args.maxReadLen, args.out)
    else:
        base_per_seq_content(args.readfile, args.maxReadLen, args.readfile)