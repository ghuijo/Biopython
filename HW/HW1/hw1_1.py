# hw1_1

# 사용자로부터 DNA 서열 입력 받기
DNA_seq = input("DNA 서열을 대문자로 입력하시오: ")

# 서열 내 염기 개수와 유효하지 않은 문자 개수를 담을 변수 초기화
Ti = Cy = Ad = Gu = non_valid = 0

# 서열 내 염기를 돌면서 각 염기별 개수와 유효하지 않은 문자 개수 카운트
for i in DNA_seq:
    if (i == "T"): Ti += 1
    elif (i == "C"): Cy += 1
    elif (i == "A"): Ad += 1
    elif (i == "G"): Gu += 1
    else: non_valid += 1

# 유효하지 않은 숫자를 제외한 서열 길이 저장
len_seq = len(DNA_seq) - non_valid

# 각 염기 비율 계산
rateT = Ti/len_seq * 100
rateC = Cy/len_seq * 100
rateA = Ad/len_seq * 100
rateG = Gu/len_seq * 100

# 사용자에게 출력
print("T : %.2f%%, C : %.2f%%, A : %.2f%%, G : %.2f%%" % (rateT, rateC, rateA, rateG))
print("유효하지 않은 문자 : %d개" % non_valid)

