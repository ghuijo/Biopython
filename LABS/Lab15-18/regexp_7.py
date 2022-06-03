import re

def largest_protein_re(seq_prot):
     mos = re.finditer("M[^_]*_", seq_prot)  # 중간에 종결코돈 아닌 것(M 포함)의 반복 가능
     sizem = 0
     lprot = ""
     for x in mos:
         ini = x.span()[0]    # M이 시작하는 부분의 인덱스
         fin = x.span()[1]    # 종결코돈 _으로 끝나는 부분의 인덱
         s = fin - ini + 1    # 발견한 패턴의 사이즈(길이)
         if s> sizem:    # 계속 패턴들의 길이 비교
            lprot = x.group()
            sizem = s
     return lprot   # 가장 긴 단백질 서열 리턴

print(largest_protein_re("MHCAMATVWV_MAAAT_"))
print(largest_protein_re("MHCAMATVWV_MAAAHHHHVYYWWAAT_"))

