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

       All the example codes can be found in https://github.com/heche-psb/evotree-docs/tree/main/docs/Example_Code


Now, let's add uncertainty bands to each internal nodes using the command below:

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


