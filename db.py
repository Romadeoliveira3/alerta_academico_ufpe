import sqlite3

# Criar uma conexão com o banco de dados
conn = sqlite3.connect('aulas.db')

# Criar um cursor para a conexão
c = conn.cursor()

# Criar uma tabela para as aulas
c.execute('''
CREATE TABLE aulas (
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
conn.close()