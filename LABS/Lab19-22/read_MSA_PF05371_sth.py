from Bio import AlignIO

alignment = AlignIO.read("PF05371_seed.sth", "stockholm")
print(alignment)
