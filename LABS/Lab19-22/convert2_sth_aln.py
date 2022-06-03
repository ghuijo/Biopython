from Bio import AlignIO

alignment = AlignIO.read("PF05371_seed.sth", "stockholm")
AlignIO.write([alignment],"PF05371_seed0.aln", "clustal")

