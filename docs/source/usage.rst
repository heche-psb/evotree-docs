Usage
=====

.. _plottree:

Plottree
------------

Let's draw a simple phylogenetic tree using the command below:

>>> from evotree.basicdraw import plottree
>>> TB,tree_object = plottree(tree="FigTree_newick")
>>> TB.basicdraw()
>>> TB.saveplot('Baisc_Tree.svg')

.. image:: Example_Data/wgd_dmd.svg


Users can also write the above code into a ``*.py`` file and plot the tree using the command below:
.. code-block:: console

      (ENV)$ python Example_Code/basic_tree.py


.. note::

       All the codes and output figures can be found in :doc:`Example_Code` and :doc:`Example_Data`.


