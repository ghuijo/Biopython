from Bio import AlignIO

alignment = AlignIO.parse("HBA.aln", "clustal")
for record in alignment:
    print(record)
