from Bio import AlignIO

alignment = AlignIO.read("HBA.aln", "clustal")
for record in alignment:
    print("%s - %s" % (record.seq[:10], record.id))

