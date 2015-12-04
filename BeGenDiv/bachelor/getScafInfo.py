'''
Created on 19.08.2015

@author: maxdriller
'''

import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser(description="get info on Scaffs in fasta-file(length, N-content, ...)")
parser.add_argument("ScafFasta", help="path and name of file containing the scaffolds with numts in fasta format", type=str)
parser.add_argument("output", help="path and name of outputfile for info on Scafs", type=str)

args = parser.parse_args()


scafIn = SeqIO.parse(args.ScafFasta, "fasta")
outstream = open(args.output, "w")


outstream.write("Scafname+ID \t scafLen \t #Ns \n")

for scaf in scafIn:
    
    s_id = scaf.id
    s_name = scaf.description.split(" ")[8].strip(",")
    s_len = len(scaf.seq)
    s_Ns = scaf.seq.count("N")
    
    outstream.write(s_name + " " + s_id + "\t" + str(s_len) + "\t" + str(s_Ns) + "\n")
    
        