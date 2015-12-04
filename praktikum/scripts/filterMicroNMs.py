'''
Created on 30.03.2015

@author: maxdriller
'''


stream = open("/home/maxdriller/Schreibtisch/maped_probes.txt")
outstream = open("/home/maxdriller/Schreibtisch/maped_probes_NMfiltered.txt", "w")

for line in stream:
    print line
    if not line.startswith("#"):
        splitted = line.split("\t")
        print splitted[1]
        if splitted[1][1:3] == "NM":
            #print "found NM"
            #print splitted[1][1:2]
            outstream.write(line)