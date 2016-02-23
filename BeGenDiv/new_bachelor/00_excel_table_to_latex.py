'''
Created on 01.02.2016

@author: maxdriller
'''

import argparse

parser = argparse.ArgumentParser(description="Extract reads from BLASTed Contigs")
parser.add_argument("csvIn", help="tab seperated fileas input", type=str)
parser.add_argument("out", help="text file of table in latex table style", type=str)

args = parser.parse_args()

outWriter = open(args.out, "w")
inFile = open(args.csvIn)

outWriter.write("\begin{longtable}{|")
firstLineSplit = inFile.readline().strip("\n").split("\t")

for tab in firstLineSplit:
    outWriter.write(" p{1.5cm} |")
    #outWriter.write(" l")
outWriter.write("}"+"\n")


outWriter.write("\t"+"\caption[ADDNAME]{ADD TEXT}"+"\n")
outWriter.write("\t"+"\label{tab:ADDNAME}"+"\n")
outWriter.write("\t"+"\centering"+"\n")
#outWriter.write("\t"+"\begin{tabular}{")

 

for x, tab in enumerate(firstLineSplit):
            
    if x == len(firstLineSplit)-1:
        outWriter.write("\t" + tab + "\\\ \hline" + "\n")
    else:
        outWriter.write("\t" + tab +" &")

for line in inFile:
    splitted = line.strip("\n").split("\t")
    
    for x, tab in enumerate(splitted):
        
        if x == len(splitted)-1:
            outWriter.write("\t" + tab + "\\\ \hline" + "\n")
        else:
            outWriter.write("\t" + tab +" &")
    


outWriter.write("\end{longtable}"+"\n")