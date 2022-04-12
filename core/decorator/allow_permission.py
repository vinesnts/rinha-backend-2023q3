import falcon
from app.usuario.permissions import ADMIN
from core.error_codes import FORBIDDEN
from core.response import Error, Response

def allow_permissions(permissions: tuple):
    def verify_permission(func):
        def wraper(*args, **kwargs):
            error = False
            if len(args) == 3:
                _, req, resp = args
                if hasattr(req, 'usuario'):
                    usuario = req.usuario
                    permissao = usuario.get('id_permissao', None)
                    if not int(permissao) == ADMIN:
                        if int(permissao) not in permissions:
                            resp.status = falcon.HTTP_403
                            error = True

            if not error:
                func(*args, **kwargs)
            else:
                resp.media = Response(success=False, error=Error(FORBIDDEN))
            return
        return wraper
    return verify_permission