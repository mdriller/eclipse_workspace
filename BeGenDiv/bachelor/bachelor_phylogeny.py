'''
Created on 13.11.2015

@author: maxdriller
'''

#from Bio import Phylo

#msa = AlignIO.read('Tests/TreeConstruction/msa.phy', 'phylip')
#msas = bootstrap(msa, 100)

if __name__ == "__main__":
    
    import Bio
    from Bio.Phylo import PhyloXML, NewickIO
    import argparse
    from Bio import Phylo
    from Bio import AlignIO
    from Bio.Phylo.Consensus import *
    from Bio.Phylo.TreeConstruction import DistanceCalculator
    from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
    
    parser = argparse.ArgumentParser(description= "")
    parser.add_argument("multSeqAln", help="",type=str)
    #parser.add_argument("out",help="")
    
    args = parser.parse_args()
    
    msa = AlignIO.read(args.multSeqAln, "fasta")
    
    #tree = Phylo.read(args.multSeqAln, "newick")
    #msas = bootstrap(msa, 100)
   
    calculator = DistanceCalculator('blosum62')
    constructor = DistanceTreeConstructor(calculator)
    #trees = bootstrap_trees(msa, 100, constructor)
    print "start bootstrap"
    consensus_tree = bootstrap_consensus(msa, 2, constructor, majority_consensus)
    print "bootstrap done"
    print consensus_tree
    consensus_tree.root_with_outgroup("Tamandua") 
    Phylo.draw(consensus_tree)
    
    