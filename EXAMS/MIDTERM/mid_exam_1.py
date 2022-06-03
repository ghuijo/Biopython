# Midterm exam_1

s1 = BioSeq("ATAATGATAGATAGATGAT")
print(len(s1))
print(s1.get_seq_biotype())
s1.show_info_seq()
print(s1.count_ocuur('AT'))
print('')

s1 = BioSeq("AUAAUAUAGA", "RNA")
print(len(s1))
print(s1.get_seq_biotype())
print(s1.seq[4])
print(s1.seq[2:5])
s1.show_info_seq()
print('')

s1 = BioSeq("MARKKVSJEVPYW", "PROTEIN")
print(len(s1))
print(s1.seq[0])
s1.show_info_seq()

