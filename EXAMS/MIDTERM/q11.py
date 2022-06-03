from q1 import BioSeq

s1 = BioSeq("ATAATGATAGATAGATGAT")
print(len(s1))
print(s1.get_seq_biotype())
s1.show_info_seq()
print(s1.count_occir('AT'))
print('')
