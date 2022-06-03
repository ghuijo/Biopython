# Midterm exam_a2

from Bio.Seq import MutableSeq
from Bio.SeqUtils import GC

seq = MutableSeq("TGTAACGAACGGTGCAATAGTGATCCACACCCAACGCCTGAAATCAGATCCAGGGGGTAATCTGCTCTCC")
print(seq)

seq[3] = "C"
print(seq)

del seq[1]      # seq.pop(1)
print(seq)

seq.insert(8, "G")
print(seq)

gc_contents = GC(seq)
print("GC 함량: ", gc_contents)

