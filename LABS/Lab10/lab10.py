# BioPython
# L10. SeqIO Module II


# 1. 파일의 속성 변경
# fasta format이므로 number of features는 0

from Bio import SeqIO
record_iterator = SeqIO.parse("ls_orchid.fasta", "fasta")
first_record = next(record_iterator)
print(first_record, "\n")
first_record.id = "new_id"
first_record.id = first_record.id + " " + "desired new description"
print(first_record.format("fasta")[:200], "\n")


# 2. 파일 handle을 사용하여 읽기

from Bio import SeqIO
print(sum(len(r) for r in SeqIO.parse("ls_orchid.gbk", "gb")))

from Bio import SeqIO
handle = open("ls_orchid.gbk")
print(sum(len(r) for r in SeqIO.parse(handle, "gb")))
handle.close()

from Bio import SeqIO
with open("ls_orchid.gbk") as handle:   # close() 필요X
    print(sum(len(r) for r in SeqIO.parse(handle, "gb")))
print("")


# 3. Entrez 모듈을 이용해 인터넷에서 파일 읽기

from Bio import Entrez, SeqIO
Entrez.email = "yourid@example.com"
with Entrez.efetch(
    db = "nucleotide", rettype = "gb", retmode = "text",
    id = "6273291, 6273290, 6273289") as handle:
    for seq_record in SeqIO.parse(handle, "gb"):
        print("%s %s..." % (seq_record.id, seq_record.description[:50]))
        print("Sequence length %i, %i features, from: %s"
              % (len(seq_record), len(seq_record.features),
                 seq_record.annotations["source"]))
print("")

# Genbank라서 feature 존재
from Bio import Entrez, SeqIO
Entrez.email = "yourid@example.com"
with Entrez.efetch(
    db = "nucleotide", rettype = "gb", retmode = "text", id = "6273291"
    ) as handle:
    seq_record = SeqIO.read(handle, "gb")
    print("%s with %i features" % (seq_record.id, len(seq_record.features)))
print("")

from Bio import Entrez, SeqIO
Entrez.email = "youtid@example.com"
handle = Entrez.efetch(db = "nucleotide", rettype = "gb",
                       retmode = "text", id = "AY463215")
for s in handle:
    print(s.strip())
handle.close()
print("")

# fasta 포맷의 경우
from Bio import Entrez, SeqIO
Entrez.email = "yourid@example.com"
with Entrez.efetch(
    db = "nucleotide", rettype = "fasta", retmode = "text", id = "42540826"
    ) as handle:
    seq_record = SeqIO.read(handle, "fasta")
    print("%s with %i features" % (seq_record, len(seq_record)))
print("")

from Bio import Entrez, SeqIO
Entrez.email = "yourid@example.com"
handle = Entrez.efetch(db = "nucleotide", rettype = "fasta",
                       retmode = "text", id = "AY463215")
for s in handle:
    print(s.strip())
handle.close()
print("")


# 4. FASTQ 파일 포맷 읽기

from Bio.SeqIO.QualityIO import FastqGeneralIterator
count = total_len = 0
with open("SRR020192.fastq") as in_handle:
    for title, seq, qual in FastqGeneralIterator(in_handle):
        count += 1
        total_len += len(seq)
print("%i records with total sequence length %i" % (count, total_len), "\n")

from Bio import SeqIO
seq_record = SeqIO.parse("SRR020192_edited.fastq", "fastq")
print(type(seq_record))
for s in seq_record:
    print(type(s))
    print(s)
    print("")


# 5. Sequence 파일 쓰기

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

rec1 = SeqRecord(Seq(
    "MMYQQGCFAG GTVLRLAKDL AENNRGARVL VVCSEITAVT FRGPSETHLD SMVGQALFGD"
    "GAGAVIVGSD PDLSVERPLY ELVWTGATLL PDSEGAIDGH LREVGLTFHL LKDVPGLISK"
    "NIEKSLKEAF TPLGISDWNS TFWIAHPGGP AILDQVEAKL GLKEEKMRAT REVLSEYGNM"
    "SSAC",),
                 id = "gi|14150838|gb|AAK54648.|AF376133_1",
                 description = "chalcone synthase [Cucumis sativus]",)

rec2 = SeqRecord(Seq(
    "YPDYYFRITN REHKAELKEK FQRMCDKSMI KKRYMYLTEE ILKENPSMCE YMAPSLDARQ"
    "DMVVVEIPKL GKEAAVKAIK EWGQ",),
                 id = "gi|13919613|gb|AAK33142.1|",
                 description = "chalcone synthase [Fragaria vesca subsp. bracteata]",)

rec3 = SeqRecord(Seq(
    "MVTVEEFRRA QCAEGPATVM AIGTATPSNC VDQSTYPDYY FRITNSEHKV ELKEKFKRMC"
    "EKSMIKKRYM HLTEEILKEN PNICAYMAPS LDARQDIVVV EVPKLGKEAA QKAIKEWGQP"
    "KSKITHLVFC TTSGVDMPGC DYQLTKLLGL RPSVKRFMMY QQGCFAGGTV LRMAKDLAEN"
    "NKGARVLVVC SEITAVTFRG PNDTHLDSLV GQALFGDGAA AVIIGSDPIP EVERPLFELV"
    "SAAQTLLPDS EGAIDGHLRE VGLTFHLLKD VPGLISKNIE KSLVEAFQPL GISDWNSLFW"
    "IAHPGGPAIL DQVELKLGLK QEKLKATRKV LSNYGNMSSA CVLFILDEMR KASAKEGLGT"
    "TGEGLEWGVL FGFGPGLTVE TVVLHSVAT",),
                 id = "gi|13925890|gb|AAK49457.1",
                 description = "chalcone synthase [Nicotiana tabacum]",)
my_records = [rec1, rec2, rec3]
SeqIO.write(my_records, "my_example.fasta", "fasta")
