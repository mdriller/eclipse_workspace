'''
Created on 09.06.2015

@author: maxdriller
'''
import argparse
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os
#import psutil
#import memory_profiler

#read in info file(modified blast tab-output)
#--> creates NUMTdict with the Scaf as a key and the numtpositions in the scaffold as a list
#--> also creates NUMTnames (dictionary) which contains the numt-positions in the mtgenome for all Scafs
#@profile
def getNUMTinfo(infostream, NUMTdict, names, NUMTlen=0):
    
    for line in infostream:
        if not line.startswith("#"):
            splitted = line.split("\t")
            numtID = splitted[0]
            sId = splitted[1]
            sAnno = splitted[2]
            start = int(splitted[4])-1
            end = int(splitted[5])-1
            
            n_len = int(splitted[3])
            # check if NUMT longer than threshold
            if n_len >= NUMTlen:
            # store numts indices in scafs in NUMTdict and the mt indices for names in namesDICT
                if NUMTdict.get(sId, "missing") == "missing":
                    NUMTdict[sId] = [[start, end]]
                    names[sId] = [[int(splitted[6])-1, int(splitted[7])-1, numtID, sAnno]]
                else:
                    NUMTdict[sId].append([start, end])
                    names[sId].append([int(splitted[6])-1, int(splitted[7])-1, numtID, sAnno])

#@profile
#uses the NUMTdict to extract the numts form each Scaffold and puts them into folders for each Scaffold            
def getScafs(scafstream, NUMTdict, outpath, names, flank=0):
    
    #checks is path laready exitsts
    if not os.access(outpath + "/NUMTS", os.F_OK):
        os.makedirs(outpath + "/NUMTS")
    #create info-file with information on Scaffolds
    infoStream=open(outpath+"/"+"Scaffs_info.txt", "w")
    infoStream.write("scaf_name" + " " + "scaf_id" + "\t" + "scaf_len" + "\t" + "#Ns" + "\t" + "%Ns" + "\t" + "total_numt_len" + "\t" + "%numts" + "\n")
    for scaf in scafstream:

        s_name = scaf.description.split("-")[2]
        if not s_name.startswith("S"):
            s_name = scaf.description.split("-")[3]
        s_mt = 0
        #print sId
            
        if NUMTdict.get(s_name, "missing") != "missing":
            numtlist = NUMTdict[s_name]  
            namelist = names[s_name]
        
        
            if args.ns == False:
                if not os.access(outpath + "/NUMTS/" + s_name, os.F_OK):
                    os.mkdir(outpath + "/NUMTS/" + s_name)
                
            for idx, numt in enumerate(numtlist):                    
                
                if numt[0] < numt[1]:
                    if numt[0] - flank >= 0:    
                        start = numt[0] - flank
                    else:
                        start = 0
                        
                    if numt[1] + flank <= len(scaf.seq):
                        end = numt[1] + flank
                    else:
                        end = len(scaf.seq)
                else:
                    if numt[1] - flank >= 0:    
                        end = numt[1] - flank
                    else:
                        end = 0
                        
                    if numt[0] + flank <= len(scaf.seq):
                        start = numt[0] + flank
                    else:
                        start = len(scaf.seq)
                        
                      
                
                
                newnumt = SeqRecord("", "fasta")
                newnumt.id = "numt" + namelist[idx][2] + " "+ s_name + "_" + str(start) + "-" + str(end) + " " + namelist[idx][3]
                #newnumt.description = "bases from: " + str(start) + "-" + str(end)
                
                if end > start:
                    name = "numt" + namelist[idx][2] + "_"+ str(namelist[idx][0]) + "-" + str(namelist[idx][1])
                    newnumt.seq = scaf.seq[start:end]    
                else:           
                    name = "numt" + namelist[idx][2] + "_"+ str(namelist[idx][1]) + "-" + str(namelist[idx][0])
                    newnumt.seq = scaf.seq[end:start]
                    name = name + "_reverse"

                    
                #SeqIO.write(newnumt, outpath + "/NUMTS/" + sId + "/" + str(start) + "-" + str(end) + ".fasta", "fasta")
                if args.ns:
                    SeqIO.write(newnumt, outpath + "/NUMTS/" + name + ".fasta", "fasta")
                elif args.a:
                    SeqIO.write(newnumt, outpath + "/NUMTS/" + s_name + "/mt:_" + name + "_nc:_" + str(start) + "-" + str(end) + ".fasta", "fasta")
                else:
                    SeqIO.write(newnumt, outpath + "/NUMTS/" + s_name + "/" + name + ".fasta", "fasta")
                
                    
                s_mt += len(newnumt.seq)
            #write info File
            s_id = scaf.id
            s_len = len(scaf.seq)               
            s_Ns = scaf.seq.count("N")
            #print float(s_Ns)/float(s_len)
            perc_Ns = float(s_Ns)/float(s_len)*100
            perc_mt = float(s_mt)/float(s_len)*100
            
            if perc_mt + perc_Ns > 85:
                infoStream.write(s_name + " " + s_id + "\t" + str(s_len) + "\t" + str(s_Ns) + "\t" + str(perc_Ns) + "\t" + str(s_mt) + "\t" + str(perc_mt) + "\t DANGER -> mt+Ns percentage too high!!!" + "\n")
            else:
                infoStream.write(s_name + " " + s_id + "\t" + str(s_len) + "\t" + str(s_Ns) + "\t" + str(perc_Ns) + "\t" + str(s_mt) + "\t" + str(perc_mt) + "\n")

        
                          

          
parser = argparse.ArgumentParser(description="Extract reads from BLASTed Contigs")
parser.add_argument("NUMTinfo", help="path and name of blastfile in tab format", type=str)
parser.add_argument("ScaffFasta", help="path and name of Scaffolds in fasta format", type=str)
parser.add_argument("output", help="path where all folders and files will be created", type=str)
parser.add_argument("--ns", "-noscaf", help="enable = output not ordered by scafs they were extracted from", action="store_true")
parser.add_argument("--a", "-all", help="enable = output named by both indices of nc and mt genome", action="store_true")
parser.add_argument("--fl", "-flank", help="extracts surrounding(upstream AND downstream) regions, flanking the NUMT", type=int)
parser.add_argument("--len", "-length", help="length threshold for NUMTs", type=int)

args = parser.parse_args()

#open files in readmode --> biopython for fasta-seqs(beacuase its way more comfortable for working with subseqs)
infoNUMTs = open(args.NUMTinfo)
scaffs = SeqIO.parse(args.ScaffFasta, "fasta")
#get path for output folders & files
path = args.output
#create empty dictonaries
NUMTsdict = {}
NUMTsnames = {}
#
if args.len:
    getNUMTinfo(infoNUMTs, NUMTsdict, NUMTsnames, args.len)
else:
    getNUMTinfo(infoNUMTs, NUMTsdict, NUMTsnames)

#for scaf in NUMTsdict:
#    print scaf + " " + str(NUMTsdict[scaf])
    
#
if args.fl: 
    getScafs(scaffs, NUMTsdict, path, NUMTsnames, args.fl)
else:
    getScafs(scaffs, NUMTsdict, path, NUMTsnames)


infoNUMTs.close()
scaffs.close()

#prints a list with the scafs which contain more than one numt --> for merging
for key in NUMTsdict:
    
    nr_numts = len(NUMTsdict[key])
    if nr_numts > 1:
        print key, nr_numts, NUMTsdict[key]
        
        
        
