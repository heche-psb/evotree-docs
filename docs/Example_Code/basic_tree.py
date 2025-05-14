from evotree.basicdraw import plottree
TB,tree_object = plottree(tree="FigTree_newick")
TB.basicdraw()
TB.saveplot('Baisc_Tree.svg')
