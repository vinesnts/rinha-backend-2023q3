import falcon
import jwt

from falcon.http_status import HTTPStatus

from core.utils.utils import logstd
from core.settings import JWT_SECRET


DEFAULT_TOKEN_OPTS = {"name": "big-dash-integracao-user", "location":"header"}

class AuthMiddleware(object):

    def __init__(self):
        self.secret = JWT_SECRET

    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', '*')
        resp.set_header('Access-Control-Allow-Headers', '*')
        resp.set_header('Access-Control-Max-Age', 1728000)  # 20 days
        if req.method == 'OPTIONS':
            raise HTTPStatus(falcon.HTTP_200, body='\n')

    def process_resource(self, req, resp, resource, params):
        # Place login resource here at the second parameter to ignore login route
        # if isinstance(resource, ):
        #     return

        token = req.auth

        if not token:
            description = ('Please provide an auth token '
                           'as part of the request.')

            raise falcon.HTTPUnauthorized(
                'Auth token required',
                description,
                [],
                href='http://docs.example.com/auth')

        token_decoded = self._token_is_valid(token)
        if not token_decoded:
            description = ('The provided auth token is not valid. '
                           'Please request a new token and try again.')

            raise falcon.HTTPUnauthorized(
                'Authentication required',
                description,)

        req.usuario = token_decoded.get('usuario', None)

    def _token_is_valid(self, token):
        try:
            options = {'verify_exp': True}
            raw_token = token.split(' ')[1]
            usuario = jwt.decode(raw_token, self.secret, verify='True', algorithms=['HS256'], options=options)
            return usuario
        except (jwt.DecodeError, IndexError) as err:
            logstd("Token validation failed Error :{}".format(str(err)))
            return False