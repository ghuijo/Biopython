# Lab6_1

#1#########################################################################
from Bio.Seq import Seq

seq = Seq("tataaaggcaatatgcagtagggca")

comp_seq = seq.complement()
revcomp_seq = seq.reverse_complement()

print(comp_seq)
print(revcomp_seq)

print("")


#2#########################################################################
seq = "tataaaggcaatatgcagtagggca"

comp_dic = {'a':'t', 'c':'g', 'g':'c', 't':'a'}
comp_seq = ""

for s in seq:       # s의 자료형은 char로, seq에 있는 문자 하나하나가 담김.
    comp_seq += comp_dic[s]     # 문자와 문자를 concatenate

revcomp_seq = comp_seq[::-1]

print(comp_seq)
print(revcomp_seq)

print(comp_dic["a"]) # key로 대문자 'A' 주면 error 발생

print("")


#3#########################################################################
from Bio.Seq import Seq

seq = Seq("tataaaggcaatatgcagtagggca")

comp_dic = {'a':'t', 'c':'g', 'g':'c', 't':'a'}
comp_seq = ""

for s in seq:
    comp_seq += comp_dic[s]

revcomp_seq = comp_seq[::-1]

print(comp_seq)
print(revcomp_seq)

print("")


#4#########################################################################
from Bio.Seq import Seq

tatabox_seq = Seq("TATAAAGGCAATATGCAGTAG")
print(tatabox_seq)
print(type(tatabox_seq))

print("")


#5#########################################################################
from Bio.Data import CodonTable

codon_table = CodonTable.unambiguous_dna_by_name["Standard"]
print(codon_table)

print("")


#6#########################################################################
from Bio.Data import CodonTable

codon_table = CodonTable.unambiguous_dna_by_name["Vertebrate Mitochondrial"]
print(codon_table)

print("")


#7#########################################################################
from Bio.Seq import Seq

""" original sequence인 tatabox_seq에서 atg를 찾아라.
    없으면 start_idx -1 반환
    start 인덱스부터 끝까지 중에서 tag 찾아라
"""
tatabox_seq = Seq("tataaaggcaatatgcagtagggca")
start_idx = tatabox_seq.find("atg") 
end_idx = tatabox_seq.find("tag", start_idx)
orf = tatabox_seq[start_idx:end_idx+3]  # end_idx 18 + 3 -1까지

print(orf)  # open read frame (?)
print(start_idx)
print(end_idx)

print("")


#8#########################################################################
from Bio.Seq import Seq
from Bio.SeqUtils import GC

exon_seq = Seq("atgcagtag")
gc_contents = GC(exon_seq)
print(gc_contents)

print("")


#9#########################################################################
from Bio.Seq import Seq
from Bio.SeqUtils import molecular_weight

seq1 = Seq("ATGCAGTAG")
print(molecular_weight(seq1))
seq2 = seq1.transcribe()
print(molecular_weight(seq2, seq_type = "RNA"))
print(molecular_weight(seq1, seq_type = "protein"))

print("")


#10########################################################################
from Bio.Seq import Seq
from Bio.SeqUtils import six_frame_translations

seq1 = Seq("ATGCCTTGAAATGTATAG")
print(six_frame_translations(seq1))

print("")


#11########################################################################
from Bio.Seq import Seq
from Bio.SeqUtils import MeltingTemp as mt

seq1 = Seq("ATGCCTTGAAATGTATGGGGGCCCCCCCAG")
print(mt.Tm_Wallace(seq1))

print("")


#12########################################################################
from Bio.SeqUtils import seq1
# seq1 메소드는 아미노산 서열 기호를 약자로 변환시킴

essential_amino_acid_3 = "LeuLysMetValIleThrTrpPhe"
print(seq1(essential_amino_acid_3))

print("")


#13########################################################################
from Bio.SeqUtils import seq3

essential_amino_acid_3 = "LKMVITWF"
print(seq3(essential_amino_acid_3))

print("")

