# Midterm exam_a3_2

from Bio import SeqIO

record = SeqIO.read("Helicobacter.gb", "genbank")
print(len(record.seq))
print(record.id)
print(record.name)
print(record.description)
print(record.annotations)


record = SeqIO.read("Helicobacter.fasta", "fasta")
print(len(record.seq))
print(record.id)
print(record.name)
print(record.description)
print(record.annotations)

