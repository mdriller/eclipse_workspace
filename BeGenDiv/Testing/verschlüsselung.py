'''
Created on 02.10.2015

@author: maxdriller
'''

import argparse


def encode(instream, writer):
    

    linecount = 1
    for line in instream:
        newline = ""   
        line = line.strip("\n") 
        poscount = 1
        for char in line:
            #print "old:" + str(ord(char)) + " " + str(len(str(ord(char))))
            #print "new: " + str(ord(char) + linecount*poscount)
            
            newchar = str(ord(char) + linecount*poscount)
            
            if len(newchar) == 1:
                newchar = "00" + newchar
            elif len(newchar) == 2:
                newchar = "0" + newchar
            
            
            #print "VERYnew: " + newchar  
            newline += newchar
            #print newline
            poscount += 1
        
        linecount += 1
        print linecount
        writer.write(newline + "\n")
    
        
def decode(instream, writer):

    linecount = 1
    for line in instream:
        newline = ""
        line = line.strip("\n")
        poscount = 1
        triplechar= ""
        for char in line:
            triplechar += char
            if len(triplechar) == 3:

                #print "old:" + str(triplechar)
                #print "new: " + str(int(triplechar) - linecount*poscount)
                newchar = chr(int(triplechar) - linecount*poscount)
                newline += newchar
            
                triplechar = ""
                poscount += 1

            
        
        linecount += 1
        #print linecount
        writer.write(newline + "\n")
            


parser = argparse.ArgumentParser(description="")
parser.add_argument("infile", help="path and name of text file that should be ", type=str)
parser.add_argument("outfile", help="path and name of outputfile for numts will be created", type=str)
parser.add_argument("--d", "-decode", help="decoding", action="store_true")
args = parser.parse_args()



if __name__ == '__main__':
    infile = open(args.infile)
    writer = open(args.outfile, "w")
    
    if args.d:
        decode(infile, writer)
    else:
        encode(infile, writer)  
        
    infile.close()
    writer.close()
            