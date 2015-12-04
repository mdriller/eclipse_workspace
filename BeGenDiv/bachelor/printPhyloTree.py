'''
Created on 19.11.2015

@author: maxdriller
'''



if __name__ == "__main__":
    
    import argparse
    from Bio import Phylo
    from Bio import AlignIO
    
    
    parser = argparse.ArgumentParser(description= "")
    parser.add_argument("newick_tree", help="",type=str)
    
    args = parser.parse_args()
    newicktree = Phylo.read(args.newick_tree, "newick")
    
    Phylo.draw(newicktree)
    
    newicktree.root_with_outgroup("Tamandua")
   
    Phylo.draw(newicktree)
    
    