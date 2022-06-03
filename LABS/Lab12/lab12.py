# BioPython
# L12. Pattern Matching II

from BM import *

def test_pattern_search():
    seq = input("input sequence: ")
    pat = input("input pattern: ")
    print(pat, "occurs in the following positions:",)
    bm = BoyerMoore("ACTG", pat)
    print(bm.search_pattern(seq))

test_pattern_search()

