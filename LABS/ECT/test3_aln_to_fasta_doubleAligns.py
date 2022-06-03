from Bio import AlignIO

count = AlignIO.convert("doubleAligns.aln", "clustal", "doubleAligns.fasta", "fasta", molecule_type = "protein")
print("Converted %i alignments" % count)
