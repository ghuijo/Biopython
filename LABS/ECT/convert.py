from Bio import AlignIO

count = AlignIO.convert("PF05371.aln", "clustal", "PF05371.newick", "newick", molecule_type = "protein")
print("Converted %i alignments" % count)
