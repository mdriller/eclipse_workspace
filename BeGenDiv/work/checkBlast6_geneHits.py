'''
Created on Dec 14, 2015

@author: maxdriller
'''
#anno header
# feature    class    assembly    assembly_unit    seq_type    chromosome    genomic_accession    start    end    strand    product_accession    non-redundant_refseq    related_accession    name    symbol    GeneID    locus_tag    feature_interval_length    product_length    attributes


def getGenes(genomeanno):
    
    scafDict = {}
    
    s_last=""
    e_last=""
    
    for line in genomeanno:
        if not line.startswith("#"):
            
            #always 3 rows per gene gene,mDNA,CD all contain the same info but CD contains all needed
         
            splitted = line.split("\t")
                
            scaf_id = splitted[6]
            start = splitted[7]
            end = splitted[8]
            gene_name = splitted[13]
            #print scaf_id, start, end
            #print gene_name  

            
            if start == s_last and end == e_last:
                continue
            
            if gene_name == "":
                continue
            
            if scafDict.get(scaf_id, "missing") == "missing":
                scafDict[scaf_id] = [start,end]
                
            else:
                scafDict[scaf_id].append([start,end, gene_name])
                
            s_last = start
            e_last = end

    
    return scafDict   



def checkBlastHits(blast6, scafDict):
    for line in blast6:
        splitted = line.split("\t")
        
        scaf_id = splitted[1].split("|")[3]
        scaf_start = splitted[8]
        scaf_end = splitted[9]
        
        #print scaf_id, scaf_start, scaf_end
        
        if scafDict.get(scaf_id, "missing") != "missing":
            
            for gene in scafDict[scaf_id]:
                if int(scaf_start) >= int(gene[0]) and int(scaf_end) <= int(gene[1]):
                    print "FOUND gene "+gene[2]

if __name__ == "__main__":
    
    import argparse 
    
    
    parser = argparse.ArgumentParser(description="check if blast hits are hits against genes")
    parser.add_argument("genomeanno", help="genome in gb format", type=str)
    parser.add_argument("blast6", help="", type=str)
    #parser.add_argument("outDir", help="directory where fasta files will be created", type=str)
    args = parser.parse_args()
    
    genome = open(args.genomeanno)
    blastIn = open(args.blast6)
    geneList = getGenes(genome)
    
    #for scaf in geneList:
    #    print scaf
        
    #print len(geneList)
    
    checkBlastHits(blastIn, geneList)
    
    #for gene in geneList["KB524583.1"]:
    #    print gene[2]
