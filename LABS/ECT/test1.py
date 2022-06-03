'''
#from Bio.SeqIO.FastaIO import *

from Bio.SeqIO import *
with open("ls_orchid.fasta") as in_handle:
    for title, seq in SimpleFastaParser(in_handle):
        print(title)
        print("")
'''

