# Lab5_2

#1#########################################################################
from Bio.Seq import Seq

my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")

print(my_seq[4:12])
print(my_seq[0::3])
print(my_seq[1::3])
print(my_seq[2::3])
print(my_seq[::-1])

print("")

#2#########################################################################
from Bio.Seq import Seq

protein_seq = Seq("EVRNAK")
dna_seq = Seq("ACGT")

print(protein_seq + dna_seq)

print("")

#3#########################################################################
from Bio.Seq import Seq

list_of_seqs = [Seq("ACGT"), Seq("AACC"), Seq("GGTT")]
concatenated = Seq("")

for s in list_of_seqs:
    concatenated += s

print(concatenated)

print("")

#4#########################################################################

from Bio.Seq import Seq

contigs = [Seq("ATG"), Seq("ATCCCG"), Seq("TTGCA")]
spacer = Seq("N" * 10)

print(spacer.join(contigs))

