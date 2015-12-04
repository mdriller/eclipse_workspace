'''
Created on 27.03.2015

@author: maxdriller
'''

from Bio import Entrez 
from Bio import SeqIO

Entrez.email = "mdriller@zedat.fu-berlin.de"
query = "Balamuthia[Orgn]"
handle = Entrez.esearch(db="nucleotide", term=query)

#for line in handle:
#    print line
    
record = Entrez.read(handle)
hit_count = record["Count"]
hit_ids = record["IdList"]
print hit_count
print hit_ids

id_str = ",".join(hit_ids)
handle2 = Entrez.efetch(db="nucleotide", id=id_str, rettype="gb")

records = SeqIO.parse(handle2, "gb")
for rec in records:
    print("downloaded record " + rec.id)
