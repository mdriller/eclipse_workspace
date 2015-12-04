'''
Created on 18.03.2015

@author: maxdriller
'''

import argparse
import gzip


def getReadIDs(instream, idlist, mini, maxi, outstream):
    for line in instream:
        if line.startswith("@") == False:
            splitted = line.split("\t")

            if int(splitted[3]) < maxi and int(splitted[3]) > mini:
                    if splitted[0] not in idlist:
                        #idlist.append(splitted[0])
                        #print splitted[0] + "\t" + splitted[7] + "\t" + splitted[4]
                        outstream.write(splitted[0]+"\n")
                    else:
                        continue
        

parser = argparse.ArgumentParser(description="get read-IDs that mapped against a specific range out of the bam/sam file")
parser.add_argument("input", help="sam/bam input file")
parser.add_argument("mini", help="lower limit of the range", type=int)
parser.add_argument("maxi", help="upper limit of the range", type=int)
parser.add_argument("output", help="path and name of output file")
args = parser.parse_args()

idlist = []

try: 
    mapstream = open(args.input)
    outstream= open(args.output, "w")
except:
    print "Error - unable to open file"
    
getReadIDs(mapstream, idlist, args.mini, args.maxi, outstream)

mapstream.close()
outstream.close()
