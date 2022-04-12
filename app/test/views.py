import traceback
import falcon

from core.database.connection import connect
from core.response import Error, Response
from core.utils.utils import logstd
from core.error_codes import SERVER

class TestResource:

    def on_get(self, req, resp):
        conn = None
        try:
            conn = connect()
            cursor = conn.cursor()

            select = 'select 1 as um where 1=1;'
            cursor.execute(select)
            
            result = cursor.fetchone()

            if result[0] != 1:
                raise Exception()

            resp.media = Response(payload='success')
            resp.status = falcon.HTTP_200
        except Exception as e:
            traceback.print_exc()
            logstd(str(e))
            resp.media = Response(success=False, error=Error(SERVER))
            resp.status = falcon.HTTP_500
        finally:
            if conn:
                conn.close()