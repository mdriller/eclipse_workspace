'''
Created on 21.10.2015

@author: maxdriller
'''
from decimal import *

def prob_of_read_being_accurate(quality, rlength): 
    
    p = 0
    for base in quality:
        #p = float(-(ord(base)-33))/10
        p += 10**(float(-(ord(base)-33))/10)
        #print p
        
    return p/rlength

def cigarize(ref, read):
    
    pos = 0
    cigar = ""
    
    match = 0
    ins = 0
    deli = 0
    
    for i, base1 in enumerate(ref):
        base2 = read[i]
        
        #print base1, base2
    
        if pos == 0:
            if base2 != " ":
                pos = i + 1
        
        if base1 == " ":
            
            #print "ins"
            ins += 1
            
            if match > 0:              
                cigar += "%iM" % match
                match = 0
            
            elif deli > 0:
                cigar += "%iD" % deli
                deli = 0
            
        
        if base2 == " ":          
                   
            if pos > 0:
                #print "deli"
                deli += 1
            
            if match > 0:               
                cigar += "%iM" % match
                match = 0
            
            elif ins > 0:                
                cigar += "%iI" % ins
                
        if base1 != " " and base2 != " ":
            
            #print "match"
            
            match += 1
            
            if deli > 0:               
                cigar += "%iD" % deli
                deli = 0
            
            elif ins > 0:                
                cigar += "%iI" % ins
                ins = 0
        
        #print match, ins, deli
    
    if match > 0:
        cigar += "M%i" % match
          
    
    
    return pos, cigar  


if __name__ == '__main__':
    
    rquali = "GEDEEEECCBB;9"
    
    print prob_of_read_being_accurate(rquali, 13)
    
    ref= "CCATCCT GAACTGACTAAC"
    read="   TCCTAGAA TGGCT   "
    
    pos, cig = cigarize(ref, read)
    print "pos: %i"%pos  + " cigar: %s"%cig
    