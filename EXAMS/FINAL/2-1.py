from re import search


def validate_protein_re(seq):
    if search("[^ACDEFGHIKLMNPQRSTVWY]", seq) != None:
        return False
    else:
        return True

seq = input("단백질 서열 여부를 확인할 서열 데이터를 입력하시오: ")
print(validate_protein_re(seq))
