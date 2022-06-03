# Midterm exam_a4

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

rec = SeqIO.read("sequence0.fasta", "fasta")
print(len(rec.seq))
seq = rec.seq

record = SeqRecord(seq, id=rec.id, name = rec.name, description=rec.description, annotations={"molecule_type":"DNA"})

SeqIO.write(record, "sequence0.gbk", "genbank")

