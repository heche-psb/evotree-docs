Usage
=====

.. _plottree:

Plottree
--------

Let's draw a simple phylogenetic tree using the command below:

>>> from evotree.basicdraw import plottree
>>> TB,tree_object = plottree(tree="FigTree_newick")
>>> TB.basicdraw()
>>> TB.saveplot('Baisc_Tree.svg')

.. image:: Example_Data/Baisc_Tree.svg


Users can also write the above code into a ``*.py`` file and plot the tree using the command below:

.. code-block:: console

      (ENV)$ python Example_Code/basic_tree.py


.. note::

       All the example codes can be found in `Example_Code <https://github.com/heche-psb/evotree-docs/tree/main/docs/source/Example_Code>`_ and the example data in `Example_Data <https://github.com/heche-psb/evotree-docs/tree/main/docs/source/Example_Data>`_.


Now, let's add **uncertainty bands** to each internal nodes using the command below:

>>> from evotree.basicdraw import plottree
>>> TB,tree_object = plottree(tree="FigTree_newick")
>>> TB.plotnodeuncertainty = True
>>> TB.nulw = 3
>>> TB.nuccolor = 'gray'
>>> TB.basicdraw()
>>> TB.saveplot('With_Uncertainty.svg')

Or using the command below:

.. code-block:: console

      (ENV)$ python Example_Code/with_uncertainty.py


.. image:: Example_Data/With_Uncertainty.svg


We can also add the **fossil calibrations** that we used using the command below:

>>> from evotree.basicdraw import plottree
>>> TB,tree_object = plottree(tree="FigTree_newick")
>>> TB.plotnodeuncertainty = True
>>> TB.nulw = 3
>>> TB.nuccolor = 'gray'
>>> TB.basicdraw()
>>> fossilnodes=[('Prasinoderma_coloniale','Amborella_trichopoda'),('Ostreococcus_lucimarinus','Pedinomonas_minor'),('Pedinomonas_minor','Mesostigma_viride'),('Botryococcus_braunii','Volvox_carteri'),('Botryococcus_braunii','Coccomyxa_subellipsoidea'),('Spirogloea_muscicola','Amborella_trichopoda'),('Anthoceros_angustus','Amborella_trichopoda'),('Takakia_lepidozioides','Marchantia_polymorpha'),('Selaginella_moellendorffii','Amborella_trichopoda'),('Adiantum_capillus-veneris','Amborella_trichopoda'),('Cycas_panzhihuaensis','Amborella_trichopoda'),('Aristolochia_fimbriata','Amborella_trichopoda')]
>>> TB.highlightnode(nodes=fossilnodes,colors=['orange' for i in fossilnodes],nodesizes=[8 for i in fossilnodes],addlegend=True,legendlabel="Fossil calibrations")
>>> TB.saveplot('With_Fossil.svg')

Or using the command below:

.. code-block:: console

      (ENV)$ python Example_Code/with_fossil.py


.. image:: Example_Data/With_Fossil.svg


We can further highlight specific clades using the command below:

>>> from evotree.basicdraw import plottree
>>> TB,tree_object = plottree(tree="FigTree_newick")
>>> TB.plotnodeuncertainty = True
>>> TB.nulw = 3
>>> TB.nuccolor = 'gray'
>>> TB.basicdraw()
>>> fossilnodes=[('Prasinoderma_coloniale','Amborella_trichopoda'),('Ostreococcus_lucimarinus','Pedinomonas_minor'),('Pedinomonas_minor','Mesostigma_viride'),('Botryococcus_braunii','Volvox_carteri'),('Botryococcus_braunii','Coccomyxa_subellipsoidea'),('Spirogloea_muscicola','Amborella_trichopoda'),('Anthoceros_angustus','Amborella_trichopoda'),('Takakia_lepidozioides','Marchantia_polymorpha'),('Selaginella_moellendorffii','Amborella_trichopoda'),('Adiantum_capillus-veneris','Amborella_trichopoda'),('Cycas_panzhihuaensis','Amborella_trichopoda'),('Aristolochia_fimbriata','Amborella_trichopoda')]
>>> TB.highlightnode(nodes=fossilnodes,colors=['orange' for i in fossilnodes],nodesizes=[8 for i in fossilnodes],addlegend=True,legendlabel="Fossil calibrations")
>>> TB.highlightclade(clades=[('Amborella_trichopoda','Anthoceros_angustus'),('Zygnema_circumcarinatum_SAG_698-1b','Mesostigma_viride')],facecolors=['red','green'],gradual=True,alphas=[0.6,0.3],rightoffset=0.01,topoffset=0.02,bottomoffset=-0.01,labels=['Embryophyta','Streptophyta'],labelboxcolors=['black','black'],labelcolors=['white','white'])
>>> TB.highlightclade(clades=[('Volvox_carteri','Pedinomonas_minor'),('Micromonas_pusilla','Ostreococcus_lucimarinus')],facecolors=['gray','black'],gradual=True,alphas=[0.3,0.3],rightoffset=0.01,topoffset=0.02,bottomoffset=-0.01,labels=['Chlorophytina','Prasinophytina'],labelboxcolors=['black','black'],labelcolors=['white','white'])
>>> TB.saveplot('Highlight_Clade.svg')

Or using the command below:

.. code-block:: console

      (ENV)$ python Example_Code/highlight_clade.py


.. image:: Example_Data/Highlight_Clade.svg



