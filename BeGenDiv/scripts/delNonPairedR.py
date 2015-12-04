'''
Created on 26.01.2015

@author: maxdriller
'''

def delNonPairedReads(stream):
    list = []
    
    for line in stream:
              
        if line.startswith("@M01271"):
            id = line.split("-")[1].split(" ")[0]
            #print id
                 
            if id in list:
                list.remove(id)
            else:    
                list.append(id)
                #print "appended"
            
    return list
    
    
def writeOnlyPaired(stream, outstream, list):
    x = 0
    
    for line in stream:
              
        if line.startswith("@M01271"):
            #print "hallo"
            
            id = line.split("-")[1].split(" ")[0]
            
            if id not in list:
                outstream.write(line)
                x = 3
        
        elif x > 0:
            outstream.write(line)  
            

#stream1 = open("/home/maxdriller/Schreibtisch/Praktikum/Azza/S15MIRA+MITObim2/S15finalreads2.fastq")
stream1 = open("/home/maxdriller/Schreibtisch/Praktikum/Azza/S15mapping/S15toEquusGrevyG51/S15equusGrevyG51Reads.fastq")

nonPairedList = delNonPairedReads(stream1)
stream1.close()


print nonPairedList

#stream1 = open("/home/maxdriller/Schreibtisch/Praktikum/Azza/S15MIRA+MITObim2/S15finalreads2.fastq")
#outstr = open("/home/maxdriller/Schreibtisch/Praktikum/Azza/S15MIRA+MITObim2/S15onlyPairedR.fastq", "w")

#stream1 = open("/home/maxdriller/Schreibtisch/Praktikum/Azza/S15/S15equusGrevyReads.fastq")
#outstr = open("/home/maxdriller/Schreibtisch/Praktikum/Azza/S15/S15equusGrevyReadsFINAL.fastq","w")

#stream1 = open("/home/maxdriller/Schreibtisch/Praktikum/Azza/S15mapping/S15toEquusGrevyG51/S15equusGrevyG51Reads.fastq")
#outstr = open("/home/maxdriller/Schreibtisch/Praktikum/Azza/S15mapping/S15toEquusGrevyG51/S15equusGrevyG51ReadsFINAL.fastq","w")

#stream1 = open("/home/maxdriller/Schreibtisch/Praktikum/Azza/S15mapping/S15toEquusBurcelli2_Quagga/S15equusBurcelli_QuaggaReads.fastq")    
#outstr = open("/home/maxdriller/Schreibtisch/Praktikum/Azza/S15mapping/S15toEquusBurcelli2_Quagga/S15equusBurcelli_QuaggaReadsFINAL.fastq", "w") 

stream1 = open("/home/maxdriller/Schreibtisch/Praktikum/Azza/S15mapping/S15toHyena/MIRA/S15_blastedreads_hyena.fastq")    
outstr = open("/home/maxdriller/Schreibtisch/Praktikum/Azza/S15mapping/S15toHyena/MIRA/S15_blastedreads_hyenaPAIRED.fastq", "w") 


writeOnlyPaired(stream1, outstr, nonPairedList)

stream1.close()
outstr.close()

