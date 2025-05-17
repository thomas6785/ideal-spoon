.. ideal-spoon documentation master file, created by
   sphinx-quickstart on Sat May 17 18:22:48 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ideal-spoon documentation
=========================

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. ifconfig:: developer_mode

   .. autoclass:: MyTestClass.MyTestClass
      :members:
      :private-members:
      :undoc-members:

.. ifconfig:: not developer_mode

   .. autoclass:: MyTestClass.MyTestClass
      :members:
      :undoc-members:
      :no-index:
