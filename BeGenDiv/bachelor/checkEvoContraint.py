'''
Created on 01.07.2015

@author: maxdriller
'''
import argparse
import scipy.stats as mst
from Bio import SeqIO


#script to check and compare the evolutionary constraint between two seqs
# currently testing how to let the script know where the genes are by reading in a gb file
# reading in data works now need to check how to loop through the codons

#NEED to add a fkt which checks for insertions/deletions in similar positions because that would be a huge indication for duplication

# checks the GC and AT content for both seqs ==> no return value yet!!!
def checkGC_AT_content(seq1, seq2):
    
    print seq1.count("T")
            
    seq1 = seq1.upper()
    seq1g = seq1.count("G")
    seq1c = seq1.count("C")
    seq1gc = float(seq1g + seq1c)/len(seq1)
            
    seq1a = seq1.count("A")
    seq1t = seq1.count("T")
    seq1at = float(seq1a + seq1t)/len(seq1)
            
    seq2 = seq2.upper()
    seq2g = seq2.count("G")
    seq2c = seq2.count("C")
    seq2gc = float(seq2g + seq2c)/len(seq2)
            
    seq2a = seq2.count("A")
    seq2t = seq2.count("T")
    seq2at = float(seq2a + seq2t)/len(seq2)
        
    print "seq1 GC: " + str(seq1gc) + " | AT: " + str(seq1at)
    print "seq2 GC: " + str(seq2gc) + " | AT: " + str(seq2at)



# gets the annotation and reading frame of prot-coding mtDNA ==> not used right now because seqs will be already cut before given...
# so currently useless       
def getReadingFrame(gbstream, genecoords):
    
    for line in gbstream:
        '''
        if line.startswith("     tRNA") or line.startswith("     rRNA"):
            splitted = line.strip().split(" ")
            
            if not splitted[12].startswith("complement"):
                coords = []
                coords.append(int(splitted[12].split("..")[0])-1)
                coords.append(int(splitted[12].split("..")[1])-1)
                genecoords.append(coords)
            else:
                test = splitted[12].strip(")")
                test = test.split("(")[1]
                test = test.split("..")
                
                coords = []
                coords.append(int(test[0])-1)
                coords.append(int(test[1])-1)
                genecoords.append(coords)         
        '''       
        if line.startswith("     CDS"):
            splitted = line.strip().split(" ")
    
            if not splitted[13].startswith("complement"):
                coords = []
                coords.append(int(splitted[13].split("..")[0])-1)
                coords.append(int(splitted[13].split("..")[1])-1)
                genecoords.append(coords)            
            else:
                test = splitted[13].strip(")")
                test = test.split("(")[1]
                test = test.split("..")
                
                coords = []
                coords.append(int(test[0])-1)
                coords.append(int(test[1])-1)
                genecoords.append(coords)     
            
    print genecoords

# compares the 2 seqs base per base and counts the synonymus and non-syn. mutations and the SNPs per codon position 
# in the end chi-squared-test for codon pos.
def checkMutations(seq1, seq2):
    
    nr_nonsynM = 0
    nr_synM = 0
    
    protseq1 = seq1.seq.translate()
    protseq2 = seq2.seq.translate()
    
    codChecked = False
    
    mismatches = [0]*3
    codonpos = 0
    for idx, char1 in enumerate(seq1.seq):
    
        char2 = seq2.seq[idx]
        #print char1, char2
        if char1 != char2:
            #print "mismatch"
            mismatches[codonpos] += 1
            
            if codChecked == False:
                if protseq1[idx/3] == protseq2[idx/3]:
                    nr_synM +=1
                else:
                    nr_nonsynM += 1
                
                codChecked = True
        
        if codonpos == 2:
            codonpos = 0
            codChecked = False
        else:
            codonpos += 1
    
    print "total nr of as-mismatches per codon: " + str(mismatches)
    print "#synonymus mutations: " + str(nr_synM)
    print "#nonsynonymus mutations: " + str(nr_nonsynM)
    
    #totalmut = sum(mismatches)
    #seqlen = len(seq1)
    #print totalmut
    #expected = [0]*3
    
    #for idx, pos in enumerate(mismatches):
    #    expected[idx] = (seqlen/3)/seqlen * totalmut/seqlen * seqlen
    
    print mst.chisquare(mismatches)
 
 
 
parser = argparse.ArgumentParser(description="Compare two NUMTs --> variety of fkts")
parser.add_argument("--atgc", "-atgc", help="check the AT/GC content of the seqs", action="store_true")
parser.add_argument("--cm", "-checkmut", help="check the mutations (for codon pos) in the seqs to check the selektive contraint --> x^2-test", action="store_true")

args = parser.parse_args()
 
 
    
'''useless/old stuff
#gbstream = open("/home/maxdriller/Schreibtisch/C.didactylus_sequence.gb")
#genecoords = []
#getReadingFrame(gbstream, genecoords)
#print len(genecoords)
'''

numt1 = SeqIO.read(open("/home/maxdriller/Schreibtisch/Praktikum/Bachelor/Choloepus_hoffmanni/analysis/CH/test(numt_comparison)/(0-10075)_mapped_cns.fasta"), "fasta")
numt2 = SeqIO.read(open("/home/maxdriller/Schreibtisch/Praktikum/Bachelor/Choloepus_hoffmanni/analysis/CH/test(numt_comparison)/0-7934.fasta"), "fasta")
numt1.seq = numt1.seq.upper()
numt2.seq = numt2.seq.upper()


if args.atgc:
    checkGC_AT_content(numt1, numt2)
if args.cm:
    checkMutations(numt1, numt2)

