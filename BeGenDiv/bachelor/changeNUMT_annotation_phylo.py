'''
Created on 07.10.2015

@author: maxdriller
'''

import os



if __name__ == '__main__':
    
    import argparse

    parser = argparse.ArgumentParser(description="change the annotation of the numts of phylogenetic analysis")
    parser.add_argument("numtDir", help="path and name of dir conaing all numts in fasta seqs", type=str)
    parser.add_argument("outDir", help="path and name of outputfile for info on Scafs", type=str)

    args = parser.parse_args()

    
    inPath = args.numtDir
    outPath = args.outDir

    infoWriter = open(os.path.join(outPath, "NUMTs_anno.info"), "w")
    
    numtcounter = 1
    
    for file in os.listdir(inPath):
        print file
        if file.endswith(".fasta"):

            test = open(os.path.join(inPath, file))
            newname = "numt%i_"%numtcounter + file
            testout = open(os.path.join(outPath, newname), "w")
            
            for line in test:
                if line.startswith(">"):
                    testout.write(">numt%i "%numtcounter + line[1:])
                    infoWriter.write("numt%i\t"%numtcounter + line.split(" ")[0][1:] + "\n")
                else:
                    testout.write(line)
                    
                                    
            test.close()
            testout.close()
                                
        
            numtcounter += 1
                
                
                
                