'''
Created on Dec 14, 2015

@author: maxdriller
'''
#anno header
# feature    class    assembly    assembly_unit    seq_type    chromosome    genomic_accession    start    end    strand    product_accession    non-redundant_refseq    related_accession    name    symbol    GeneID    locus_tag    feature_interval_length    product_length    attributes

def getreadlengths(queryFile):
    
    from Bio import SeqIO
    
    fastaStream = SeqIO.parse(queryFile, "fasta")
    
    readlens = {}
    
    for seq in fastaStream:
        readlens[seq.id] = len(seq.seq)

    return readlens

def getGenes(genomeanno):
    
    scafDict = {}
    
    s_last=""
    e_last=""
    
    #creates an overview
    for line in genomeanno:
        if not line.startswith("#"):
            
            #most of the time (not always) 3 rows per gene gene,mDNA,CD all contain the same info but not all contain the gene_id
            splitted = line.split("\t")
                
            scaf_id = splitted[6]
            start = splitted[7]
            end = splitted[8]
            id = splitted[10]
            gene_name = splitted[13]
            #print scaf_id, start, end
            #print gene_name  
            
            # cases if all info has been obtained or some is missing in this line
            if start == s_last and end == e_last:
                continue
            if gene_name == "":
                continue
            if id == "":
                continue
            
            # create new entry for start end end of gene on a scaffold (scaf id is key)          
            if scafDict.get(scaf_id, "missing") == "missing":
                scafDict[scaf_id] = [start,end]
            # if scaffold already has some genes on it append the new gene    
            else:
                scafDict[scaf_id].append([start, end, gene_name, id])
                
            s_last = start
            e_last = end
    
    return scafDict   



def checkBlastHits(blast6, scafDict, outwriter, rLens):
    for line in blast6:
        splitted = line.split("\t")
        
        #the blast hits need to have a evalue of at least e-50 (-50 important) or smaller
        # and the blast hits need to represent at least 95% of the seq length 
        hit_len = splitted[3]
        eVal = splitted[10]
        hitLen = splitted[3]
        pIdent = splitted[2]
        
        #print eVal
        if eVal != "0.0":
            if int(eVal.split("-")[1]) < 50:
                continue 
        if float(hit_len)/rLens[splitted[0]]*100 < 95:
            continue
        
        scaf_id = splitted[1].split("|")[3]
        scaf_start = splitted[8]
        scaf_end = splitted[9]
        
        #print scaf_id, scaf_start, scaf_end
        # check if scaffold of hit has some genes on it
        if scafDict.get(scaf_id, "missing") != "missing":
            #print scafDict[scaf_id]           
            # check for every gene on the scaffold if the blast hit is in range
            for gene in scafDict[scaf_id]:
                #print gene[0]
                if int(scaf_start) >= int(gene[0]) and int(scaf_start) <= int(gene[1]):
                    #print "FOUND gene "+gene[2]
                    # if gene found --> write hit in output              
                    #outwriter.write(splitted[0] + "\t" + scaf_id + "\t" + scaf_start + "\t" + scaf_end +  "\t" + hitLen + "\t" + pIdent + "\t" + eVal + "\t" gene[2] + "\t" + gene[3] + "\t" + "[" + gene[0] + "-" + gene[1] + "]" + "\n")
                    outwriter.write(splitted[0] + "\t" + scaf_id + "\t" + scaf_start + "\t" + scaf_end +  "\t" + hitLen + "\t" + pIdent + "\t" + eVal+ "\t" + gene[2] + "\t" + gene[3] + "\t" + "[" + gene[0] + "-" + gene[1] + "]" + "\n")
                elif int(scaf_end) >= int(gene[0]) and int(scaf_end) <= int(gene[1]):
                    outwriter.write(splitted[0] + "\t" + scaf_id + "\t" + scaf_start + "\t" + scaf_end +  "\t" + hitLen + "\t" + pIdent + "\t" + eVal+ "\t" + gene[2] + "\t" + gene[3] + "\t" + "[" + gene[0] + "-" + gene[1] + "]" + "\n")

                
                
if __name__ == "__main__":
    
    import argparse 
    
    parser = argparse.ArgumentParser(description="check if blast hits are hits against genes")
    parser.add_argument("genomeanno", help="genome features f.e. GCA_000344595.1_CheMyd_1.0_feature_table.txt", type=str)
    parser.add_argument("queryFasta", help="fasta file containing the query/ies of the blast search", type=str)
    parser.add_argument("blast6", help="blast output in format 6 (-outfmt 6", type=str)
    parser.add_argument("outFile", help="directory where fasta files will be created", type=str)
    args = parser.parse_args()
    
    
    readLens = getreadlengths(args.queryFasta)
    
    
    genome = open(args.genomeanno)
    blastIn = open(args.blast6)
    geneList = getGenes(genome)
    outWriter = open(args.outFile, "w")
    outWriter.write("queryName" + "\t" + "scafName" + "\t" + "start" + "\t" +  "end" + "\t" + "length" + "\t" + "pIdenty" + "\t" + "eValue" + "\t" + "geneName" + "\t" + "geneID" + "\n")
    
    checkBlastHits(blastIn, geneList, outWriter, readLens)
    
    