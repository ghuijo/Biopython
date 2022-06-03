from Bio import AlignIO

alignment = AlignIO.read("PF05371_seed.sth", "stockholm")
print("Alignment length %i" % alignment.get_alignment_length())
for record in alignment:
    print("%s - %s" % (record.seq, record.id))
