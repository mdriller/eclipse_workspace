'''
Created on 08.12.2014

@author: maxdriller
'''

import sys
from Bio import SeqIO
from Bio.SeqIO.QualityIO import phred_quality_from_solexa

#def readfastAfile(inStream):
 #   for line in inStream:
 #       if line.startswith(">"):
 #           #print line
 #           continue
 #       else:
 #           print line.replace("T", "t")
 #           continue



#if len(sys.argv) > 1:
#    inStream = open(sys.argv[1], "r")
#    readfastAfile(inStream)

#else:
#    print "ERROR - no input file!"

#SeqIO.convert("reads.fastq", "fastq-illumina", "reads.fasta", "fasta")


#SeqIO.convert("splitreads1.fastq", "fastq-illumina", "splitreads1.fasta", "fasta")



'''
def checkPaired(stream):
    
    count1 = 0
    count2 = 0
    
    for line in stream:
        if line.startswith("@M01271"):
        #if line.startswith("@Tthymallus"): 
            #print line.split(" ")[1].split(":")[0]
            
            #fuer format: 1:N:0:15 oder 2:N:0:15
            id = line.split(" ")[1].split(":")[0]
            
            #fuer format /1 oder /2
            #id = line.split("/")[1].strip("\n")
            #print id
            if id == "1":
                count1 = count1 + 1
                #print 1
                #out1.write(line)
                #x = 3
            
            if id == "2":
                count2 = count2 + 1
                #print 2
                #out2.write(line)
                #y = 3
                
        #elif x > 0:
            #out1.write(line)
            #x -= 1
       #elif y > 0:
            #out2.write(line)
            #y -= 1
            
        
    return count1, count2

#stream1 = open("/home/maxdriller/Schreibtisch/Praktikum/Azza/raw/S10.fastq", "r")
#stream1 = open("/home/maxdriller/Schreibtisch/Praktikum/Azza/S15MIRA+MITObim2/S15onlyPairedR.fastq")
#stream1 = open("/home/maxdriller/Schreibtisch/Praktikum/Azza/S15mapping/S15toEquusGrevyG51/S15equusGrevyG51Reads.fastq")
#stream1 = open("/home/maxdriller/Schreibtisch/Praktikum/Azza/S15mapping/S15toEquusBurcelli2_Quagga/S15equusBurcelli_QuaggaReadsFINAL.fastq")    

stream1 = open("/home/maxdriller/Schreibtisch/Praktikum/Azza/S15mapping/S15toEquusBurcelli2_Quagga/S15equusBurcelli_QuaggaReads.fastq")

#out1 = open("/home/maxdriller/Schreibtisch/Praktikum/MITObimTest/testdata1/splitreads1.fastq", "w")
#out2 = open("/home/maxdriller/Schreibtisch/Praktikum/MITObimTest/testdata1/splitreads2.fastq", "w")


print checkPaired(stream1)
'''

    
    
