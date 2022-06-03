from re import search

def validate_dna_re(seq):
    if search("[^ACTGactg]", seq) != None:
       return False
    else:
       return True
    
print(validate_dna_re("aTcgtttactgtgc"))
print(validate_dna_re("aTcgtttacYa"))

