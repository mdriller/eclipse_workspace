'''
Created on 15.10.2015

@author: maxdriller
'''
from Bio import SeqIO
if __name__ == '__main__':
    
    import argparse

    parser = argparse.ArgumentParser(description="change the annotation of the numts of phylogenetic analysis")
    parser.add_argument("fastaIn", help="path and name of fastafile", type=str)
    parser.add_argument("fastaOut", help="path and name of outputfile", type=str)
    parser.add_argument("start", help="wanted len for outputfile", type=int)
    parser.add_argument("end", help="wanted len for outputfile", type=int)
    args = parser.parse_args()
    
    fastastream = SeqIO.read(args.fastaIn, "fasta")
    newseq = fastastream
    
    newseq.seq = fastastream.seq[args.start:args.end]

    SeqIO.write(newseq, args.fastaOut, "fasta")