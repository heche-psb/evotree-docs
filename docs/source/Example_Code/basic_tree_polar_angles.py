from evotree.basicdraw import plottree
import matplotlib.pyplot as plt
fig, axes = plt.subplots(2,3,figsize=(24, 16),subplot_kw={'projection': 'polar'})
angles = [60,120,180,270,330,355]
for angle,ax in zip(angles,axes.flatten()):
    TB,tree_object = plottree(tree="FigTree_newick",userfig=fig,userax=ax)
    TB.polardraw(polar=angle)
TB.saveplot('Baisc_Tree_Polar_Angles.svg')
