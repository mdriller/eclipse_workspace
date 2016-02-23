'''
Created on 09.06.2015

@author: maxdriller
'''
import argparse


def buildAnnoDICT(assemInfo, annoDict):

    infoReader = open(assemInfo)
    
    
    
    for line in infoReader:
        if not line.startswith("#"):
            scafNo = line.split("\t")[0]
            genBankID = line.split("\t")[4].split(".")[0]
            
            annoDict[genBankID] = scafNo
    
    
    infoReader.close()


            
parser = argparse.ArgumentParser(description="Extract reads from BLASTed Contigs")
parser.add_argument("blast6", help="path and name of blastfile in tab format", type=str)
parser.add_argument("assemInf", help="path and name of assembly info file", type=str)
parser.add_argument("output", help="path and name of outputfile(.fasta)", type=str)

args = parser.parse_args()

instream = open(args.blast6)
outstream = open(args.output, "w")

annotDict = {}

buildAnnoDICT(args.assemInf, annotDict)

outstream.write("#ScafId" + "\t" + "ScafGenBank" + "\t" + "length" + "\t" + "ScafStart"+ "\t" + "ScafEnd" + "\t" + "mt_Start" + "\t" + "mtEnd" + "\t" + "eval "+ "\t" + "BitScore" + "\t" + "pIdent" + "\n")

for line in instream:
        splitted = line.split("\t")
        genBank = splitted[2]
        outstream.write(annotDict[genBank] + "\t" + genBank + "\t" + splitted[4] + "\t" + splitted[9] + "\t" + splitted[10] + "\t" + splitted[7] + "\t" + splitted[8] + "\t" + splitted[11] + "\t" + splitted[12] + "\t" + splitted[3] + "\n")
