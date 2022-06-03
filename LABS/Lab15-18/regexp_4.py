import re

rgx = re.compile("(TATA..)((GC){3})")
seq = "ATATAAGGCGCGCCTTATGCGC"
result = rgx.search(seq)

print(result.group(0))
print(result.group(1))
print(result.group(2))

