from re import search   # 메소드
from re import finditer # 메소드

def find_pattern_re(seq, pat):  # seq, pat 모두 문자열
    mo = search(pat, seq)   # 메소드를 import해주었으므로 re.search할 필요 없음
    if (mo != None ) :  # mo는 결과를 담은 객체
        return mo.span()[0] # span()은 인덱스를 반환해줌
    else:
        return -1
    
def find_all_occurrences_re(seq, pat):  # 어디서 발견됐는지 모두 찾음
    mos = finditer(pat, seq)
    res = []
    for x in mos:
         res.append(x.span()[0])
    return res

def test():
    seq = input("Input sequence:")
    pat = input("Input pattern ( as a regular expression):")
    
    res = find_pattern_re(seq, pat)
    if res >= 0:
        print("Pattern found in position: ", res)
    else: print("Pattern not found")    # 패턴이 발견 안 될 경우 -1

    all_res = find_all_occurrences_re(seq, pat)
    if len(all_res) > 0:
        print("Pattern found in positions: ", all_res)
    else: print("Pattern not found")

test()

