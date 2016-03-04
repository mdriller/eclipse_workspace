'''
Created on Mar 2, 2016

@author: maxdriller
'''

import argparse



def writeStuff(writer, ms, name):
    
    #writer.write(name + "_" + str(i))
    for m in ms:
        if type(m) == list:
            for n in m:
                writer.write("\t")
                writer.write(n)
        
        else:   
            writer.write("\t")
            writer.write(m)
            writer.write("\n")
            

def buildPredictionDICT(mDict, misa):
    
    #first line is a head but doesn't start with # so solved it this way
    firstline = misa.readline()
    
    
    name1=""
    name2=""
    
    for line in misa:
        name = line.split("\t")[0].split("_")[0]
        ids = line.split("\t")[0].split("_")[-1]
        microsat = line.strip().split("\t")[1:]
        #print id
        #will be filled out in the first step of the loop
        if name1 == "":
            name1 = name
        
        elif name2 == "":
            name2 = name
        
        
        if mDict.get(name, "missing") == "missing":
            mDict[name] = {}
        
        if mDict[name].get(id, "missing") == "missing":
            mDict[name][ids] = microsat
        else:
            mDict[name][ids].append(microsat)
            
            #print mDict[name][id]

        #last id is the number of sequence comparisons (size of Dicts)
    #print "name1 " + name1
    #print "name2 " + name2
    
    
    return ids, name1, name2
        
        #if mDict.get(id, "missing") == "missing":
            #mDict[id] = 
        
#compares the microsatellite prediction entries in both dictionaries and outputs the completely identical ones    
def compareDictsIdenitcal(mDicts, mInfo, outWriter, outWriter2, shiftedOut):
    
    dLength = int(mInfo[0])
    name1 = mInfo[1]
    name2 = mInfo[2]
    
    for i in range(1, dLength):
        
        #if i == 1:
            #print mDicts[name1].get(str(i), "missing")
            
        
        if mDicts[name1].get(str(i), "missing") != "missing" and mDicts[name2].get(str(i), "missing") != "missing":
            
            ms1 = mDicts[name1][str(i)]
            ms2 = mDicts[name2][str(i)]
            
            #case MS are 100% identical   
            if ms1 == ms2:
                outWriter.write(name1 + "_" + str(i))
                for m1 in ms1:
                    if type(m1) == list:
                        for n1 in m1:
                            outWriter.write("\t")
                            outWriter.write(n1)
        
                    else:   
                        outWriter.write("\t")
                        outWriter.write(m1)
                outWriter.write("\n")
                    
                outWriter.write(name2 + "_" + str(i))
                for m2 in ms2:
                    if type(m2) == list:
                        for n2 in m2:
                            outWriter.write("\t")
                            outWriter.write(n2)
                            
                    else:
                        outWriter.write("\t")
                        outWriter.write(m2)
                outWriter.write("\n")
                    
                outWriter.write("########################################################################################" + "\n")
                    
                mDicts[name1].pop(str(i))
                mDicts[name2].pop(str(i))

            #MS not 100% identical
            else:
                #print ms1[2], ms2
                # look into how to do it for more than 2 MS per seq
                if len(ms1[2].split(")")) > 2:
                    print ""
                    #print ms1[2].split(")")[0][1:]
                    #print ms1[2].split(")")[1].split("(")[1]
                    #print ms1[2].split(")")[2][1:]
                    #print ms1[2]
                    
                else:
                    ms_n1 = ms1[2].split(")")[0][1:]
                    ms_n2 = ms2[2].split(")")[0][1:]
                    
                    
                    # different MS other seq repeeted
                    if ms_n1 != ms_n2:
                        print ms1, ms2
                        print "different MS!!!"
                        
                        outWriter2.write(name1 + "_" + strMDc3Yjk2Z!(i))
                        for m1 in ms1:
                            if type(m1) == list:
                                for n1 in m1:
                                    outWriter2.write("\t")
                                    outWriter2.write(n1)
                    
                            else:   
                                outWriter2.write("\t")
                                outWriter2.write(m1)
                        outWriter2.write("\n")
                        mDicts[name1].pop(str(i))
                        #outWriter2.write("########################################################################################" + "\n")
                        
                        outWriter2.write(name2 + "_" + str(i))
                        for m2 in ms2:
                            if type(m2) == list:
                                for n2 in m2:
                                    outWriter2.write("\t")
                                    outWriter2.write(n2)
                    
                            else:   
                                outWriter2.write("\t")
                                outWriter2.write(m2)
                        outWriter2.write("\n")
                        mDicts[name2].pop(str(i))
                        outWriter2.write("########################################################################################" + "\n")
                    
                    #same MS (ms_n1 == ms_n2)
                    else:
                        print ms1, ms2
                        
                        start1 = int(ms1[4])
                        start2 = int(ms2[4])
                        end1 = int(ms1[5])
                        end2 = int(ms2[5])
                        
                        #print start1, start2
                        #print end1, end2
                        
                        #threshold of 4
                        if (start1 > start2-5) and (start1 < start2+5) and (end1 > end2-5) and (end1 < end2+5):
                            print "shifted MS"
                             
                            shiftedOut.write(name1 + "_" + str(i))
                            for m1 in ms1:
                                if type(m1) == list:
                                    for n1 in m1:
                                        shiftedOut.write("\t")
                                        shiftedOut.write(n1)
                    
                                else:   
                                    shiftedOut.write("\t")
                                    shiftedOut.write(m1)
                            shiftedOut.write("\n")
                            mDicts[name1].pop(str(i))
                            
                            shiftedOut.write(name1 + "_" + str(i))
                            for m2 in ms2:
                                if type(m2) == list:
                                    for n2 in m2:
                                        shiftedOut.write("\t")
                                        shiftedOut.write(n2)
                    
                                else:   
                                    shiftedOut.write("\t")
                                    shiftedOut.write(m2)
                            shiftedOut.write("\n")
                            mDicts[name2].pop(str(i))
                            
                            shiftedOut.write("########################################################################################" + "\n")

def checkDifferences(mDicts, mInfo, outWriter3):
    
      
    dLength = int(mInfo[0])
    name1 = mInfo[1]
    name2 = mInfo[2]
    
    for i in range(1, dLength):
        
        #if i == 1:
            #print mDicts[name1].get(str(i), "missing")
            #print mDicts[name2].get(str(i), "missing")
            
        
        if mDicts[name1].get(str(i), "missing") != "missing" and mDicts[name2].get(str(i), "missing") == "missing":
            #if MS is in one species/sample but not the other one (no MS on the same locus)
                
            ms1 = mDicts[name1][str(i)]
                
            outWriter3.write(name1 + "_" + str(i))
            for m1 in ms1:
                if type(m1) == list:
                    for n1 in m1:
                        outWriter3.write("\t")
                        outWriter3.write(n1)
        
                else:   
                    outWriter3.write("\t")
                    outWriter3.write(m1)
            outWriter3.write("\n")
            mDicts[name1].pop(str(i))
            outWriter3.write("########################################################################################" + "\n")
               

            
            
        elif mDicts[name2].get(str(i), "missing") != "missing" and mDicts[name1].get(str(i), "missing") == "missing":
            #if MS is in one species/sample but not the other one (no MS on the same locus)
             
            ms2 = mDicts[name2][str(i)]
                        
            outWriter3.write(name2 + "_" + str(i))
            for m2 in ms2:
                if type(m2) == list:
                    for n2 in m2:
                        outWriter3.write("\t")
                        outWriter3.write(n2)
                
                else:   
                    outWriter3.write("\t")
                    outWriter3.write(m2)
            outWriter3.write("\n")
            mDicts[name2].pop(str(i))
            outWriter3.write("########################################################################################" + "\n")
            
        #if mDicts[name1].get(str(i), "missing") != "missing" and mDicts[name2].get(str(i), "missing") != "missing":
            
    



parser = argparse.ArgumentParser(description="")
parser.add_argument("misaIn", help="", type=str)
parser.add_argument("identicalOut", help="", type=str)
parser.add_argument("completeDiffs", help="", type=str)
parser.add_argument("closeDiffs", help="", type=str)
parser.add_argument("shifted", help="", type=str)

args = parser.parse_args()

misaFile = open(args.misaIn)

dict1 = {}

msInfo = buildPredictionDICT(dict1, misaFile)
#print msInfo

compareDictsIdenitcal(dict1, msInfo, open(args.identicalOut, "w"), open(args.closeDiffs, "w"), open(args.shifted, "w"))

checkDifferences(dict1, msInfo, open(args.completeDiffs, "w"))

#print len(dict1["1524"])
#print len(dict1["1562"])


