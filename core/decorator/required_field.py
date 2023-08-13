import traceback
import falcon
from core.response import Error, Response
from core.utils.utils import logstd

def required_fields(fields: tuple):
    '''Validates POST, PUT and GET requests
    - The fields MUST be in the body
    - The fields CAN'T be empty/null

    \* OTHER METHODS WILL BE DENIED
    '''
    def verify_fields(func):
        def wraper(*args, **kwargs):
            error = False
            errors = []
            if len(args) == 3:
                try:
                    _, req, resp = args
                    # Validates POST and PUT body to find fields
                    if req.method == 'POST' or req.method == 'PUT' or req.method == 'DELETE':
                        if hasattr(req, 'media'):
                            body = req.media
                            for field in fields:
                                if field not in body or not body[field]:
                                    resp.status = falcon.HTTP_400
                                    errors.append(field)
                                    error = True
                    # Validates GET query params to find fields
                    elif req.method == 'GET':
                        if hasattr(req, 'params'):
                            body = req.params
                            for field in fields:
                                if field not in body or not body[field]:
                                    resp.status = falcon.HTTP_400
                                    errors.append(field)
                                    error = True
                except Exception as e:
                    traceback.print_exc()
                    logstd(str(e))
                    error = True
                    resp.status = falcon.HTTP_400
                    errors = resp.status

            if not error:
                func(*args, **kwargs)
            else:
                resp.media = Response(success=False, error=Error(400, errors))
            return
        return wraper
    return verify_fields