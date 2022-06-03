# BioPython
# L2. Bioinfomatics tool - BLAST


''' if it doesn't work, change the path
import os
os.chdir("your path")
'''


# implement Blast using biopython
from Bio.Blast import NCBIWWW
from Bio import SeqIO

record = SeqIO.read("ls_orchid_first.fasta", format="fasta")
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

