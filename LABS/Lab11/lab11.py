# BioPython
# L11. Pattern Matching I

def search_first_occ(seq, pattern):
    found = False
    i = 0
    while i <= len(seq) - len(pattern) and not found:
        j = 0
        while j < len(pattern) and pattern[j] == seq[i + j]:    j += 1
        if j == len(pattern):   found = True
        else:   i += 1
    if found:   return i
    else:   return -1

def search_all_occ(seq, pattern):
    res = []
    for i in range(len(seq) - len(pattern) + 1):
        j = 0
        while j < len(pattern) and pattern[j] == seq[i + j]:    j += 1
        if j == len(pattern):   res.append(i)
    return res

def test_pattern_search():
    seq = input("Input sequence: ")
    pat = input("Input pattern: ")
    print(pat, "occurs in the following positions:",)
    print(search_first_occ(seq, pat))
    print(search_all_occ(seq, pat))

test_pattern_search()


