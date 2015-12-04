'''
Created on 30.03.2015

@author: maxdriller
'''


tRAPstream = open("/home/maxdriller/Schreibtisch/UNI/SoftwarePraktikum-2015/analysis/PWM-Genome-Scan/2000bp-promoter-seqs-NEW-tRAP.bed")
outstream = open("/home/maxdriller/Schreibtisch/UNI/SoftwarePraktikum-2015/analysis/PWM-Genome-Scan/2000bp-promoter-seqs-FINAL.bed", "w")


for line in tRAPstream:
    if not line.startswith("#"):
        splitted = line.split("\t")
        
        start = int(splitted[0].split(":")[1].split("-")[0])
        end = int(splitted[0].split(":")[1].split("-")[1])
        
        #print start
        #print end
        hg19annostream = open("/home/maxdriller/Schreibtisch/UNI/SoftwarePraktikum-2015/SoftwarePraktikum/data/PWM-Genome-Scan/files-for-trap/hg19_annotation.bed")
        
        for hg19line in hg19annostream:
            hg19splitted = hg19line.split("\t")
            
            #print "comparing: " + (splitted[0].split(":")[1].split("-")[0]) + " "+ (hg19splitted[1])
            if hg19splitted[5] == "-":
                if (int(hg19splitted[2]) - 1000) == start:
                    #print "found reversed"
                    outstream.write(line.strip("\n") + "\t" + hg19splitted[3] + "\n")
                    break 
            
            else:
                if (int(hg19splitted[1]) - 1000) == start:
                    #print "found it"
                    outstream.write(line.strip("\n") + "\t" + hg19splitted[3] + "\n")
                    break
            
        hg19annostream.close()
                