# hw1_2

# Seq 클래스 import
from Bio.Seq import Seq

# DNA 염기 서열 담을 Seq 객체 생성
DNA_coding_strand = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
print("%-25s" % "DNA coding strand 객체", DNA_coding_strand)

# template 객체 생성
DNA_template_strand = DNA_coding_strand.complement()
print("%-25s" % "DNA template strand 객체", DNA_template_strand)

# 전사를 통해 mRNA 객체 생성
mRNA = DNA_template_strand.transcribe()
print("%-25s" % "mRNA 객체", mRNA)

# 번역을 통해 protein 객체 생성
protein = mRNA.translate()
print("%-25s" % "protein 객체", protein)

