#과제2_3
'''
from re import search
from re import finditer

def find_motif(seq):
    regexp = "Y..F[YT]"
    res = search(regexp, seq)
    result = []
    if (res != None):
        res = finditer(regexp, seq)
        for x in res:
            result.append(x.start())
        return result
    else:
        return -1

# main
seq = input("단백질 서열을 입력하시오: ")
print(find_motif(seq))
'''

from re import search
from re import finditer

def find_motif(seq):
    regexp = "Y..F[YT]"
    res = search(regexp, seq)
    result = []
    if (res != None):
        res = finditer(regexp, seq)
        for x in res:
            result.append((x.group(), x.start()))
        t = tuple(result)
        return t
    else:
        return "발견되지 않았습니다"

# main
seq = input("단백질 서열을 입력하시오: ")
print(find_motif(seq))


