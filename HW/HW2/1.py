#과제2_1

from re import search
from re import finditer

def pattern_find(seq, pat):
    mos = finditer(pat, seq)
    result = ""
    pat_info = []
    for x in mos:
        result = x.group()
        pat_info.append(result)
    print(pat_info)

# main

seq = input("DNA 서열을 입력하시오: ")
pat = input("찾는 패턴을 입력하시오: ")

pattern_find(seq, pat)

