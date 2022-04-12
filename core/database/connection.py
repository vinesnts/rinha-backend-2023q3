import psycopg2

from core.settings import DATABASES
from core.utils.utils import logstd

SGBD = ['postgres', 'sqlserver']

PARAM_FORMAT = {
  'postgres': '%s',
  'sqlserver': '?'
}

def dict_fetchall(cursor):
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

def dict_fetchone(cursor):
    columns = [col[0] for col in cursor.description]
    result = cursor.fetchone()
    return dict(zip(columns, result)) if result else None

def postgres(connection):
  logstd(f"begin connecting {connection['name']} db")
  connect = psycopg2.connect(f"dbname='{connection['name']}' user='{connection['user']}' host='{connection['host']}' port={connection['port']} password='{connection['password']}'")
  logstd(f"end connecting {connection['name']} db")

  return connect

def dict_fetchall(cursor):
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

def dict_fetchone(cursor):
    columns = [col[0] for col in cursor.description]
    result = cursor.fetchone()
    return dict(zip(columns, result)) if result else None

def connect(db: str = 'default', sgbd: str = 'postgres', databases: dict = None):
  if sgbd == 'postgres':
    return postgres(databases if databases else DATABASES[db])