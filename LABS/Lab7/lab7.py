import os
os.chdir("your path")

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord     # Bio.SeqSecord에서 SeqRecord를 import

seq = Seq("ACGT")   # 먼저 Sequence 객체를 만든다
seqRecord = SeqRecord(seq)  # SeqRecord 객체를 만든다

print(seqRecord)    # seqRecord는 하나의 객체임

print("")


from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

seq = Seq("ACGT")
seqRecord = SeqRecord(seq, id = "NC_1111", name = "Test")

print(seqRecord)

print("")


from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

seq = Seq("ACGT")
seqRecord = SeqRecord(seq, id = "NC_1111", name = "Test")
seqRecord.name = "New name"

print(seqRecord)

print("")


from Bio import SeqIO

record = SeqIO.read("J01636.1.fasta", "fasta")  # seqRecord 타입으로 읽어옴

print(type(record))
print(record)

print("")


from Bio import SeqIO

record = SeqIO.read("Ecoli.gb", "genbank")
print(type(record))
print(record)

print("")


str1 = "acgt"
str2 = 'acgt'

print(str1)
print(str2)
print(str1 == str2)  # boolean 타입으로 결과 반환

print("")


from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

seq1 = Seq("ACGT")
record1 = SeqRecord(seq1)
print(record1)

seq2 = Seq("ACGT")
record2 = SeqRecord(seq2)
print(record2)

print(record1.seq == record2.seq)
print(record1.name == record2.name)
# print(record1 == record2)
# 오류 발생, 관심 있는 객체의 정보를 explicitly compare할 것.

print("")


