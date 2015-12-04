'''
Created on 23.10.2015

@author: maxdriller
'''
# script to extract the numts that have been "verified" with flanking regions to then check them for correctness via mapping


#gets all the important info about the numts out of the info file [in this case: /home/maxdriller/Schreibtisch/Praktikum/Bachelor/DOKU/NUMTS_info/2_NUMTS_info2_for_R.csv]
 
def getNumtInfo(infostream, numtDict, scafDict):
    
    for line in infostream:
        
        if not line.startswith("#"):
            splitted = line.split("\t")
            #print splitted
            
            numtid = splitted[0]
            scaf = splitted[1]
            sstart = splitted[4].split("-")[0]
            send = splitted[4].split("-")[1]
            
            #print numtid
            if numtDict.get(numtid, "missing") == "missing":
                numtDict[numtid] = [sstart, send]
            
            
            if scafDict.get(scaf, "missing") == "missing":
                scafDict[scaf] = [numtid]
            
            else:
                scafDict[scaf].append(numtid)
                
                
def getScafs(scafpath, numtDict, scafDict, outPath, flank):
    
    from Bio import SeqIO
    from Bio.SeqRecord import SeqRecord
    import os
    
    
    scafs = SeqIO.parse(scafpath, "fasta")
    os.mkdir(outPath+"allNUMTS-%i-flanked"%flank)
    
    for scaf in scafs:

        slength = len(scaf.seq) -1
        sid =  scaf.description.split(" ")[8][8:].strip(",")
        print sid
        
        if scafDict.get(sid, "missing") != "missing":
            numtid = scafDict[sid] 

            for nid in numtid:              
                    
                newnumt = SeqRecord("", "fasta")
                #print "DICT: " + str(numtDict[nid])
                start = int(numtDict[nid][0])
                end = int(numtDict[nid][1])
                name = "numt%s" %nid + "_%i_flanked"%flank
                newnumt.id = name
                #print name           
                
                if end > start:
                    if (end + flank) <= slength:  
                        end += flank
                    if (start - flank) >= 0:
                        start += -flank     
                
                    newnumt.seq = scaf.seq[start:end]
                    newnumt.description = "Scaffold%s"%sid
                else: 
                    if (end - flank) >= 0:  
                        end += -flank
                    else:
                        end = 0
                    if (start + flank) <= slength:
                        start += flank     
                    else: start
                
                    newnumt.seq = scaf.seq[end:start]
                    newnumt.description = "reverse Scaffold%s"%sid
                
                print name, len(newnumt.seq)  
                
                SeqIO.write(newnumt, outPath+"allNUMTS-%i-flanked/"%flank + name + ".fasta", "fasta")
                   
               
if __name__ == "__main__":
    
    import argparse
    
    parser = argparse.ArgumentParser(description="Extract reads from BLASTed Contigs")
    parser.add_argument("NUMTinfo", help="file containing the NUMTinfo in a specific way...", type=str)
    parser.add_argument("ScafFasta", help="path and name of Scaffolds in fasta format", type=str)
    parser.add_argument("output", help="path where all files will be created", type=str)
    parser.add_argument("--fl", "-flank", help="extraction includes surrounding(upstream AND downstream) regions, flanking the NUMT default: 500", type=int, default=500)

    args = parser.parse_args() 
    
    infoFile = open(args.NUMTinfo)   
    outpath = args.output          
    flanksize = args.fl
    
    numtDICT = {}
    scafDICT = {}

    print "Starting to gather the needed info for the numts"
    getNumtInfo(infoFile, numtDICT, scafDICT)
    print "All done!"
    print "Starting the extraction with a flanksize of %i" %flanksize
    getScafs(args.ScafFasta, numtDICT, scafDICT, outpath, flanksize)
    print "All done!"
   # print scafDICT
   # print "\n\n\n"
   # print numtDICT
