from Bio import AlignIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

alignment = AlignIO.read("HBA.aln", "clustal")
records = []

for aligns in alignment:
    s = Seq(str(aligns.seq))
    record = SeqRecord(s, id = aligns.id, name = "", description = "", )
    records.append(record)

SeqIO.write(records, "records.fasta", "fasta")
