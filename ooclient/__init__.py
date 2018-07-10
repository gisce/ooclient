from urlparse import urlparse
from erppeek import Client as PeekClient, Service
import functools
from six.moves import xmlrpc_client as xmlrpclib


def parse_client_url(url, db=None, user=None, password=None,
                 transport=None, verbose=False):
    url = urlparse(url)
    server = '{p.scheme}://{p.hostname}:{p.port}'.format(p=url)
    values = {
        'server': server,
        'db': db,
        'user': user,
        'password': password,
        'transport': transport,
        'verbose': verbose
    }
    if url.username:
        values['user'] = url.username
    if url.password:
        values['password'] = url.password
    if url.path.lstrip('/'):
        values['db'] = url.path.lstrip('/')
    return values


class Client(PeekClient):
    def __init__(self, url, *args, **kwargs):
        params = parse_client_url(url, *args, **kwargs)
        super(Client, self).__init__(**params)


class ClientWST(Client):

    def __init__(self, server, db=None, user=None, password=None,
                 verbose=False):
        self.transaction_id = None
        methods = ['execute', 'get_transaction',
                   'commit', 'rollback', 'close', 'begin', 'close_connection']
        self._sync = Service(server, 'ws_transaction', methods, verbose=verbose)
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
        self._execute_bare = self._execute
        self._execute_sync = authenticated(self._sync.execute)
        self._commit = authenticated(self._sync.commit)
        self._rollback = authenticated(self._sync.rollback)
        self._begin = authenticated(self._sync.begin)
        self._close_connection = authenticated(self._sync.close_connection)

    _login = login
    _login.cache = {}

    def begin(self):
        tid = self._begin()
        self.transaction_id = tid
        self._execute = functools.partial(self._execute_sync, tid)
        return self

    def get_transaction(self, transaction_id):
        self.transaction_id = self._get_transaction(transaction_id)
        # Reloading modules for transaction
        self._execute = functools.partial(self._execute_sync,
                                          self.transaction_id)
        return self.transaction_id

    def commit(self):
        self._commit(self.transaction_id)

    def rollback(self):
        try:
            self._rollback(self.transaction_id)
        except xmlrpclib.Fault as e:
            if 'commands ignored until end of transaction block' not in str(e):
                raise

    def close(self):
        self._close_connection(self.transaction_id)

