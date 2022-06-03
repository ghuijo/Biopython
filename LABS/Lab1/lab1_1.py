# Biopython
# 1. Biopython introduction
# 1-1 FASTA file parsing


from Bio import SeqIO
record = SeqIO.read("hemoglobin_subunit_beta.fasta", "fasta")
print(record.id)
print(len(record.seq))
print(record.seq.count("A"))


from Bio import Entrez
Entrez.email =  "yourid@example.com"
handle = Entrez.egquery(term="bioinformatics")
record = Entrez.read(handle)
for result in record['eGQueryResult']:
    if result['DbName'] == 'pubmed':
        print(result['Count'])


from Bio import Entrez
from Bio import GenBank
handle = Entrez.efetch(db="nucleotide", id="KT225476",
                       rettype='gb', retmode='text')
record = GenBank.read(handle)
print("Accesion: ", record.accession)
print("Organism: ", record.organism)
print("Size: ", record.size)


from Bio import SeqIO
for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))


from Bio import SeqIO
for seq_record in SeqIO.parse("ls_orchid.gbk", "genbank"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))


from Bio import Entrez
Entrez.email = "yourid@example.com"
handle = Entrez.egquery(term='biopython')
record = Entrez.read(handle)
for row in record["eGQueryResult"]:
    print(row["DbName"], row["Count"])


from Bio.Blast import NCBIWWW
from Bio import SeqIO
record = SeqIO.read("blastSample.fasta", format="fasta")
result_handle = NCBIWWW.qblast("blastn", "nt", record.format("fasta"))
with open("blast_result.xml", "w") as out_handle:
    out_handle.write(result_handle.read())
result_handle.close()

from Bio.Blast import NCBIXML
result_handle = open("blast_result.xml")
blast_records = NCBIXML.parse(result_handle)
for blast_record in blast_records:
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            print(alignment.title)
            print(alignment.length)
            print(hsp.expect)
            print(hsp.query)
            print(hsp.match)
            print(hsp.sbjct)
            print("")
result_handle.close()


