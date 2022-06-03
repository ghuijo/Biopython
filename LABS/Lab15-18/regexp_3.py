import re

seq = "AAATAGAGATGAAGAGAGATAGCGC"
rgx = re.compile("GA.A")
rgx.search(seq).group()
rgx.findall(seq)
mo = rgx.finditer(seq)
for x in mo: print(x.span())

