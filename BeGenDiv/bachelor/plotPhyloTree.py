'''
Created on 15.10.2015

@author: maxdriller
'''

    
if __name__ == '__main__':
    
    from Bio import Phylo
    
    import argparse

    parser = argparse.ArgumentParser(description="change the annotation of the numts of phylogenetic analysis")
    parser.add_argument("NewickIn", help="path and name of a tree in newick format", type=str)
    #parser.add_argument("out", help="path and name of outputfile", type=str)
    args = parser.parse_args()
    
    testtree = Phylo.read(args.NewickIn, 'newick')
    testtree.ladderize()
    Phylo.draw(testtree)
    
    
