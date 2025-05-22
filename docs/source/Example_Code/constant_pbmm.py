from evotree.simulatepbmm import PBMMBuilder

PBMM = PBMMBuilder(tree='Fern.newick',trait='Fern_Data.tsv',traitcolname='Average DNA amount per chromosome (Mb)',traitname='Average chromosome size')
PBMM.ancestry_infer_constantpbmm()
TB = PBMM.drawalltrait_constant(topologylw=3,nodetextdecimal=2,traitdecimal=2)
TB.drawscale(plotfulllengthscale=True,fullscaletickheight=0.1,fullscaleticklabeloffset=0.1,addgeo=True,geoscaling=100,fullscalexticks=[int(i*100) for i in range(5)])
TB.saveplot("Ancestral_Trait_Reconstruction.svg")
