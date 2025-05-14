from evotree.basicdraw import plottree
from matplotlib.pyplot import cm
import numpy as np
TB,tree_object = plottree(tree="FigTree_newick")
TB.plotnodeuncertainty = True
TB.fs =(16,13)
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
inixoffset = 0.60
colors = cm.viridis(np.linspace(0, 1, 7))
colormap = {i:colors[i] for i in range(7)}
Map_Habitat = {0:"Terrestrial",1:"Subaerial",2:"Freshwater",3:"Marine",4:"Terrestrial/Subaerial",5:"Subaerial/Freshwater",6:"Hypersaline"}
TB.drawcircles(traittype="Habitat.tsv",xoffset=inixoffset,usetypedata=["Habitat"],traitobjectname="Habitat",scalingx=0.1,maxcirclesize=24,colormap=colormap,legendmap=Map_Habitat)
# Add the categorical information from external data
#
#
stepxoffset = 0.15
cols = ["WGD-pairs-percentage","TD-pairs-percentage","PD-pairs-percentage","TRD-pairs-percentage","DSD-pairs-percentage"]
for ind,col in enumerate(cols):
    quantitylegendflag = True if ind == 0 else False
    TB.drawcircles(traitquantity='dupfinder.info.percentage.tsv',usequantitydata=[col],xoffset=inixoffset+stepxoffset*(ind+1),traitobjectname="{}".format(col.replace("-percentage","")),scalingx=0.2,maxcirclesize=24,quantitylegend=quantitylegendflag,maxvaluescaler=1,decimal=2)
# Add the gene duplication information from external data
#
#
handles, labels = TB.ax.get_legend_handles_labels()
order_dic = {'Terrestrial':1,'Terrestrial/Subaerial':2,'Subaerial':3,'Subaerial/Freshwater':4,'Freshwater':5,'Marine':6,'Hypersaline':7}
labels, handles = zip(*sorted(zip(labels, handles), key=lambda x: order_dic.get(x[0],0)))
TB.showlegend(handles,labels,frameon=False,bbox_to_anchor=(0.25, 0.45),labelspacing=2.3)
# Show all legends that were set before, set the desired order and other parameters
#
#
TB.saveplot('Add_GD.svg')
