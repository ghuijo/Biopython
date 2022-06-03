# BioSeq class

class BioSeq():
    
    def __init__(self, seq):
        self.seq = seq
        self.biotype = "DNA"

    def len(self):
        return len(self.seq)
    
    def get_seq_biotype(self):
        return self.biotype
    
    def show_info_seq(self):
        print("Sequence: ", self.seq, " biotype: ", self.biotype)

    def count_occur(self, pat):
        lenSeq = len(self.seq)
        lenPat = len(pat)
        start = 0
        cnt = 0
        
        while (lenSeq >= lenPat):
            seqRead = self.seq[start:start+lenPat]
            if (seqRead == pat):
                start += lenPat
                lenSeq -= lenPat
                cnt += 1
            else:
                start += 1

        return cnt
