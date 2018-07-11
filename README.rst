PowERP client library
=====================

This is a wrapper for an `ERPPeek <http://erppeek.readthedocs.io/en/latest/>`_, but with some
features for our ERP.

- Initialitzacion with url schema
- XML-RPC Transactions with the `ws_transactions module <https://github.com/gisce/ws_transactions>`_
  (original library was `erppeek_wst <https://github.com/gisce/erppeek_wst>`_)
- (TODO) `MsgPack <https://msgpack.org>`_ support

.. code-block:: python

  from ooclient import Client
  
  c = Client('http://admin:password@localhost:8069/database')
