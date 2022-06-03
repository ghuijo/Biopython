# hw2_1_sol

import re

def find_all_re(seq, rgx):
 answer = rgx.findall(seq)
 print(answer)

def test():
 seq = input("Input Sequence: ")
 rgx = re.compile('GT...TACTAAC...AC')
 find_all_re(seq, rgx)

test()
