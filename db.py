import sqlite3
from flask import g

DATABASE = 'aulas.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
  # Criar uma conexão com o banco de dados
  conn = sqlite3.connect('aulas.db')

  # Criar um cursor para a conexão
  c = conn.cursor()

  # Criar uma tabela para as aulas
  c.execute('''
  CREATE TABLE IF NOT EXISTS aulas (
    nome TEXT,
    carga_horaria INTEGER,
    aulas_semana INTEGER,
    semanas INTEGER,
    total_aulas INTEGER,
    aulas_faltadas INTEGER,
    percentual_faltas FLOAT
  )
  ''')

  # Salvar as alterações no banco de dados
  conn.commit()

  # Fechar a conexão com o banco de dados
def close_connection(exception):
  db = getattr(g, '_database', None)
  if db is not None:
      db.close()
