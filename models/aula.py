import sqlite3



class Aula:
  def __init__(self, nome, carga_horaria, aulas_semana):
    self.nome = nome
    self.carga_horaria = carga_horaria
    self.aulas_semana = aulas_semana
    self.semanas = carga_horaria // aulas_semana
    self.total_aulas = self.semanas * aulas_semana
    self.aulas_faltadas = 0

    self.head = None  # Início da lista encadeada. A cabeça da lista é o primeiro nó.

    # Conectar ao banco de dados
    self.conn = sqlite3.connect('aulas.db')
    self.c = self.conn.cursor()

    
  def adicionar_falta(self):
    self.aulas_faltadas += 1
    self.verificar_situacao()

    # Atualizar aulas_faltadas no banco de dados
    self.c.execute('''
        UPDATE aulas
        SET aulas_faltadas = ?
        WHERE nome = ?
    ''', (self.aulas_faltadas, self.nome))

    # Salvar (commit) as alterações
    self.conn.commit()


  def verificar_situacao(self):
    percentual_faltas = (self.aulas_faltadas / self.total_aulas) * 100
    if percentual_faltas > 25:
      print(f"Alerta! Você ultrapassou o limite de faltas na disciplina {self.nome}. Percentual de faltas: {percentual_faltas}%")
    else:
      faltas_restantes = (self.total_aulas * 0.25) - self.aulas_faltadas
      print(f"Você pode faltar mais {faltas_restantes} aulas na disciplina {self.nome} sem ser reprovado por falta.")

  def mostrar_faltas(self):
    return self.aulas_faltadas