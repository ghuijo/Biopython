from re import finditer
from Bio.Seq import Seq

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
    positions.insert(0,0)
    positions.append(len(sequence))
    for i in range(len(positions)-1):
        res.append(sequence[positions[i]:positions[i+1]])
    return res
  

def test():
    print("제한효소에 의해 절단된 DNA 서열들의 정보")
    seq = "CGAATTTATTGAATTCGTAAAATTTTAAGTTAAATTCTAACGT"
    pos = cut_positions("R^AATTY", seq)   	   
    print(pos)
    print(cut_subsequences(pos, seq))
    print()
    
    print("제한효소에 의해 절단된 상보적 DNA 서열들의 정보")
    sequences = Seq(seq)
    seq_reversed = sequences.reverse_complement()
    pos_reversed = cut_positions("R^AATTY", str(seq_reversed))   	   
    print(pos_reversed)
    print(cut_subsequences(pos_reversed, str(seq_reversed)))

test()
