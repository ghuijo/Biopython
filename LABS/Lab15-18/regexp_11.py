from re import finditer


def iub_to_RE(iub):
     dic = {"A":"A", "C":"C", "G":"G", "T":"T", "R":"[GA]", "Y":"[CT]", 
     "M":"[AC]", "K":"[GT]", "S":"[GC]", "W":"[AT]", "B":"[CGT]", 
     "D":"[AGT]", "H":"[ACT]", "V":"[ACG]", "N":"[ACGT]", ".":" ","-":" "}
     site = iub.replace("^", "")
     regexp = ""
     for c in site:
          regexp += dic[c]
     return regexp


def  cut_positions(enzyme, sequence):
     cutpos = enzyme.find("^")
     regexp = iub_to_RE(enzyme)
     matches = finditer(regexp, sequence)
     locs = []
     for m in matches:
         locs.append(m.start() + cutpos)
     return locs

def cut_subsequences(locs, sequence):
    res = []
    positions = locs
    positions.insert(0,0)     # [0, 7, 19]
    positions.append(len(sequence))     # [0, 7, 19, 23]
    for i in range(len(positions)-1): # len(positions)-1 = 3번 반복(0,1,2)
        res.append(sequence[positions[i]:positions[i+1]])
        # sequence[0:7], sequence[7:19], sequence[19:23]
    return res
  

def test():
     pos = cut_positions("G^ATTC", "GTAGAAGATTCTGAGATCGATTC")   	   
     print(pos)
     print(cut_subsequences(pos, "GTAGAAGATTCTGAGATCGATTC"))

test()


