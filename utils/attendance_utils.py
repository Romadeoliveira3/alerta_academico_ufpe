from datetime import datetime

def calcular_faltas(data_inicio, data_fim, aulas):
  """
  Calcula o número de faltas de um aluno em um determinado período.

  Args:
    data_inicio: A data de início do período.
    data_fim: A data de fim do período.
    aulas: A lista de aulas do aluno.

  Returns:
    Um dicionário com as seguintes chaves:
    * "total_faltas": O número total de faltas.
    * "faltas_por_aula": Um dicionário com as faltas por aula.
  """

  faltas = {}
  for aula in aulas:
    faltas[aula.nome] = 0

  for dia in range(data_inicio.day, data_fim.day + 1):
    for aula in aulas:
      if aula.dia == dia:
        faltas[aula.nome] += 1

  return {
    "total_faltas": sum(faltas.values()),
    "faltas_por_aula": faltas,
  }

def gerar_notificacao(aluno, curso, percentual_faltas):
  """
  Gera uma notificação para um aluno que está se aproximando do limite de faltas.

  Args:
    aluno: O aluno que está recebendo a notificação.
    curso: O curso do aluno.
    percentual_faltas: O percentual de faltas do aluno.

  Returns:
    Uma string com o texto da notificação.
  """

  if percentual_faltas > 75:
    text = f"Alerta! O aluno {aluno.nome} do curso {curso.nome} ultrapassou o limite de faltas. Percentual de faltas: {percentual_faltas}%. Por favor, entre em contato com o professor para mais informações."
  else:
    text = f"O aluno {aluno.nome} do curso {curso.nome} está se aproximando do limite de faltas. Percentual de faltas: {percentual_faltas}%. Por favor, fique atento às suas faltas."

  return text
