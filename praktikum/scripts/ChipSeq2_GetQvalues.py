'''
Created on 07.04.2015

@author: maxdriller
'''

instream = open("/home/maxdriller/Schreibtisch/UNI/SoftwarePraktikum-2015/analysis/MACS/MACS_qvalue0.8/MACS2/Treated-Ethanol/Treated-Ethanol_peaks.bed")
instream2 = open("/home/maxdriller/Schreibtisch/UNI/SoftwarePraktikum-2015/analysis/MACS/MACS_qvalue0.8/MACS2/Treated-Ethanol/ethanol_final2.bed")
outstream = open("/home/maxdriller/Schreibtisch/UNI/SoftwarePraktikum-2015/analysis/MACS/MACS_qvalue0.8/MACS2/Treated-Ethanol/ethanol_final2_qvalues.bed", "w")


peakqval = {}
for line in instream:
    splitted = line.split("\t")
    pid = splitted[3]
    test = splitted[4]
    peakqval[pid] = splitted[4]


for line in instream2:
    line.strip("\n")
    splitted = line.split("\t")
    pid = splitted[4]
    qval = peakqval[pid]
    outstream.write(line.strip("\n") + "\t" + qval)

instream.close()
instream2.close()
outstream.close()
