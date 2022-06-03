from re import search
from re import finditer

def find_pattern_re(seq, pat):
    mo = search(pat, seq)
    if (mo != None ) :
        return mo.span()[0]
    else:
        return -1
    
def find_all_occurrences_re(seq, pat):
    mos = finditer(pat, seq)
    res = []
    for x in mos:
         res.append(x.span()[0])
    return res

def find_all_overlap(seq, pat):
    return find_all_occurrences_re(seq, "(?="+pat+")")

def test():
    seq = input("Input sequences: ")
    pat = input("Input pattern ( as a regular expression):")

    res = find_pattern_re(seq, pat)
    if res >= 0:
       print("Pattern found in position: ", res)
    else: print("Pattern not found")
    

    all_res = find_all_occurrences_re(seq, pat)
    if len(all_res) > 0:
        print("Pattern found in positions: ", all_res)

    all_ov = find_all_overlap(seq, pat)
    if len(all_ov) > 0: # 0보다 크면 overlap되는 부분이 있다
        print("Pattern found in positions (overlap): ", all_ov)
    else:
        print("Pattern not found")

test()

