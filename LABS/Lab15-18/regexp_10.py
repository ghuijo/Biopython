
def iub_to_RE(iub):
     dic = {"A":"A", "C":"C", "G":"G", "T":"T", "R":"[GA]", "Y":"[CT]", 
     "M":"[AC]", "K":"[GT]", "S":"[GC]", "W":"[AT]", "B":"[CGT]", 
     "D":"[AGT]", "H":"[ACT]", "V":"[ACG]", "N":"[ACGT]", ".":" ","-":" "}
     site = iub.replace("^", "")
     regexp = ""
     for c in site:
          regexp += dic[c]
     return regexp
      
def test():
     print(iub_to_RE("G^AMTV"))

test()

