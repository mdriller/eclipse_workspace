'''
Created on 10.04.2015

@author: maxdriller
'''

import argparse
import os
import subprocess

def getFlagstats(inpath, outpath):
    
    filelist = os.listdir(inpath)
    filelist
    bamlist = [] 
    
    outstream = open(outpath, "w")

        
    for file in filelist:
        
        if file.endswith(".bam"):
            #sys.stdout.write("\"" + file.split("_")[0]+"_"+file.split("_")[1] +"\", ")
            bamlist.append(file)
            
    print bamlist
            
    flaglist =[]        
    print bamlist
    for bam in bamlist:
        print bam
        x = subprocess.Popen("samtools flagstat "+inpath+bam, shell=True, stdout=subprocess.PIPE).stdout
        outstream.write(bam.split("_")[0] + "_" + bam.split("_")[1] + "\t")
        flaglist.append(x)
    
    outstream.write("\n")
    
    #print len(flaglist)
    
    for i in range(0,10):
        for flag in flaglist:
            line = flag.readline()
            outstream.write(line.strip("\n") + "\t")
            print "written line: " + str(i)
            print line
        outstream.write("\n")  
    outstream.write("\n")       
    
    outstream.close()
    
#########################

parser = argparse.ArgumentParser(description="create a tab seperated file containing all the falgstats for each bam file of a set")
parser.add_argument("inpath", help="path and name of the directory containg all the (indexed!)bam files")
parser.add_argument("outpath", help="path and name of the output file that will be created")
args = parser.parse_args()

   

#path1 ="/home/maxdriller/Schreibtisch/Praktikum/sloths/mapping/BTR/"
#path2 ="/home/maxdriller/Schreibtisch/Praktikum/sloths/assemblies/BTR-139/mapping/assemblies_mapped/mapping/"

getFlagstats(args.inpath, args.outpath)
