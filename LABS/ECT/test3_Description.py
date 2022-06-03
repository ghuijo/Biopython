from Bio import SeqIO
all_species = [
    seq_record.description.split()[3]
    for seq_record in SeqIO.parse("yeast.fasta", "fasta")
]
print(all_species, "\n\n")


all_species = [
    seq_record.description
    for seq_record in SeqIO.parse("yeast.fasta", "fasta")
]
print(all_species, "\n\n")
