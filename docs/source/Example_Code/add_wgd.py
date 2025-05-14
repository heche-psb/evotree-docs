from evotree.basicdraw import plottree
TB,tree_object = plottree(tree="FigTree_newick")
TB.plotnodeuncertainty = True
# Plot the node uncertainty (usually 95%HPD time uncertainty)
TB.nulw = 3
TB.nuccolor = 'gray'
# Set the linewidth of the node uncertainty band and color
TB.basicdraw()
#
#
fossilnodes=[('Prasinoderma_coloniale','Amborella_trichopoda'),('Ostreococcus_lucimarinus','Pedinomonas_minor'),('Pedinomonas_minor','Mesostigma_viride'),('Botryococcus_braunii','Volvox_carteri'),('Botryococcus_braunii','Coccomyxa_subellipsoidea'),('Spirogloea_muscicola','Amborella_trichopoda'),('Anthoceros_angustus','Amborella_trichopoda'),('Takakia_lepidozioides','Marchantia_polymorpha'),('Selaginella_moellendorffii','Amborella_trichopoda'),('Adiantum_capillus-veneris','Amborella_trichopoda'),('Cycas_panzhihuaensis','Amborella_trichopoda'),('Aristolochia_fimbriata','Amborella_trichopoda')]
TB.highlightnode(nodes=fossilnodes,colors=['orange' for i in fossilnodes],nodesizes=[8 for i in fossilnodes],addlegend=True,legendlabel="Fossil calibrations")
# Highlight certain nodes, set color, size, legend and legendlabel
#
#
TB.highlightclade(clades=[('Amborella_trichopoda','Anthoceros_angustus'),('Zygnema_circumcarinatum_SAG_698-1b','Mesostigma_viride')],facecolors=['red','green'],gradual=True,alphas=[0.6,0.3],rightoffset=0.01,topoffset=0.02,bottomoffset=-0.01,labels=['Embryophyta','Streptophyta'],labelboxcolors=['black','black'],labelcolors=['white','white'])
TB.highlightclade(clades=[('Volvox_carteri','Pedinomonas_minor'),('Micromonas_pusilla','Ostreococcus_lucimarinus')],facecolors=['gray','black'],gradual=True,alphas=[0.3,0.3],rightoffset=0.01,topoffset=0.02,bottomoffset=-0.01,labels=['Chlorophytina','Prasinophytina'],labelboxcolors=['black','black'],labelcolors=['white','white'])
# Highlight the MRCA clades, set shadow color, transparency, gradual style, xoffset and yoffset, label texts, labelxoffset and labelyoffset, colors and text box colors
#
#
TB.drawscale(plotfulllengthscale=True,fullscaletickheight=0.1,fullscaleticklabeloffset=0.1,addgeo=True,geoscaling=100,fullscalexticks=[int(i*100) for i in range(14)])
# Add time-scale at the bottom, set geoscaling (here the branch length is at the unit of 100 million years so we set as 100), preset xticks (by default six evenly-spaced xticks) as [0,100,200,..,1300], yoffset for tick and ticklabel
#
#
TB.drawwgd(wgd="Spi_WGD.tsv",addlegend=True,legendlabel="Newly dated ancient polyploidy event",lw=8,al=0.8)
# With external data on WGD date (example as Spirogloea muscicola), plot WGD dates in the corresponding time and phylogenetic location
#
#
TB.showlegend(frameon=False,bbox_to_anchor=(0.60, 0.95))
TB.saveplot('Add_WGD.svg')
