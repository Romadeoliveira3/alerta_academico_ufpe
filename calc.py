# calc.py
class Disciplina:
    def __init__(self, nome, carga_horaria, aulas_semana):
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.aulas_semana = aulas_semana
        self.semanas = carga_horaria // aulas_semana
        self.total_aulas = self.semanas * aulas_semana
        self.aulas_faltadas = 0

    def adicionar_falta(self):
        self.aulas_faltadas += 1
        self.verificar_situacao()

    def verificar_situacao(self):
        percentual_faltas = (self.aulas_faltadas / self.total_aulas) * 100
        if percentual_faltas > 25:
            print(f"Alerta! Você ultrapassou o limite de faltas na disciplina {self.nome}. Percentual de faltas: {percentual_faltas}%")
        else:
            faltas_restantes = (self.total_aulas * 0.25) - self.aulas_faltadas
            print(f"Você pode faltar mais {faltas_restantes} aulas na disciplina {self.nome} sem ser reprovado por falta.")

    def mostrar_faltas(self):
        return self.aulas_faltadas

class Aula:
    def __init__(self, nome, carga_horaria, aulas_semana):
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.aulas_semana = aulas_semana
        self.semanas = carga_horaria // aulas_semana
        self.total_aulas = self.semanas * aulas_semana
        self.aulas_faltadas = 0
        self.next = None  # Ponteiro para a próxima aula na lista encadeada

    def adicionar_falta(self):
        self.aulas_faltadas += 1
        return self.verificar_situacao()

    def verificar_situacao(self):
        percentual_faltas = (self.aulas_faltadas / self.total_aulas) * 100
        if percentual_faltas > 25:
            return f"Alerta! Você ultrapassou o limite de faltas na disciplina {self.nome}. Percentual de faltas: {percentual_faltas}%"
        else:
            faltas_restantes = (self.total_aulas * 0.25) - self.aulas_faltadas
            return f"Você pode faltar mais {faltas_restantes} aulas na disciplina {self.nome} sem ser reprovado por falta."

    def mostrar_faltas(self):
        return self.aulas_faltadas


class ListaDeAulas:
    def __init__(self):
        self.head = None  # Início da lista encadeada

    def adicionar_aula(self, nome, carga_horaria, aulas_semana):
        nova_aula = Aula(nome, carga_horaria, aulas_semana)
        nova_aula.next = self.head
        self.head = nova_aula

    def adicionar_falta(self, nome):
        aula_atual = self.head
        while aula_atual is not None:
            if aula_atual.nome == nome:
                aula_atual.adicionar_falta()
                return
            aula_atual = aula_atual.next
        print(f"Aula {nome} não encontrada.")

    def mostrar_aulas(self):
        aula_atual = self.head
        while aula_atual is not None:
            print(f'Nome da aula: {aula_atual.nome}, Faltas: {aula_atual.mostrar_faltas()}')
            aula_atual = aula_atual.next

class Acao:
    def __init__(self, tipo, aula, msg):
        self.tipo = tipo  # Tipo de ação (por exemplo, "falta")
        self.aula = aula  # Aula associada à ação
        self.msg = msg    # Mensagem associada

class Historico:
    def __init__(self):
        self.pilha = []

    def adicionar_acao(self, acao):
        self.pilha.append(acao)

    def desfazer_acao(self):
        if self.pilha:
            acao = self.pilha.pop()
            if acao.tipo == "falta":
                acao.aula.aulas_faltadas -= 1
                print(f"Desfeita a falta na aula {acao.aula.nome}.")
        else:
            print("Nenhuma ação para desfazer.")

    def mostrar_historico(self):
        for acao in self.pilha:
            print(f"Ação: {acao.tipo}, Aula: {acao.aula.nome}")
