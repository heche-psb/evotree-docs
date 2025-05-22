Model
=====

.. _modelpbmm:

PBMM
----

The **Phylogenetic Brownian Motion Model (PBMM)** describes how continuous traits (for instance genome size) evolve along a phylogenetic tree under the assumption that changes accumulate randomly and gradually over time, resembling particles undergoing Brownian motion.

There are a few key assumptions:

**1) Trait Evolution as a Random Walk**

Trait values change continuously through time following a Brownian motion process.

**2) Phylogenetic Signal**

More closely related species are supposed to share more similar traits because they share a longer common evolutionary history. The expected trait covariance between species is proportional to the shared branch length in the tree.

**3) Neutral Evolution**

Changes in the trait are unbiased/neutral — there's no directional trend or selection (but see Ornstein-Uhlenbeck model).


The trait values at the tips of the tree follow a **multivariate normal distribution**:

.. math::

   X \sim \mathcal{N}(\mu \mathbf{1}, \sigma^2 \mathbf{C})


Where :math:`\mu` is a scalar mean, :math:`\mathbf{1}` is a column vector of ones, with the same length as the number of tips or observations, :math:`\sigma^2` is the Brownian motion rate parameter (i.e., the trait evolutionary rate), :math:`\mathbf{C}` is the phylogenetic covariance matrix.

:math:`\sigma^2` controls how quickly variance accumulates over evolutionary time. A larger :math:`\sigma^2` means traits are evolving faster and can differ more between species. We have the following **expected variance of trait divergence**:

.. math::

   \mathrm{Var}[X_i - X_j] \propto \sigma^2 \cdot \text{time since common ancestor}



:math:`\mathbf{C}` is an :math:`n \times n` matrix where n is the number of tips. It encodes the shared evolutionary history under a Brownian motion process. :math:`C_{ij}` is the total shared branch length from the root to the most recent common ancestor of species *i* and *j*. Diagonal elements :math:`C_{ii} =` total path length from root to tip *i*. We have the **expected covariance** between trait values of species *i* and *j* as:

.. math::

   \mathrm{Cov}[X_i, X_j] = \sigma^2 C_{ij}



