from evotree.basicdraw import plottree
TB,tree_object = plottree(tree="FigTree_newick")
TB.plotnodeuncertainty = True
TB.nulw = 3
TB.nuccolor = 'gray'
TB.polardraw()
fossilnodes=[('Prasinoderma_coloniale','Amborella_trichopoda'),('Ostreococcus_lucimarinus','Pedinomonas_minor'),('Pedinomonas_minor','Mesostigma_viride'),('Botryococcus_braunii','Volvox_carteri'),('Botryococcus_braunii','Coccomyxa_subellipsoidea'),('Spirogloea_muscicola','Amborella_trichopoda'),('Anthoceros_angustus','Amborella_trichopoda'),('Takakia_lepidozioides','Marchantia_polymorpha'),('Selaginella_moellendorffii','Amborella_trichopoda'),('Adiantum_capillus-veneris','Amborella_trichopoda'),('Cycas_panzhihuaensis','Amborella_trichopoda'),('Aristolochia_fimbriata','Amborella_trichopoda')]
TB.highlightnodepolar(nodes=fossilnodes,colors=['orange' for i in fossilnodes],nodesizes=[8 for i in fossilnodes],addlegend=True,legendlabel="Fossil calibrations")
TB.highlightcladepolar(clades=[('Amborella_trichopoda','Anthoceros_angustus'),('Zygnema_circumcarinatum_SAG_698-1b','Mesostigma_viride')],facecolors=['red','green'],gradual=False,alphas=[0.6,0.3],rightoffset=0,topoffset=0,bottomoffset=0,labels=['Embryophyta','Streptophyta'],labelboxcolors=['black','black'],labelcolors=['white','white'],saturations=[0.8]*2,labelpositions=['bottom','bottom'])
TB.highlightcladepolar(clades=[('Volvox_carteri','Pedinomonas_minor'),('Micromonas_pusilla','Ostreococcus_lucimarinus')],facecolors=['gray','black'],gradual=False,alphas=[0.3,0.3],rightoffset=0,topoffset=0,bottomoffset=0,labels=['Chlorophytina','Prasinophytina'],labelboxcolors=['black','black'],labelcolors=['white','white'],saturations=[0.8]*2,labelpositions=['bottom','bottom'])
TB.drawscalepolar(plotfulllengthscale=True,geoscaling=100,fullscalexticks=[int(i*100) for i in range(14)],addfulltickring=True,fulltickscaler=2.5,fullscaletickringcolors=["gray","black"]*7,fullscaletickringalphas=[0.1]*14,addfulltickline=True,fullscalels='--',fullscalealpha=0.5,fullscalecolor='gray')
TB.saveplot('Baisc_Tree_Polar_Add_TimeScale_Simplering_Arc.svg')
