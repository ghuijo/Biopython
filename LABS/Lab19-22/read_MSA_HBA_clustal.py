from Bio import AlignIO

alignment = AlignIO.read("HBA.aln", "clustal")
print(alignment)

alignment = AlignIO.parse("HBA.aln", "clustal")
for record in alignment:
    print(record)
