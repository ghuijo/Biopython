import re


p = re.compile('[a-z]+')    # 패턴을 p에 저장
m = p.match("python")     
print(m.group())        # 매치된 문자열을 돌려준다.
print(m.span())         # 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.

m = re.match('[a-z]+', "python")
print(m.group())
print(m.span())

text = "문의사항이 있으면 010-1234-5678 으로 연락주시기 바랍니다."
 
regex = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')
matchobj = regex.search(text)
phonenumber = matchobj.group()
print(phonenumber) 


text = "문의사항이 있으면 010-1234-5678 으로 연락주시기 바랍니다."
matchobj = re.search("\d\d\d-\d\d\d\d-\d\d\d\d", text)
print(matchobj.group()) 


text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류"
regex = re.compile("에러\s\d+")
mc = regex.findall(text)    # 목록으로 반환-> 리스트 형태로 반환
print(mc)


text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류"
regex = re.compile("에러 1033")
mo = regex.search(text)
if mo != None:
    print(mo.group())


text = "문의사항이 있으면 010-1234-5678 으로 연락주시기 바랍니다."
 
regex = re.compile(r'(\d{3})-(\d{4}-\d{4})')
matchobj = regex.search(text)
areaCode = matchobj.group(1)
num = matchobj.group(2)
fullNum = matchobj.group()
print(areaCode, num)
print(fullNum)

text = "문의사항이 있으면 010-1234-5678 으로 연락주시기 바랍니다."
regex = re.compile(r'(?P<area>\d{3})-(?P<num>\d{4}-\d{4})')
matchobj = regex.search(text)
areaCode = matchobj.group("area")
num = matchobj.group("num")
print(areaCode, num)  

