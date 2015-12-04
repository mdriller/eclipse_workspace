'''
Created on 01.02.2015

@author: maxdriller
'''
#import psutil
#from memory_profiler import profile
#import gzip
#from Bio import SeqIO


#print(psutil.cpu_times())
#print(psutil.cpu_count())

#@profile
#def doStuff():
#    testfile = gzip.open("/home/maxdriller/Schreibtisch/Praktikum/Bachelor/miseq_sloths/raw/BTR/BTR-139_S1_L001_R1_001.fastq.gz", "r")

    
#    for line in testfile:
        
#        if len(line) > 600:
#            print "ups"
            

#if __name__ == '__main__':
#    doStuff()

#import subprocess
#subprocess.call(['cd', '/home/maxdriller/Schreibtisch/Praktikum/Bachelor/Choloepus_hoffmanni/analysis/1_numt_blasting/NUMTS_mt_index_mt_like_deleted_NEW_anno/NUMTS'], shell=True)
#test = subprocess.call("ls")
'''
fastareader = SeqIO.parse("/home/maxdriller/Schreibtisch/Praktikum/Bachelor/Choloepus_hoffmanni/analysis/1_numt_blasting/CH_Scafs_withNUMTS.fasta", "fasta")

for scaf in fastareader:
    if scaf.id == "gi|692246508|gb|KN191980.1|":
        print scaf.id
        
        subseq = scaf.seq[387801:395801]
        print subseq
        
'''
#fasta = SeqIO.read("/home/maxdriller/Schreibtisch/Praktikum/Bachelor/Choloepus_hoffmanni/analysis/2_Scaffolds_with_muliple_numts/merged_NUMTS/Scaffold259005_387801-393304.fasta", "fasta")

#SeqIO.write(fasta, "/home/maxdriller/Schreibtisch/Praktikum/Bachelor/Choloepus_hoffmanni/analysis/2_Scaffolds_with_muliple_numts/merged_NUMTS/Scaffold259005_387801-393304.fasta", "fasta")
'''
fasta = SeqIO.read("/home/maxdriller/Schreibtisch/Praktikum/Bachelor/assembled_mt_genomes/CH/CH_mt_no_overlap.fasta", "fasta")

print len(fasta.seq)

fasta.seq = fasta.seq[0:10075]

print len(fasta.seq)

SeqIO.write(fasta, "/home/maxdriller/Schreibtisch/CH_mt_subseq_0-10075.fasta", "fasta")
'''

#fasta = SeqIO.read("/home/maxdriller/Schreibtisch/Praktikum/Bachelor/NUMT_analysis/0_4_all_numts_after_merging/long_numts_500bp+/Scaffold254774_merged_numt.fasta", "fasta")
#print len(fasta.seq)


#import zipfile

#archive = zipfile.ZipFile('/home/maxdriller/spree/users/BeGenDivServer_backup/Geneious Backup 2014-10-29.backup.zip', 'r')
'''
from Bio import Phylo
from Bio import SeqIO

testtree = Phylo.read('/home/maxdriller/Schreibtisch/Praktikum/Bachelor/NUMT_analysis/0_4_all_numts_after_merging/phylo_analysis/first_analysis_start/multAlign/phylip_dnaml_results/outtree', 'newick')
testtree.ladderize()
Phylo.draw(testtree)

testseq = SeqIO.read("/home/maxdriller/Schreibtisch/Praktikum/Bachelor/NUMT_analysis/0_4_all_numts_after_merging/long_numts_500bp+_newAnno/numt7_9387-1553_reverse.fasta", "fasta")
print testseq.seq
newseq = testseq
newseq.seq = testseq.seq.reverse_complement()
print newseq.seq

SeqIO.write(newseq ,"/home/maxdriller/Schreibtisch/Praktikum/Bachelor/NUMT_analysis/0_4_all_numts_after_merging/long_numts_500bp+_newAnno/numt7_9387-1553.fasta", "fasta")
'''


#from Bio import SeqIO

#testscafs = SeqIO.parse("/home/maxdriller/Schreibtisch/Praktikum/Bachelor/NUMT_analysis/0_4_all_numts_after_merging/phylo_analysis/first_analysis_start/reverse_complements/numt2_5_7_15_32+mts_reverse_compls.fasta", "fasta")
#SeqIO.write(testscafs ,"/home/maxdriller/Schreibtisch/Praktikum/Bachelor/NUMT_analysis/0_4_all_numts_after_merging/phylo_analysis/first_analysis_start/reverse_complements/numt2_5_7_15_32+mts_reverse_compls_2.fasta", "fasta")



'''
testscafs = SeqIO.parse("/home/maxdriller/Schreibtisch/Praktikum/Bachelor/soap_BTR_scaf_assembly/scafs/graph_prefix.scafSeq", "fasta")

big_scafs = []
count = 0
for scaf in testscafs:
    if len(scaf.seq) >= 10000:
        print scaf.id, len(scaf.seq)
        big_scafs[count] = scaf
        count += 1 
    
    SeqIO.write(big_scafs, "/home/maxdriller/Schreibtisch/Praktikum/Bachelor/soap_BTR_scaf_assembly/scafs/graph_prefix_10000bp+.scafSeq", "fasta")
'''       
'''        
from Bio import AlignIO

test = AlignIO.read("/home/maxdriller/Schreibtisch/Praktikum/Bachelor/NUMT_analysis/0_4_all_numts_after_merging/phylo_analysis/PHYLO/2_/multAln_numt14_22_mts.fasta.phy", "phylip", 7)

#AlignIO.write(test, "/home/maxdriller/Schreibtisch/Praktikum/Bachelor/NUMT_analysis/0_4_all_numts_after_merging/phylo_analysis/only_mts_phylo/multAln_all_mts.fasta.phylip", "phylip")
print "alignment length %i" % test.get_alignment_length()

print (test)
'''


'''
countReads = open("/home/maxdriller/Schreibtisch/BeGenDiv/arbeit/demulti/marina_reads/caddle_countReads.236894.out")
outfile = open("/home/maxdriller/Schreibtisch/BeGenDiv/arbeit/demulti/marina_reads/caddle_run_readCount.tsv", "w")
linecount = -2
for line in countReads:
    #print line
    
    if line.strip("\n") != "":

        #print linecount
        if line.startswith("/home/") or line.startswith("gzip"):
            linecount = 2
            rName = line.split("/")[-1].strip("\n")
            #print rName
            outfile.write(rName + "\t")
        elif linecount == 2:
            print line
            linecount = 0
            if line.strip("\n") != "0":
                readCount = int(line.strip("\n"))/4
                outfile.write(str(readCount) + "\n")
            else:
                print "zero reads"
                outfile.write(line)




'''
'''
infile = open("/home/maxdriller/Schreibtisch/BeGenDiv/arbeit/demulti/marina_reads/bats_run_readCount.tsv")
outfile = open("/home/maxdriller/Schreibtisch/BeGenDiv/arbeit/demulti/marina_reads/bats_run_readCountFINAL.tsv", "w")


r1 = 0
r2 = 0
name = ""
for line in infile:
    if line.strip("\n")  != "":
        #print line
        
        if line.split("\t")[0].strip("\n").endswith("fastq.gz"):      
            
            #print "hi"
            splitted = line.split("_")
            
            red = splitted[-2]
            print red

                
            if splitted[0] != name:   
      
                print name


                outfile.write(name +"_R1 total:\t" + str(r1) +  "\n")
                outfile.write(name +"_R2 total:\t" + str(r2) +  "\n\n\n")
                r1 = 0
                r2 = 0
                
                name = splitted[0]
            #print splitted
            
            if red == "R1":
                r1 += int(line.split("\t")[1])
            elif red == "R2":
                r2 += int(line.split("\t")[1])
                
            print r1, r2

            if red.startswith("R"):
                outfile.write(line)
    else:
        outfile.write(line)

if r1 != 0:
    outfile.write(name +"_R1 total:\t" + str(r1) +  "\n")
    outfile.write(name +"_R2 total:\t" + str(r2) +  "\n\n\n")
    r1 = 0
    r2 = 0        
'''
'''
from Bio import SeqIO

rRNAseqs = SeqIO.parse("/home/maxdriller/Schreibtisch/own_ncbi_rRNA_comp.fasta", "fasta")

for seq in rRNAseqs:
    
    print seq.id
    #if seq.id.startswith("C.D"):
    print len(seq.seq)
    print seq.seq.translate()

'''

test = open("/home/maxdriller/Schreibtisch/BeGenDiv/arbeit/miseq_run_analysis/MiSeq_Result_Analysis.csv")

testout = open("/home/maxdriller/Schreibtisch/BeGenDiv/arbeit/miseq_run_analysis/MiSeq_Result_Analysis2.tsv", "w")

for line in test:
    line = line.replace(",", ".")
    splitted = line.split("\t")
    print len(splitted)
    for idx, i in enumerate(splitted):
        if idx != 7 and idx != 12:
            testout.write(splitted[idx] + "\t")
        elif idx == 7:
            #print "7", splitted[idx]
            if len(splitted[idx]) > 1:
                testout.write(splitted[idx].split("/")[0] + "\t" + splitted[idx].split("/")[1] + "\t")
            else:
                testout.write(splitted[idx] + "\t")
        elif idx == 12:
            testout.write(splitted[idx])
        
        
            
            