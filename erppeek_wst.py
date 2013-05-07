#!/usr/bin/env python
# -*- coding: utf-8 -*-

from erppeek import Client, Service
import functools


class ClientWST(Client):

    def __init__(self, server, db=None, user=None, password=None,
                 verbose=False):
        self.transaction_id = None
        methods = ['execute', 'get_transaction',
                   'commit', 'rollback', 'close']
        self._sync = Service(server, 'sync', methods, verbose=verbose)
        super(ClientWST,
              self).__init__(server, db=db, user=user,
                             password=password, verbose=verbose)

    def login(self, user, password=None, database=None):
        super(ClientWST,
              self).login(user, password=password, database=database)

        args = self._execute.args

        def authenticated(method):
            return functools.partial(method, args[0], args[1], args[2])
        self._get_transaction = authenticated(self._sync.get_transaction)
        self._execute_sync = authenticated(self._sync.execute)
        self._commit = authenticated(self._sync.commit)
        self._rollback = authenticated(self._sync.rollback)
        self._close = authenticated(self._sync.close)

    _login = login
    _login.cache = {}

    def get_transaction(self, transaction_id):
        self.transaction_id = self._get_transaction(transaction_id)
        # Reloading modules for transaction
        self._execute = functools.partial(self._execute_sync,
                                          self.transaction_id)
        return self.transaction_id

    def commit(self):
        self._commit(self.transaction_id)

    def rollback(self):
        self._rollback(self.transaction_id)

    def close(self):
        self._close(self.transaction_id)
