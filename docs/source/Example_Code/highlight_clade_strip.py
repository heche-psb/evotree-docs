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
TB.highlightclade_strip(clades=[('Amborella_trichopoda','Anthoceros_angustus'),('Zygnema_circumcarinatum_SAG_698-1b','Mesostigma_viride'),('Volvox_carteri','Pedinomonas_minor'),('Micromonas_pusilla','Ostreococcus_lucimarinus')],stripcolors=['red','green','gray','black'],stripalphas=[0.6,0.3,0.3,0.3],striplws=[5]*4,stripxoffset=[6,8.7,6,6],striplabelrt=['vertical']*4,stripyoffset=[0.02]*4,striplabels=['Embryophyta','Streptophyta','Chlorophytina','Prasinophytina'],striplabelboxcolors=['none']*4,striplabelcolors=['black']*4,striplabelxoffset=[0.4]*4,striplabelsweight=['bold']*4)
TB.highlightclade(clades=[('Amborella_trichopoda','Anthoceros_angustus'),('Zygnema_circumcarinatum_SAG_698-1b','Mesostigma_viride'),('Volvox_carteri','Pedinomonas_minor'),('Micromonas_pusilla','Ostreococcus_lucimarinus')],facecolors=['red','green','gray','black'],gradual=True,alphas=[0.6,0.3,0.3,0.3],rightoffset=0.01,topoffset=0.02,bottomoffset=-0.01,labels=['Embryophyta','Streptophyta','Chlorophytina','Prasinophytina'],labelboxcolors=['black','black','black','black'],labelcolors=['white','white','white','white'])
# Highlight the MRCA clades, set strip or shadow color, transparency, gradual style, xoffset and yoffset, label texts, labelxoffset and labelyoffset, colors and text box colors
#
#
TB.saveplot('Highlight_Clade_Strip.svg')
