# BioPython
# L9. SeqIO Module I


# 1. SeqIO Module
from Bio import SeqIO
help(SeqIO)
print("\n")


# 2. read()
from Bio import SeqIO
record = SeqIO.read("J01636.1.fasta","fasta")
print(type(record))
print(record, "\n")

from Bio import SeqIO
record = SeqIO.read("Ecoli.gb","genbank")
print(type(record))
print(record, "\n")


# 3. parse()_Bio.SeqIO.parse() gives a SeqRecord iterator one by one
from Bio import SeqIO
for seq_record in SeqIO.parse("./ls_orchid.fasta", "fasta"):
     print(seq_record.id)
     print(repr(seq_record.seq))
     print(len(seq_record))
print("")

from Bio import SeqIO
for seq_record in SeqIO.parse("./ls_orchid.gbk", "genbank"):
     print(seq_record.id)
     print(repr(seq_record.seq))
     print(len(seq_record))
print("")


# 3_More than one record in your files
from Bio import SeqIO
record_iterator= SeqIO.parse("./yeast.gbk", "genbank")
first_record= next(record_iterator)
print(first_record.id)
print(first_record.description)
second_record= next(record_iterator)
print(second_record.id)
print(second_record.description, "\n")


# 3_Turn the “record iterator” into a list of SeqRecord objects using list()
from Bio import SeqIO
records = list(SeqIO.parse("./yeast.gbk", "genbank"))
print("Found %irecords" % len(records))
print("The last reord")
last_record= records[-1]
print(last_record.id)
print(repr(last_record.seq))
print(len(last_record))
print("The first record")
first_record= records[0]
print(first_record.id)
print(repr(first_record.seq))
print(len(first_record))

print("")


# 3_Extracting data from your files (Genbank format)
from Bio import SeqIO
record_iterator = SeqIO.parse("./yeast.gbk", "genbank")
first_record = next(record_iterator)
print(first_record, "\n")
print(first_record.annotations, "\n")     # dictionary 형태로 출력해줌
print(first_record.annotations.keys(), "\n")
print(first_record.annotations.values(), "\n")
print(first_record.annotations['source'],"\n")
print(first_record.annotations['organism'], "\n")

from Bio import SeqIO
all_species = []
for seq_record in SeqIO.parse("ls_orchid.gbk", "genbank"):
    all_species.append(seq_record.annotations['organism'])
print(all_species, "\n")


# 3_Extracting data from your files (Fasta format)
from Bio import SeqIO
all_species = [
    seq_record.description.split()[1]
    for seq_record in SeqIO.parse("yeast.fasta", "fasta")
]
print(all_species, "\n")

from Bio import SeqIO
all_species = [
    seq_record.description.split()[1]
    for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta")
]
print(all_species, "\n")

all_species = []
for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
    all_species.append(seq_record.description.split()[1])
print(all_species, "\n")

