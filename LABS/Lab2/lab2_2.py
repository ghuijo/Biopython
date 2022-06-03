# BioPython
# L2. Bioinfomatics tool - BLAST


# implement Blast with several options using biopython
from Bio.Blast import NCBIWWW

result_handle = NCBIWWW.qblast("blastn", "nt", "8332116")

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
