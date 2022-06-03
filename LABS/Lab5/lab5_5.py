# Lab5_5

#1#########################################################################
from Bio.Seq import Seq

coding_dna = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print(coding_dna)

template_dna = coding_dna.reverse_complement()
print(template_dna)
print(template_dna.reverse_complement().transcribe())

messenger_rna = coding_dna.transcribe()
print(messenger_rna)

print("")


#2#########################################################################
from Bio.Seq import Seq

messenger_rna = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG")
print(messenger_rna)

print(messenger_rna.back_transcribe())

print("")


#3#########################################################################
from Bio.Seq import Seq

messenger_rna = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG")
print(messenger_rna)

print(messenger_rna.translate())

print("")


#4#########################################################################
from Bio.Seq import Seq

coding_dna = Seq("ATCCVVATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
print(coding_dna)

print(coding_dna.translate())
print(coding_dna.translate(table = "Vertebrate Mitochondrial"))
print(coding_dna.translate(table = 2))
print(coding_dna.translate(to_stop = True))
print(coding_dna.translate(table = 2, to_stop = True))

print("")


#5#########################################################################
from Bio.Seq import Seq

gene = Seq("GTGAAAAAGATGCAATCTATCGTACTCGCACTTTCCCTGGTTCTGGTCGCTCCCATGGCA"
           "GCACAGGCTGCGGAAATTACGTTAGTCCCGTCAGTAAAATTACAGATAGGCGATCGTGAT"
           "AATCGTGGCTATTACTGGGATGGAGGTCACTGGCGCGACCACGGCTGGTGGAAACAACAT"
           "TATGAATGGCGAGGCAATCGCTGGCACCTACACGGACCGCCGCCACCGCCGCGCCACCAT"
           "AAGAAAGCTCCTCATGATCATCACGGCGGTCATGGTCCAGGCAAACATCACCGCTAA")

print(gene.translate(table = "Bacterial"))
print(gene.translate(table = "Bacterial", to_stop = True))
print(gene.translate(table = "Bacterial", cds = True))

