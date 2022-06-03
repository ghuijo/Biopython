from Bio.Align.Applications import MuscleCommandline

muscle_exe = "yourPythonPath\\muscle3.8.31_i86win32.exe"
cmd_line = MuscleCommandline(muscle_exe, input="HBA_3.fasta", out="HBA.aln", clw=" ")
print(cmd_line)
stdout, stderr = cmd_line()

