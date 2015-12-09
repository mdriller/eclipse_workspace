'''
Created on 01.02.2015

@author: maxdriller
'''
test = open("/home/maxdriller/Schreibtisch/BeGenDiv/arbeit/miseq_run_analysis/MiSeq_Result_Analysis2.csv")

testout = open("/home/maxdriller/Schreibtisch/BeGenDiv/arbeit/miseq_run_analysis/MiSeq_Result_Analysis3.csv", "w")


for line in test:
    line = line.replace(",", ".")
    splitted = line.split("\t")
    #print len(splitted)
    for idx, i in enumerate(splitted):
        if idx != 7:
            
            if splitted[idx].endswith("\n"):
                testout.write(splitted[idx])
            else:
                testout.write(splitted[idx] + "\t")
        elif idx == 7:
            #print "7", splitted[idx]
            if len(splitted[idx]) > 1:
                testout.write(splitted[idx].split("/")[0] + "\t" + splitted[idx].split("/")[1] + "\t")
            else:
                testout.write(splitted[idx] + "\t")



        
        
            
            