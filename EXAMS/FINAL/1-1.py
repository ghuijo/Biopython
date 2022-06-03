from re import finditer
import re


def find_all_re(seq, rgx):
    answer = rgx.finditer(seq)

    pat_info = []
    for x in answer:
        result = [x.group(), x.span()]
        pat_info.append(result)
    print(pat_info)

def test():
    seq = "CAGACTTTCAGAACTGTCAGTTCCCCGGATTTTACCCATCACATTTTGCTACTACTTTCTACTACTATATACTTTTCCAATTTCATACGGGTACTATTATCCATACTCTACTATTAC"

    pat1 = re.compile("CATT")
    find_all_re(seq, pat1)
    
    pat2 = re.compile("ACT+C")
    find_all_re(seq, pat2)

    pat3 = re.compile("AC.*GAA.*AG")
    find_all_re(seq, pat3)
    

test()
