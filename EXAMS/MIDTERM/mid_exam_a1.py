# Midterm exam_a1

class BioSeq:
    def __init__(self, seq, seq_type = "DNA"):
        self.seq = seq.upper()
        self.seq_type = seq_type

    def __len__(self):
        return len(self.seq)
    
    def get_seq_biotype(self):
        return self.seq_type
    
    def show_info_seq(self):
        print("Sequence: ", self.seq, " biotype: ", self.seq_type)

    def count_occur(self, seq_search):
        return self.seq.count(seq_search)

