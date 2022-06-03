from Bio import Phylo

tree = Phylo.read('opunita_clustal_o.newick', 'newick')
print(tree)

Phylo.draw(tree)

