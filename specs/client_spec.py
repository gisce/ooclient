from mamba import *
from expects import *

with description('Pasing a client url'):
    with it('should return all the parameters'):
        from ooclient import parse_client_url
        params = parse_client_url('http://admin:password@localhost:8069/test')
        expect(params).to(have_keys(
            server='http://localhost:8069',
            user='admin',
            password='password',
            db='test'
        ))
    with it('should be compatible with old parameters constructor'):
        from ooclient import parse_client_url
        params = parse_client_url('http://localhost:8069', 'test', 'admin', 'password')
        expect(params).to(have_keys(
            server='http://localhost:8069',
            user='admin',
            password='password',
            db='test'
        ))
