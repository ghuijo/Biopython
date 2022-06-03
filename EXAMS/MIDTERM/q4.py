from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

seq_record = SeqIO.read("sequence0.fasta", "fasta")
seq_record.annotations['molecule_type'] = 'DNA'


SeqIO.write(seq_record, "sequence0.gbk", "genbank")


