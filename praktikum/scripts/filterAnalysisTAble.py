'''
Created on 06.04.2015

@author: maxdriller
'''

instream = open("/home/maxdriller/Schreibtisch/UNI/SoftwarePraktikum-2015/analysis/merged/PWM-microarray/3_top100_merged_PWM_micro.bed")
outstream = open("/home/maxdriller/Schreibtisch/UNI/SoftwarePraktikum-2015/analysis/merged/PWM-microarray/3_top100_merged_PWM_micro_FILTERED.bed", "w")


line1 = instream.readline()
splitl1 = line1.split("\t")
outstream.write(splitl1[1] + "\t" + splitl1[2] +"\n")
for line in instream:
    splitted = line .split("\t")
    outstream.write(splitted[1] + "\t" + splitted[2] + "\t" + splitted[3] +"\n")

