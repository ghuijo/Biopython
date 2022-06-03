from Bio import AlignIO
from Bio.Seq import Seq

alignment = AlignIO.read("PF05371_seed.sth", "stockholm")

instance = []

for record in alignment:
    s = Seq(str(record.seq))
    instance.append(s)
    print(instance)

