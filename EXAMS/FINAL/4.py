from Bio import AlignIO
from Bio.motifs import Motif
from Bio import motifs
from Bio.Seq import Seq

count = AlignIO.convert("uniprot.sth", "stockholm", "PF18225.aln", "clustal")


alignment = AlignIO.read("PF18225_.aln", "clustal")

instances = []

for record in alignment:
    s = Seq(str(record.seq))
    instances.append(s)
    
m = motifs.create(instances)
Motif.weblogo(m,"PF18225_WebLogo.jpg")
