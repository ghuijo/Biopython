from Bio import Phylo

tree = Phylo.read('Interleukin-2.newick', 'newick')
print(tree)

Phylo.draw(tree)

