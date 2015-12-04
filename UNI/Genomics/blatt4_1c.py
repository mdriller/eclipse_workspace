'''
Created on 25.11.2015

@author: maxdriller
'''

import argparse

#calculate edit distance
def calcEditDist(str1, str2):   
    r1len = len(str1)
    r2len = len(str2)
    
    eMatrix = [[0 for x in range(r1len+1)] for x in range(r2len+1)]
    
    for i in range(0,r1len+1):
        eMatrix[0][i] = i
    
    for j in range(0,r2len+1):
        eMatrix[j][0] = j
    
    #testprinting 
    '''
    for i in eMatrix:
        print i          
    print "\n"
    '''

    for j in range(1,r2len+1):
        for i in range(1,r1len+1):
            
            
            if str1[i-1] == str2[j-1]:
                eMatrix[j][i] = eMatrix[j-1][i-1]
                
            
            else:
                if i == 0:
                    ins = eMatrix[j][i]+1
                    dele = eMatrix[j][i-1]+1
                    subst = eMatrix[j][i-1]+1
                elif j == 0:
                    ins = eMatrix[j-1][i]+1
                    dele = eMatrix[j][i]+1
                    subst = eMatrix[j-1][i]+1   
                else:
                    ins = eMatrix[j-1][i]+1
                    dele = eMatrix[j][i-1]+1
                    subst = eMatrix[j-1][i-1]+1
                
                eMatrix[j][i] = min(ins, dele, subst)                 
    
    #testprinting 
    '''
    for i in eMatrix:
        print i          
    print "\n"
    '''   
    
    return eMatrix

#for parsing agruments via commandline
parser = argparse.ArgumentParser(description="Genomics Excercise 4 - Task 1c => Edit distance between 2 strings")
parser.add_argument("string1", help="",type=str)
parser.add_argument("string2", help="",type=str)
args = parser.parse_args()


print "Edit-distance between the 2 strings: %i" % calcEditDist(args.string1, args.string2)[len(args.string2)][len(args.string1)]