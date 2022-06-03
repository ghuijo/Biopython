# Lab5_3

#1#########################################################################
from Bio.Seq import Seq

dna_seq = Seq("acgtACGT")

print(dna_seq)

print(dna_seq.upper())

print(dna_seq.lower())

print("GTAC" in dna_seq)

print("GTAT" in dna_seq.upper())

print("")

#2#########################################################################
dna_seq = "acgtACGT"    # 그냥 문자열

print(dna_seq)

print(dna_seq.upper())

print(dna_seq.lower())

print("GTAC" in dna_seq)

print("GTAT" in dna_seq.upper())

