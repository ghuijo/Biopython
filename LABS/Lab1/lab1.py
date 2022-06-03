# BioPython
# L1. Introduction


# working with sequences
from Bio.Seq import Seq

my_seq = Seq("AGTACACTGGT")
print(my_seq)
print(my_seq.complement())
print(my_seq.reverse_complement())



# simple FASTA parsing example
from Bio import SeqIO

for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))



# simple GenBank parsing example
from Bio import SeqIO

for seq_record in SeqIO.parse("ls_orchid.gbk", "genbank"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))



# efetch
from Bio import GenBank
from Bio import Entrez

Entrez.email = 'yourid@example.com'
handle = Entrez.efetch(db = 'nucleotide', id = 'KT225476', rettype = 'gb', retmode = 'text')
record = GenBank.read(handle)

print("Accession: ", record.accession)
print("Organism: ", record.organism)
print("Size: ", record.size)



# EGQuery: simple example
from Bio import Entrez

Entrez.email = 'yourid@example.com'
handle = Entrez.egquery(term = "bioinformatics")
record = Entrez.read(handle)
for result in record['eGQueryResult']:
    if result['DbName'] == 'pubmed':
        print(result['Count'])


