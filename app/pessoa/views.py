from typing import List

import falcon
import traceback

from datetime import datetime, date

from psycopg2.extras import RealDictCursor

from core.database.connection import connect
from core.response import Response, Error
from core.exception.CannotBeNullException import CannotBeNullException
from core.exception.MustBeStrException import MustBeStrException
from core.exception.MustBeStrListException import MustBeStrListException
from core.exception.MustBeDateException import MustBeDateException

from app.pessoa import queries

fields_configs = [
  { 'name': 'apelido', 'required': True },
  { 'name': 'nome', 'required': True },
  { 'name': 'nascimento', 'required': True },
  { 'name': 'stack', 'required': False },
]
fields = [col['name'] for col in fields_configs]

class Pessoa:

  def on_get(self, req, resp, id: str = None):
    try:
      if id is None:
        t = req.params.get('t')
        if not t:
          resp.status = falcon.HTTP_400
          resp.media = Response(success=False, error=Error(400, 'Bad request'))
          return
        
        with connect() as conn:
          cursor = conn.cursor(cursor_factory=RealDictCursor)
          pessoas = queries.filter_pessoa(cursor, t)
          resp.status = falcon.HTTP_200
          resp.media = pessoas
          return

      with connect() as conn:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        pessoa = queries.select_pessoa_by_id(cursor, id)
        if not pessoa:
          resp.status = falcon.HTTP_404
          resp.media = Response(success=False, error=Error(404, 'Not found'))
          return
        
        resp.status = falcon.HTTP_200
        resp.media = pessoa
    except Exception as e:
      traceback.print_exc()
      resp.status = falcon.HTTP_500
      resp.media = Response(success=False, error=Error(500, 'Server'))

  def on_post(self, req, resp):
    try:
      body = req.media
      for field in fields:
        try:
          Pessoa._validate_field(field, body)
        except CannotBeNullException as e:
          resp.status = falcon.HTTP_422
          resp.media = Response(success=False, error=Error(422, str(e)))
          return
        except (MustBeStrException, MustBeStrListException, MustBeDateException) as e:
          resp.status = falcon.HTTP_400
          resp.media = Response(success=False, error=Error(400, str(e)))
          return
      with connect() as conn:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        pessoas = queries.select_pessoa_by_apelido(cursor, body['apelido'])
        if pessoas:
          resp.status = falcon.HTTP_422
          resp.media = Response(success=False, error=Error(422, f'pessoa com apelido "{body["apelido"]}" já cadastrada'))
          return
        
        pessoa = queries.insert_pessoa(cursor, body)
        resp.status = falcon.HTTP_201
        resp.media = Response(payload=pessoa)
        resp.append_header('Location', f'/pessoas/{pessoa["id"]}')
    except Exception as e:
      traceback.print_exc()
      resp.status = falcon.HTTP_500
      resp.media = Response(success=False, error=Error(500, 'Server'))
  
  @staticmethod
  def _validate_field(field_name, body):
    field = next((field for field in fields_configs if field['name'] == field_name), {})
    print(body, field)
    if not body.get(field_name) and field['required']:
      raise CannotBeNullException(f'"{field_name}" não pode ser null')
    if field_name in ('apelido', 'nome') and type(body[field_name]) != str:
      raise MustBeStrException(f'"{field_name}" deve ser string')
    if field_name == 'stack':
      if (type(body.get(field_name)) != list
            and body.get(field_name) is not None) \
          or (type(body.get(field_name)) == list 
            and not all([type(value) == str for value in body.get(field_name)])):
        raise MustBeStrListException(f'"{field_name}" deve ser um array de apenas strings')
    if field_name == 'nascimento':
      try:
        datetime.strptime(body[field_name], '%Y-%m-%d').date()
      except:
        raise MustBeDateException(f'"{field_name}" deve ser data no formato AAAA-MM-DD')
      
class ContagemPessoa:

  def on_get(self, req, resp):
    with connect() as conn:
      cursor = conn.cursor(cursor_factory=RealDictCursor)
      res = queries.count_pessoa(cursor)
      resp.status = falcon.HTTP_200
      resp.media = res['total']