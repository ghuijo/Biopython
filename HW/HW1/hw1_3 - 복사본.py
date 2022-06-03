# hw1_3

aminoF = [ "TTT", "TTC" ]
aminoL = [ "TTA", "TTG", "CTT", "CTC", "CTA", "CTG" ]
aminoS = [ "TCT" ,"TCC", "TCA", "TCG", "AGT", "AGC" ]
aminoY = [ "TAT", "TAC" ]
aminoC = [ "TGT", "TGC" ]
aminoW = [ "TGG" ]
aminoP = [ "CCT", "CCC", "CCA", "CCG" ]
aminoH = [ "CAT", "CAC" ]
aminoQ = [ "CAA", "CAG" ]
aminoR = [ "CGT", "CGC", "CGA", "CGG" ]
aminoI = [ "ATT", "ATC", "ATA" ]
aminoM = [ "ATG" ]
aminoT = [ "ACT", "ACC", "ACA", "ACG" ] 
aminoN = [ "AAT", "AAC" ]
aminoK = [ "AAA", "AAG" ]
aminoV = [ "GTT", "GTC", "GTA", "GTG" ]
aminoA = [ "GCT", "GCC", "GCA", "GCG" ]
aminoD = [ "GAT", "GAC" ]
aminoE = [ "GAA", "GAG" ]
aminoG = [ "GGT", "GGC", "GGA", "GGG" ]


dnaSeq = input("DNA 서열을 대문자로 입력하시오: ")
    lenSeq = len(dnaSeq)
    start = 0
    aminos = { "F":0, "L":0, "S":0, "Y":0, "C":0, "W":0, "P":0, "H":0, "Q":0, "R":0,
               "I":0, "M":0, "T":0, "N":0, "K":0, "V":0, "A":0, "D":0, "E":0, "G":0 }
    while (lenSeq >= 3):
        seqRead = dnaSeq[start:start+3]
        start = start + 3
        lenSeq = lenSeq - 3
        if seqRead in aminoF: aminos["F"] += 1
        elif seqRead in aminoL: aminos["L"] += 1
        elif seqRead in aminoS: aminos["S"] += 1
        elif seqRead in aminoY: aminos["Y"] += 1
        elif seqRead in aminoC: aminos["C"] += 1
        elif seqRead in aminoW: aminos["W"] += 1
        elif seqRead in aminoP: aminos["P"] += 1
        elif seqRead in aminoH: aminos["H"] += 1
        elif seqRead in aminoQ: aminos["Q"] += 1
        elif seqRead in aminoR: aminos["R"] += 1
        elif seqRead in aminoI: aminos["I"] += 1
        elif seqRead in aminoM: aminos["M"] += 1
        elif seqRead in aminoT: aminos["T"] += 1
        elif seqRead in aminoN: aminos["N"] += 1
        elif seqRead in aminoK: aminos["K"] += 1
        elif seqRead in aminoV: aminos["V"] += 1
        elif seqRead in aminoA: aminos["A"] += 1
        elif seqRead in aminoD: aminos["D"] += 1
        elif seqRead in aminoE: aminos["E"] += 1
        elif seqRead in aminoG: aminos["G"] += 1
    print("*"*5 + "{ \'아미노산\' : 빈도 }" + "*"*5)
    print(aminos)
    print("\n")

while True:
    dnaSeq = input("DNA 서열을 대문자로 입력하시오(종료는 0) ")
    if dnaSeq == "0":
        print("종료합니다.")
        break
    lenSeq = len(dnaSeq)
    start = 0
    aminos = { "F":0, "L":0, "S":0, "Y":0, "C":0, "W":0, "P":0, "H":0, "Q":0, "R":0,
           "I":0, "M":0, "T":0, "N":0, "K":0, "V":0, "A":0, "D":0, "E":0, "G":0 }
    while (lenSeq >= 3):
        seqRead = dnaSeq[start:start+3]
        start = start + 3
        lenSeq = lenSeq - 3
        if seqRead in aminoF: aminos["F"] += 1
        elif seqRead in aminoL: aminos["L"] += 1
        elif seqRead in aminoS: aminos["S"] += 1
        elif seqRead in aminoY: aminos["Y"] += 1
        elif seqRead in aminoC: aminos["C"] += 1
        elif seqRead in aminoW: aminos["W"] += 1
        elif seqRead in aminoP: aminos["P"] += 1
        elif seqRead in aminoH: aminos["H"] += 1
        elif seqRead in aminoQ: aminos["Q"] += 1
        elif seqRead in aminoR: aminos["R"] += 1
        elif seqRead in aminoI: aminos["I"] += 1
        elif seqRead in aminoM: aminos["M"] += 1
        elif seqRead in aminoT: aminos["T"] += 1
        elif seqRead in aminoN: aminos["N"] += 1
        elif seqRead in aminoK: aminos["K"] += 1
        elif seqRead in aminoV: aminos["V"] += 1
        elif seqRead in aminoA: aminos["A"] += 1
        elif seqRead in aminoD: aminos["D"] += 1
        elif seqRead in aminoE: aminos["E"] += 1
        elif seqRead in aminoG: aminos["G"] += 1
    print("*"*5 + "{ \'아미노산\' : 빈도 }" + "*"*5)
    print(aminos)
    print("\n")

print("")

