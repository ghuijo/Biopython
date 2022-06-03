from re import search

def  find_zync_finger(seq):
     regexp = "C.H.[LIVMFY]C.{2}C[LIVMYA]"   # 정규 표현식으로 바꾸어줌
     mo = search(regexp, seq)
     if( mo != None):
       return mo.span()[0]
     else:
        return -1

def test():
     seq = "HKMMLASCKHLLCLKCIVKLG"
     print(find_zync_finger(seq))

test()

