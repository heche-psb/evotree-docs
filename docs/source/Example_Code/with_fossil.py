from evotree.basicdraw import plottree
TB,tree_object = plottree(tree="FigTree_newick")
TB.plotnodeuncertainty = True
# Plot the node uncertainty (usually 95%HPD time uncertainty)
#
#
TB.nulw = 3
TB.nuccolor = 'gray'
# Set the linewidth of the node uncertainty band and color
#
#
TB.basicdraw()
#
#
fossilnodes=[('Prasinoderma_coloniale','Amborella_trichopoda'),('Ostreococcus_lucimarinus','Pedinomonas_minor'),('Pedinomonas_minor','Mesostigma_viride'),('Botryococcus_braunii','Volvox_carteri'),('Botryococcus_braunii','Coccomyxa_subellipsoidea'),('Spirogloea_muscicola','Amborella_trichopoda'),('Anthoceros_angustus','Amborella_trichopoda'),('Takakia_lepidozioides','Marchantia_polymorpha'),('Selaginella_moellendorffii','Amborella_trichopoda'),('Adiantum_capillus-veneris','Amborella_trichopoda'),('Cycas_panzhihuaensis','Amborella_trichopoda'),('Aristolochia_fimbriata','Amborella_trichopoda')]
TB.highlightnode(nodes=fossilnodes,colors=['orange' for i in fossilnodes],nodesizes=[8 for i in fossilnodes],addlegend=True,legendlabel="Fossil calibrations")
# Highlight certain nodes, set color, size, legend and legendlabel
#
#
TB.saveplot('With_Fossil.svg')
