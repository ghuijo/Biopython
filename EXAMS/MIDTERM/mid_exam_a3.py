# Midterm exam_a3

from Bio import SeqIO

print("genbank 형식")
for seq_record in SeqIO.parse("Helicobacter.gb", "genbank"):
    print("염기 수: ", len(seq_record))
    print("id: ", seq_record.id)
    print("name: ", seq_record.name)
    print("description: ", seq_record.description)
    print("annotations: ", seq_record.annotations, "\n")


print("fasta 형식")
for seq_record in SeqIO.parse("Helicobacter.fasta", "fasta"):
    print("염기 수: ", len(seq_record))
    print("id: ", seq_record.id)
    print("name: ", seq_record.name)
    print("description: ", seq_record.description)
    print("annotations: ", seq_record.annotations, "\n")

