# lab3_2

import os
os.chdir("your path")

from Bio.SeqIO.QualityIO import FastqGeneralIterator

count = 0
total_len = 0

with open("SRR020192.fastq") as in_handle:
    for title, seq, qual in FastqGeneralIterator(in_handle):
        count += 1
        total_len += len(seq)

print("%i records with total sequence length %i" %(count, total_len))



