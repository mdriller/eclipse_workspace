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
def getNUMTinfo(infostream, NUMTdict, names):
    
    for line in infostream:
        if not line.startswith("#"):
            splitted = line.split("\t")
            sId = splitted[0]
            
            if int(splitted[1]) >= 1:
                start = int(splitted[2])-1
                end = int(splitted[3])-1
            
                if NUMTdict.get(sId, "missing") == "missing":
                    NUMTdict[sId] = [[start, end]]
                    names[sId] = [[int(splitted[4])-1, int(splitted[5])-1]]
                else:
                    NUMTdict[sId].append([start, end])
                    names[sId].append([int(splitted[4])-1, int(splitted[5])-1])

#@profile
#uses the NUMTdict to extract the numts form each Scaffold and puts them into folders for each Scaffold            
def getScafs(scafstream, NUMTdict, outpath, names, infoStream):
   
    os.mkdir(outpath + "/NUMTS")
    infoStream.write("scaf_name" + " " + "scaf_id" + "\t" + "scaf_len" + "\t" + "#Ns" + "\t" + "%Ns" + "\t" + "total_numt_len" + "\t" + "%numts" + "\n")
    for scaf in scafstream:
        sId = scaf.description.split(" ")[8].strip(",")
        s_mt = 0
        #print sId
            
        if NUMTdict.get(sId, "missing") != "missing":
            numtlist = NUMTdict[sId]  
            namelist = names[sId]
            
            if args.ns == False:
                os.mkdir(outpath + "/NUMTS/" + sId)
                
            for idx, numt in enumerate(numtlist):                       
                   
                start = numt[0]
                end = numt[1]
                name = str(namelist[idx][0]) + "-" + str(namelist[idx][1])
                
                newnumt = SeqRecord("", "fasta")
                newnumt.id = sId + "_" + str(start) + "-" + str(end)
                #newnumt.description = "bases from: " + str(start) + "-" + str(end)
                
                if end > start:
                    newnumt.seq = scaf.seq[start:end]    
                else:           
                    newnumt.seq = scaf.seq[end:start]
                    name = name + "_reverse"

                    
                #SeqIO.write(newnumt, outpath + "/NUMTS/" + sId + "/" + str(start) + "-" + str(end) + ".fasta", "fasta")
                if args.ns:
                    SeqIO.write(newnumt, outpath + "/NUMTS/" + name + ".fasta", "fasta")
                elif args.a:
                    SeqIO.write(newnumt, outpath + "/NUMTS/" + sId + "/mt:_" + name + "_nc:_" + str(start) + "-" + str(end) + ".fasta", "fasta")
                else:
                    SeqIO.write(newnumt, outpath + "/NUMTS/" + sId + "/" + name + ".fasta", "fasta")
                
                    
                s_mt += len(newnumt.seq)
            #write info File
            s_id = scaf.id
            s_name = scaf.description.split(" ")[8].strip(",")
            s_len = len(scaf.seq)               
            s_Ns = scaf.seq.count("N")
            #print float(s_Ns)/float(s_len)
            perc_Ns = float(s_Ns)/float(s_len)*100
            perc_mt = float(s_mt)/float(s_len)*100
            
            if perc_mt + perc_Ns > 85:
                infoStream.write(s_name + " " + s_id + "\t" + str(s_len) + "\t" + str(s_Ns) + "\t" + str(perc_Ns) + "\t" + str(s_mt) + "\t" + str(perc_mt) + "\t DANGER -> mt/Ns percentage to high!!!" + "\n")
            else:
                infoStream.write(s_name + " " + s_id + "\t" + str(s_len) + "\t" + str(s_Ns) + "\t" + str(perc_Ns) + "\t" + str(s_mt) + "\t" + str(perc_mt) + "\n")

#@profile
#uses the NUMTdict to extract the numts form each Scaffold and puts them into folders for each Scaffold            
def getScafs2(scafstream, NUMTdict, outpath, names, infoStream, flank=0):
   
    os.mkdir(outpath + "/NUMTS")
    infoStream.write("scaf_name" + " " + "scaf_id" + "\t" + "scaf_len" + "\t" + "#Ns" + "\t" + "%Ns" + "\t" + "total_numt_len" + "\t" + "%numts" + "\n")
    for scaf in scafstream:
        sId = scaf.description.split(" ")[8].strip(",")
        s_mt = 0
        #print sId
            
        if NUMTdict.get(sId, "missing") != "missing":
            numtlist = NUMTdict[sId]  
            namelist = names[sId]
            
            if args.ns == False:
                os.mkdir(outpath + "/NUMTS/" + sId)
                
            for idx, numt in enumerate(numtlist):                    
                
                if numt[0] - flank >= 0:    
                    start = numt[0] - flank
                else:
                    start = 0
                    
                if numt[1] + flank > len(scaf.seq):
                    end = numt[1] + flank
                else:
                    end = len(scaf.seq)
                      
                name = str(namelist[idx][0]) + "-" + str(namelist[idx][1])
                
                newnumt = SeqRecord("", "fasta")
                newnumt.id = sId + "_" + str(start) + "-" + str(end)
                #newnumt.description = "bases from: " + str(start) + "-" + str(end)
                
                if end > start:
                    newnumt.seq = scaf.seq[start:end]    
                else:           
                    newnumt.seq = scaf.seq[end:start]
                    name = name + "_reverse"

                    
                #SeqIO.write(newnumt, outpath + "/NUMTS/" + sId + "/" + str(start) + "-" + str(end) + ".fasta", "fasta")
                if args.ns:
                    SeqIO.write(newnumt, outpath + "/NUMTS/" + name + ".fasta", "fasta")
                elif args.a:
                    SeqIO.write(newnumt, outpath + "/NUMTS/" + sId + "/mt:_" + name + "_nc:_" + str(start) + "-" + str(end) + ".fasta", "fasta")
                else:
                    SeqIO.write(newnumt, outpath + "/NUMTS/" + sId + "/" + name + ".fasta", "fasta")
                
                    
                s_mt += len(newnumt.seq)
            #write info File
            s_id = scaf.id
            s_name = scaf.description.split(" ")[8].strip(",")
            s_len = len(scaf.seq)               
            s_Ns = scaf.seq.count("N")
            #print float(s_Ns)/float(s_len)
            perc_Ns = float(s_Ns)/float(s_len)*100
            perc_mt = float(s_mt)/float(s_len)*100
            
            if perc_mt + perc_Ns > 85:
                infoStream.write(s_name + " " + s_id + "\t" + str(s_len) + "\t" + str(s_Ns) + "\t" + str(perc_Ns) + "\t" + str(s_mt) + "\t" + str(perc_mt) + "\t DANGER -> mt/Ns percentage to high!!!" + "\n")
            else:
                infoStream.write(s_name + " " + s_id + "\t" + str(s_len) + "\t" + str(s_Ns) + "\t" + str(perc_Ns) + "\t" + str(s_mt) + "\t" + str(perc_mt) + "\n")

        
                          

          
parser = argparse.ArgumentParser(description="Extract reads from BLASTed Contigs")
parser.add_argument("NUMTinfo", help="path and name of blastfile in tab format", type=str)
parser.add_argument("ScaffFasta", help="path and name of Scaffolds in fasta format", type=str)
parser.add_argument("output", help="path where all folders and files will be created", type=str)
parser.add_argument("--ns", "-noscaf", help="enable = output not ordered by scafs they were extracted from", action="store_true")
parser.add_argument("--a", "-all", help="enable = output named by both indices of nc and mt genome", action="store_true")
parser.add_argument("--fl", "-flank", help="extracts surrounding(upstream AND downstream) regions, flanking the NUMT", type=int)

args = parser.parse_args()

#open files in readmode --> biopython for fasta-seqs(beacuase its way more comfortable for working with subseqs)
infoNUMTs = open(args.NUMTinfo)
scaffs = SeqIO.parse(args.ScaffFasta, "fasta")
#get path for output folders & files
path = args.output
#create info-file with information on Scaffolds
infoWriter=open(path+"/"+"Scaffs_info.txt", "w")
#create empty dictonaries
NUMTsdict = {}
NUMTsnames = {}
#
getNUMTinfo(infoNUMTs, NUMTsdict, NUMTsnames)

#for scaf in NUMTsdict:
#    print scaf + " " + str(NUMTsdict[scaf])
    
#
if args.fl: 
    getScafs2(scaffs, NUMTsdict, path, NUMTsnames, infoWriter, args.fl)
else:
    getScafs(scaffs, NUMTsdict, path, NUMTsnames, infoWriter)


infoNUMTs.close()
scaffs.close()

#prints a list with the scafs which contain more than one numt --> for merging
for key in NUMTsdict:
    
    nr_numts = len(NUMTsdict[key])
    if nr_numts > 1:
        print key, nr_numts, NUMTsdict[key]
        
        
        
