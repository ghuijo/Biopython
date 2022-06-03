import re

def translate_codon_re(cod):
    if re.search("GC.", cod): aa = "A"
    elif re.search("TG[TC]", cod): aa = "C"
    elif re.search("GA[TC].", cod): aa = "D"
    elif re.search("GA[AG]", cod): aa = "E"
    elif re.search("TT[TC]", cod): aa = "F"
    elif re.search("GG.", cod): aa = "G"
    elif re.search("CA[TC]", cod): aa = "H"
    elif re.search("AT[TCA]", cod): aa = "I"
    elif re.search("AA[AG]", cod): aa = "K"
    elif re.search("TT[AG]|CT.", cod): aa = "L"
    elif re.search("ATG", cod): aa = "M"
    elif re.search("AA[TC]", cod): aa = "N"
    elif re.search("CC.", cod): aa = "P"
    elif re.search("CA[AG]", cod): aa = "Q"
    elif re.search("CG.|AG[AG]", cod): aa = "R"
    elif re.search("TC.|AG[TC]", cod): aa = "S"
    elif re.search("AC.", cod): aa = "T"
    elif re.search("GT.", cod): aa = "V"
    elif re.search("TGG", cod): aa = "W"
    elif re.search("TA[TC]", cod): aa = "Y"
    elif re.search("TA[AG]|TGA", cod): aa = "_" # _는 종결코돈
    else: aa =""
    return aa
  
print(translate_codon_re("GTATCG"))
# GTA는 거의 맨 아래에 있으므로 그 전에 ATC 발견-> I 출력됨

print(translate_codon_re("GTA"))
print(translate_codon_re("CAT"))
print(translate_codon_re("CAC"))
print(translate_codon_re("CAA"))
print(translate_codon_re("TAG"))
print(translate_codon_re("UAT"))

