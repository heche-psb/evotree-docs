from evotree.basicdraw import plottree
from matplotlib.pyplot import cm
import numpy as np
from Bio import Phylo
Tree = Phylo.read("Example_243.tree",'newick')
# Modify the tip name (only for this example)
for tip in Tree.get_terminals():
    if tip.name.endswith(".cds"):
        tip.name = tip.name[:-4]
TB,tree_object = plottree(treeobject=Tree)
TB.fs =(24,24)
TB.polardraw()
# Highlight certain clades, set color, alpha, saturation, line width, legend and legendlabel
#
#
colors = cm.viridis(np.linspace(0, 1, 7))
TB.highlightcladeringpolar(clades=[('Amborella-trichopoda','Malus-doumeri'),('Gnetum-montanum','Taxus-wallichiana'),('Dipteris-shenzhenensis','Azolla-filiculoides'),('Huperzia-asiatica','Selaginella-moellendorffii'),('Leiosporoceros-dussii','Phaeoceros-laevis_902'),('Haplomitrium-mnioides','Herbertus-kurzii'),('Takakia-lepidozioides','Brachythecium-laetum')],ringcolors=colors,ringalphas=[0.5]*7,ringroffset=[0.5]*7,ringlws=[10]*7,ringsaturations=[0.8]*7,labels=['Angiosperm','Gymnosperm','Fern','Lycophyte','Hornwort','Liverwort','Moss'])
TB.showlegend(frameon=False,fontsize=35)
TB.saveplot('Polar_Nonultra_Ring.svg')
