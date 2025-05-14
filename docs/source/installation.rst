Installation
=====

.. _pypi:

PyPI
------------

The evotree library is published on Python Package Index (PyPI), users can install it using pip. We suggest that the installation is better performed under a virtual environment:

.. code-block:: console

          $ virtualenv -p=python3 ENV (or python3/python -m venv ENV)
          $ source ENV/bin/activate
          (ENV)$ pip install evotree



.. _source:

Source
----------------

For users who would like to use the actively-updating development version, installation from the source can be achieved as follow:

.. code-block:: console

      $ git clone https://github.com/heche-psb/evotree
      $ cd evotree
      $ virtualenv -p=python3 ENV (or python3 -m venv ENV)
      $ source ENV/bin/activate
      (ENV)$ pip install -r requirements.txt
      (ENV)$ pip install . (or pip install -e .)



