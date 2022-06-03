from Bio.Align.Applications import MuscleCommandline

muscle_exe = "C:\\Users\\eldel\\appdata\\local\\programs\\python\\python39\\muscle3.8.31_i86win32.exe"
cmd_line = MuscleCommandline(muscle_exe, input="PF18225.fasta", out="PF18225.aln", clw=" ")
print(cmd_line)
stdout, stderr = cmd_line()


from Bio import AlignIO
from Bio.motifs import Motif
from Bio import motifs
from Bio.Seq import Seq

alignment = AlignIO.read("PF18225_.aln", "clustal")

instances = []

for record in alignment:
    s = Seq(str(record.seq))
    instances.append(s)
    
m = motifs.create(instances, "ACDEFGHIKLMNPQRSTVWY")
Motif.weblogo(m,"PF18225_WebLogo.jpg")
