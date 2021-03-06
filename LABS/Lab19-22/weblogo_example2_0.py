from Bio import AlignIO
from Bio.motifs import Motif
from Bio import motifs
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

alignment = AlignIO.read("HBA.aln", "clustal")

instance = []

for record in alignment:
    s = Seq(str(record.seq), IUPAC.protein)
    instance.append(s)
    
m = motifs.create(instance, "ACDEFGHIKLMNPQRSTVWY")
Motif.weblogo(m,"HBA_WebLogo.jpg")

