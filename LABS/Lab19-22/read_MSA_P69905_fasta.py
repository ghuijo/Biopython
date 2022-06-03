from Bio import AlignIO

alignment = AlignIO.read("P69905.fasta", "fasta")
print(alignment)


from Bio import SeqIO

alignment = SeqIO.read("P69905.fasta", "fasta")
print(alignment)
