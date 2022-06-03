# Lab8
# point mutation (3 types)

from Bio.Seq import MutableSeq

mutable_seq = MutableSeq("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA")
print(mutable_seq)

mutable_seq[5] = "C"    # base substitution
print(mutable_seq)

mutable_seq.remove("T")     # 제일 처음 T를 remove
print(mutable_seq)          # deletion

mutable_seq.insert(4, "T")  # insertion
print(mutable_seq)

print("")


