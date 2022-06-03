import re
  
# lookahead example
example0 = re.search('ata(?=[a-z])', "aaatatagcgccatatagc"  )
print("Pattern:", example0.group())
print("Pattern found from index:",
      example0.start(), "to",
      example0.end())

example1 = re.search('ata(?=[0-9]])', "aaatatagcgccatatagc")
print(example1)

# without using lookahead
example2 = re.search('ata([a-z])', "aaatatagcgccatatagc")
print('Without using lookahead:', example2.group())
print("Pattern found from index:",
      example2.start(), "to",
      example2.end())

example1 = re.search('ata(?=.)', "aaata)tagcgccatatagc")
print(example1)
