'''
Created on 01.12.2015

@author: maxdriller
'''
    
import argparse

    
parser = argparse.ArgumentParser(description="")
parser.add_argument("sam", help="", type=str)
args = parser.parse_args()

samIn = open(args.sam)

counter = 0
softcount = 0
nomate = 0

for line in samIn:
    if not line.startswith("@"):
        splitted = line.split("\t")
        if splitted[5] != "*":
            if "S" in splitted[5]:
                softcount += 1
                print splitted[5], splitted[1]
                
                #flag_bin = bin(splitted[1])
                
            counter += 1
            
print "%i reads in total" % counter
print "%i soft clipped reads" % softcount