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
# Highlight certain nodes, set color, alpha, saturation, size, legend and legendlabel, as well as convex hull parameters
#
#
colors = cm.viridis(np.linspace(0, 1, 7))
TB.highlightcladepolar(clades=[('Amborella-trichopoda','Malus-doumeri'),('Gnetum-montanum','Taxus-wallichiana'),('Dipteris-shenzhenensis','Azolla-filiculoides'),('Huperzia-asiatica','Selaginella-moellendorffii'),('Leiosporoceros-dussii','Phaeoceros-laevis_902'),('Haplomitrium-mnioides','Herbertus-kurzii'),('Takakia-lepidozioides','Brachythecium-laetum')],facecolors=colors,alphas=[0.5]*7,rightoffset=0,topoffset=0,bottomoffset=0,labels=['Angiosperm','Gymnosperm','Fern','Lycophyte','Hornwort','Liverwort','Moss'],labelboxcolors=['black']*7,labelcolors=['white']*7,gradual=False,convexhull=True,saturations=[0.8]*7,convexsmoothness=1000,convexalpha=None)
TB.showlegend(frameon=False,fontsize=35)
TB.saveplot('Polar_Nonultra.svg')
