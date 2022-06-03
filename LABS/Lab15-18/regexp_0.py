import re

str = "TGAAGTATGAGA"

mo = re.search("TAT", str)
print(mo.group())
print(mo.span())

mo2 = re.search("TG.", str)
print(mo2.group())
print(mo2.span())

re.findall("TA.", str)
re.findall("TG.", str)

mos = re.finditer("TG.", str)
for x in mos:
    print(x.group())
    print(x.span())
