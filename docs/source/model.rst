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


Where :math:`\mu` is a scalar mean, :math:`\mathbf{1}` is a column vector of ones, with the same length as the number of tips, :math:`\sigma^2` is the Brownian motion rate parameter (i.e., the trait evolutionary rate), :math:`\mathbf{C}` is the phylogenetic covariance matrix.

:math:`\sigma^2` controls how quickly variance accumulates over evolutionary time. A larger :math:`\sigma^2` means traits are evolving faster and can differ more between species. We have the following **expected variance of trait divergence**:

.. math::

   \mathrm{Var}[X_i - X_j] \propto \sigma^2 \cdot \text{time since common ancestor}



:math:`\mathbf{C}` is an :math:`n \times n` matrix where n is the number of tips. It encodes the shared evolutionary history under a Brownian motion process. :math:`C_{ij}` is the total shared branch length from the root to the most recent common ancestor of species *i* and *j*. Diagonal elements :math:`C_{ii}` is the total path length from root to tip *i*. We have the **expected covariance** between trait values of species *i* and *j* as:

.. math::

   \mathrm{Cov}[X_i, X_j] = \sigma^2 C_{ij}


The likelihood function for observing the trait data under a constant-rate PBMM provided the :math:`\mu` and :math:`\sigma^2` parameters is known as follows:

.. math::

   \log L(\mu, \sigma^2) = -\frac{n}{2} \log(2\pi)
   - \frac{1}{2} \log|\sigma^2 \mathbf{C}|
   - \frac{1}{2} (\mathbf{X} - \mu \mathbf{1})^\top (\sigma^2 \mathbf{C})^{-1} (\mathbf{X} - \mu \mathbf{1})

Which simplifies to:

.. math::

   \log L(\mu, \sigma^2) = -\frac{n}{2} \log(2\pi)
   - \frac{n}{2} \log \sigma^2
   - \frac{1}{2} \log|\mathbf{C}|
   - \frac{1}{2\sigma^2} (\mathbf{X} - \mu \mathbf{1})^\top \mathbf{C}^{-1} (\mathbf{X} - \mu \mathbf{1})


The Maximum Likelihood Estimation (MLE) for :math:`\mu` and :math:`\sigma^2` is known as follows:

.. math::

   \hat{\mu} = \frac{\mathbf{1}^\top \mathbf{C}^{-1} \mathbf{X}}{\mathbf{1}^\top \mathbf{C}^{-1} \mathbf{1}}


This is the generalized least squares (GLS) estimate of the mean, accounting for phylogenetic correlation via :math:`\mathbf{C}`.

The MLE for :math:`\sigma^2` is:

.. math::

   \hat{\sigma}^2 = \frac{1}{n} (\mathbf{X} - \hat{\mu} \mathbf{1})^\top \mathbf{C}^{-1} (\mathbf{X} - \hat{\mu} \mathbf{1})


Accordingly, the exact maximum likelihood can also be calculated by simply putting :math:`\hat{\mu}` and :math:`\hat{\sigma}^2` back to the likelihood function.

We can further show that the trait values at internal nodes and tips follow a joint multivariate normal distribution:

.. math::

    \begin{bmatrix}
    \mathbf{X} \\
    \mathbf{Z}
    \end{bmatrix}
    \sim
    \mathcal{N} \left(
    \begin{bmatrix}
    \mu \mathbf{1} \\
    \mu \mathbf{1}
    \end{bmatrix},
    \sigma^2
    \begin{bmatrix}
    \mathbf{C}_{tt} & \mathbf{C}_{ti} \\
    \mathbf{C}_{it} & \mathbf{C}_{ii}
    \end{bmatrix}
    \right)


Provided the calculated MLE for :math:`\mu` and :math:`\sigma^2`, The conditional distribution of internal nodes is:

.. math::

    \mathbf{Z} \mid \mathbf{X} \sim \mathcal{N}\left(
    \mu \mathbf{1}_i + \mathbf{C}_{it} \mathbf{C}_{tt}^{-1} (\mathbf{X} - \mu \mathbf{1}_t),
    \ \sigma^2 \left( \mathbf{C}_{ii} - \mathbf{C}_{it} \mathbf{C}_{tt}^{-1} \mathbf{C}_{ti} \right)
    \right)


The MLE trait value at internal nodes is then the conditional mean:

.. math::

    \hat{\mathbf{Z}} = \mu \mathbf{1}_i + \mathbf{C}_{it} \mathbf{C}_{tt}^{-1} (\mathbf{X} - \mu \mathbf{1}_t)


Which is essentially the best linear unbiased predictor (BLUP) under the Brownian motion model that minimizes expected squared error (equivalent to a generalized least squares prediction of :math:`\mathbf{Z}` on :math:`\mathbf{X}`).


.. note::
        The MLE estimates of internal nodes are independent of :math:`\sigma^2` (since :math:`\sigma^2` scales the covariance but does not affect the optimal relative positioning of nodes). Thus, once :math:`\hat{\mu}` is known, the MLE of internal node values is fully determined by the tree structure and tip data. The MLEs are equivalent to the ``ancestral state reconstruction`` under PBMM.




