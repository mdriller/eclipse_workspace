'''
Created on 06.11.2015

@author: maxdriller
'''

import argparse

parser = argparse.ArgumentParser(description= "erstellt ein subset von paired-end reads")
parser.add_argument("inFile", help="",type=float)
parser.add_argument("out",help="")

args = parser.parse_args()

fastq = open(args.inFile)

