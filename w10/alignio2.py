from Bio import AlignIO
alignment = AlignIO.read("PF05371__seed.faa", "fasta")
print(alignment) 
