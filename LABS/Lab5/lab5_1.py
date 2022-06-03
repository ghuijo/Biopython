# Lab5_1


#1#########################################################################
from Bio.Seq import Seq

my_seq = Seq("GATCG")

for index, letter in enumerate(my_seq):
    print("%i %s" %(index, letter))

print(my_seq[0])
print(my_seq[-1])
print(my_seq[-3])
print(my_seq[-5])

print("")


#2#########################################################################
from Bio.Seq import Seq

print("AAAA".count("AA"))
print(Seq("AAAA").count("AA"))

print("")


#3#########################################################################
from Bio.Seq import Seq

my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")

print(len(my_seq))

print(my_seq.count("G"))
print(my_seq.count("C"))

print(100 * float(my_seq.count("G") + my_seq.count("C")) / len(my_seq))

print("")


#4#########################################################################
from Bio.Seq import Seq
from Bio.SeqUtils import GC

my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print(GC(my_seq))

