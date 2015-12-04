'''
Created on 08.04.2015

@author: maxdriller
'''
import sys
from sys import argv


if len(argv) != 5:
    print "wrong call - not the right amount of arguments"
    print "please call: _.py [CHIPSEQ-final] [PWM-final] [MICROARRAY-final] [OUTPATH(no file names)]"
    exit() 

chipin = open(argv[1])
chipout = open(argv[4]+"CHIPSEQ_FISHER.bed", "w")
pwmin = open(argv[2])
pwmout = open(argv[4]+"PWM_FISHER.bed", "w")
microin = open(argv[3])
microout = open(argv[4]+"MICRO_FISHER.bed", "w")

#chipin = open("/home/maxdriller/Schreibtisch/UNI/SoftwarePraktikum-2015/analysis/MACS/MACS_qvalue0.8/MACS2/Treated-Ethanol/ethanol_final2_qvalues.bed")
#chipout = open("/home/maxdriller/Schreibtisch/UNI/SoftwarePraktikum-2015/analysis/MACS/MACS_qvalue0.8/MACS2/Treated-Ethanol/ethanol_final2_qvalues_FISHER.bed", "w")
#pwmin = open("/home/maxdriller/Schreibtisch/UNI/SoftwarePraktikum-2015/analysis/PWM-Genome-Scan/2000bp-promoter-seqs-FINAL_NO_DOUBLES.bed")
#pwmout = open("/home/maxdriller/Schreibtisch/UNI/SoftwarePraktikum-2015/analysis/PWM-Genome-Scan/2000bp-promoter-seqs-FINAL_NO_DOUBLES_FISHER.bed", "w")
#microin = open("/home/maxdriller/Schreibtisch/UNI/SoftwarePraktikum-2015/analysis/Microarray Data/microarray_FINAL_NO_DOUBLES.txt")
#microout = open("/home/maxdriller/Schreibtisch/UNI/SoftwarePraktikum-2015/analysis/Microarray Data/microarray_FINAL_NO_DOUBLES_FISHER.txt", "w")
#microout2 = open("/home/maxdriller/Schreibtisch/UNI/SoftwarePraktikum-2015/analysis/Microarray Data/microarray_FINAL_NO_DOUBLES_FISHER_geneExp.txt", "w")
#microout3 = open("/home/maxdriller/Schreibtisch/UNI/SoftwarePraktikum-2015/analysis/Microarray Data/microarray_FINAL_NO_DOUBLES_FISHER_adjPval.txt", "w")



for line in chipin:
    splitted = line.strip("\n").split("\t")
    chipout.write(splitted[15] + "\t" + splitted[16] + "\n")
    
chipin.close()
chipout.close()

for line in pwmin:
    splitted = line.strip("\n").split("\t") 
    pwmout.write(splitted[9].strip("\n") + "\t" + splitted[5] + "\n") 
    
pwmin.close()
pwmout.close()

for line in microin:
    splitted = line.strip("\n").split("\t") 
    microout.write(splitted[1] + "\t" + splitted[6] + "\n")
    #microout2.write(splitted[1] + "\t" + splitted[4] + "\n")
    #microout3.write(splitted[1] + "\t" + splitted[7] + "\n")
    
microin.close()
microout.close()