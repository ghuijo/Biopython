from Bio.Data import CodonTable

codon_table = CodonTable.unambiguous_dna_by_id[2]
print(codon_table)

print("")

codon_table = CodonTable.standard_dna_table
print(codon_table)

print("")

codon_table = CodonTable.generic_by_id[2]
print(codon_table)

print("")


codon_table = CodonTable.unambiguous_dna_by_name["Bacterial"]
print(codon_table)

print("")


