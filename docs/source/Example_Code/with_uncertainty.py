from evotree.basicdraw import plottree
TB,tree_object = plottree(tree="FigTree_newick")
TB.plotnodeuncertainty = True
# Plot the node uncertainty (usually 95%HPD time uncertainty)
TB.nulw = 3
TB.nuccolor = 'gray'
# Set the linewidth of the node uncertainty band and color
TB.basicdraw()
TB.saveplot('With_Uncertainty.svg')
