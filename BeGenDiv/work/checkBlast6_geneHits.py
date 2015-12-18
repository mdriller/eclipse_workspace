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
                      
            if scafDict.get(scaf_id, "missing") == "missing":
                scafDict[scaf_id] = [start,end]
                
            else:
                scafDict[scaf_id].append([start,end, gene_name, id])
                
            s_last = start
            e_last = end
    
    return scafDict   



def checkBlastHits(blast6, scafDict, outwriter):
    for line in blast6:
        splitted = line.split("\t")
        
        scaf_id = splitted[1].split("|")[3]
        scaf_start = splitted[8]
        scaf_end = splitted[9]
        
        #print scaf_id, scaf_start, scaf_end
        
        if scafDict.get(scaf_id, "missing") != "missing":
            #print scafDict[scaf_id]
            
            for gene in scafDict[scaf_id]:
                #print gene[0]
                if int(scaf_start) >= int(gene[0]) and int(scaf_end) <= int(gene[1]):
                    
                    #print "FOUND gene "+gene[2]              
                    outwriter.write(splitted[0] + "\t" + scaf_id + "\t" + scaf_start + "\t" + scaf_end +  "\t" + gene[2] + "\t" + gene[3] + "\t" + "[" + gene[0] + "-" + gene[1] + "]" + "\n")

if __name__ == "__main__":
    
    import argparse 
    
    parser = argparse.ArgumentParser(description="check if blast hits are hits against genes")
    parser.add_argument("genomeanno", help="genome in gb format", type=str)
    parser.add_argument("blast6", help="", type=str)
    parser.add_argument("outFile", help="directory where fasta files will be created", type=str)
    args = parser.parse_args()
    
    genome = open(args.genomeanno)
    blastIn = open(args.blast6)
    geneList = getGenes(genome)
    outWriter = open(args.outFile, "w")
    
    checkBlastHits(blastIn, geneList, outWriter)

