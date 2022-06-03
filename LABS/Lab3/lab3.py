# BioPython
# L3. Bioinfomatics file format - FASTA FASTQ


# fasta format example
from Bio.SeqIO.FastaIO import SimpleFastaParser

count = 0
total_len = 0

with open("ls_orchid.fasta") as in_handle:
    for title, seq in SimpleFastaParser(in_handle):
        count += 1
        total_len += len(seq)

print("%i records with total sequence length %i" %(count, total_len))



# fastq format example
from Bio.SeqIO.QualityIO import FastqGeneralIterator

count = 0
total_len = 0

with open("SRR020192.fastq") as in_handle:
    for title, seq, qual in FastqGeneralIterator(in_handle):
        count += 1
        total_len += len(seq)

print("%i records with total sequence length %i" %(count, total_len))
