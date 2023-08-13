from core.utils.utils import logstd

def insert_pessoa(cursor, body):
  query = f'''
    insert into public.pessoa ({','.join(key for key in body)})
    values ({','.join([f'%({key})s' for key in body])})
    returning id;
  '''
  logstd(query)
  cursor.execute(query, {key: value for key, value in body.items()})
  return cursor.fetchone()

def select_pessoa_by_id(cursor, id):
  query = '''
    select p.id, p.apelido, p.nome, to_char(p.nascimento, 'YYYY-MM-DD') as nascimento, p.stack
    from public.pessoa p
    where p.id = %(id)s
  '''
  logstd(query)
  cursor.execute(query, {
    'id': id
  })
  return cursor.fetchone()

def select_pessoa_by_apelido(cursor, apelido):
  query = '''
    select p.id, p.apelido, p.nome, to_char(p.nascimento, 'YYYY-MM-DD') as nascimento, p.stack
    from public.pessoa p
    where p.apelido = %(apelido)s
  '''
  logstd(query)
  cursor.execute(query, {
    'apelido': apelido
  })
  return cursor.fetchall()
  
def filter_pessoa(cursor, filtro):
  query = '''
    select p.id, p.apelido, p.nome, to_char(p.nascimento, 'YYYY-MM-DD') as nascimento, p.stack
    from public.pessoa p
    where p.apelido ilike %(filtro)s 
      or p.nome ilike %(filtro)s
      or exists (select 1 from unnest(p.stack) el where el ILIKE %(filtro)s)
  '''
  logstd(query)
  cursor.execute(query, {
    'filtro': f'%{filtro}%'
  })
  return cursor.fetchall()

def count_pessoa(cursor):
  query = '''
    select count(*) as total from public.pessoa
  '''
  logstd(query)
  cursor.execute(query)
  return cursor.fetchone()