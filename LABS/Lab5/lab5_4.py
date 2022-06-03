# Lab5_4

#1#########################################################################
from Bio.Seq import Seq

my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")

print(my_seq)

print(my_seq[::-1])

print(my_seq.complement())

print(my_seq.reverse_complement())

print("")


#2#########################################################################
my_seq = "GATCGATGGGCCTATATAGGATCGAAAATCGC"

print(my_seq)

print(my_seq[::-1])

print(my_seq.complement())      # 오류 발생

print(my_seq.reverse_complement())      # 오류 발생


