from Bio import Phylo

tree = Phylo.read('PF05371.newick', 'newick')
print(tree)

Phylo.draw(tree)

