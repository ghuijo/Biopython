from re import search
import re

pat = re.compile("[0-9]{3,5}")
seq1 = "000"

seq2 = "0000"

seq3 = "00000"

seq4 = "000000"

seq5 = "00"

print(search(pat, seq1))

print(search(pat, seq2))

print(search(pat, seq3))

print(search(pat, seq4))

print(search(pat, seq5))

