import sqlite3
from aula import Aula

class ListaDeAulas:
    def __init__(self):
        self.head = None  # Início da lista encadeada. A cabeça da lista é o primeiro nó.
        # Conectar ao banco de dados
        self.conn = sqlite3.connect('aulas.db')
        self.c = self.conn.cursor()

    def adicionar_aula(self, nome, carga_horaria, aulas_semana):
        nova_aula = Aula(nome, carga_horaria, aulas_semana)
        nova_aula.next = self.head  # O próximo nó da nova aula é a atual cabeça da lista.
        self.head = nova_aula  # A nova aula se torna a nova cabeça da lista.

    def adicionar_falta(self, nome):
        aula_atual = self.head  # Começamos na cabeça da lista.
        while aula_atual is not None:  # Enquanto não chegarmos ao final da lista.
            if aula_atual.nome == nome:  # Se encontrarmos a aula.
                aula_atual.adicionar_falta()  # Adicionamos a falta.
                return
            aula_atual = aula_atual.next  # Vamos para o próximo nó na lista.
        print(f"Aula {nome} não encontrada.")

    def mostrar_aulas(self):
        aula_atual = self.head  # Começamos na cabeça da lista.
        while aula_atual is not None:  # Enquanto não chegarmos ao final da lista.
            print(f'Nome da aula: {aula_atual.nome}, Faltas: {aula_atual.mostrar_faltas()}')
            aula_atual = aula_atual.next  # Vamos para o próximo nó na lista.

    def buscar_aula(self, nome):
        # Buscar aula no banco de dados
        self.c.execute('''
            SELECT * FROM aulas
            WHERE nome = ?
        ''', (nome,))

        aula = self.c.fetchone()

        if aula is not None:
            return aula
        else:
            print(f"Aula {nome} não encontrada.")
            return None

    def inserir_apos(self, nome, novo_nome, carga_horaria, aulas_semana):
        aula_atual = self.head  # Começamos na cabeça da lista.
        while aula_atual is not None:  # Enquanto não chegarmos ao final da lista.
            if aula_atual.nome == nome:  # Se encontrarmos a aula.
                semanas = carga_horaria // aulas_semana
                total_aulas = semanas * aulas_semana
                self.c.execute('''
                    INSERT INTO aulas(nome, carga_horaria, aulas_semana, semanas, total_aulas, aulas_faltadas)
                    VALUES(?,?,?,?,?,?)
                ''', (novo_nome, carga_horaria, aulas_semana, semanas, total_aulas, 0))
                self.conn.commit()
                return
            aula_atual = aula_atual.next  # Vamos para o próximo nó na lista.
        print(f"Aula {nome} não encontrada.")

    def remover_aula(self, nome):
        # Remover aula do banco de dados
        self.c.execute('''
            DELETE FROM aulas
            WHERE nome = ?
        ''', (nome,))

        # Salvar (commit) as alterações
        self.conn.commit()

    def obter_aula_por_indice(self, indice):
        # Obter aula pelo índice no banco de dados
        self.c.execute('''
            SELECT * FROM aulas
            LIMIT 1 OFFSET ?
        ''', (indice,))

        aula = self.c.fetchone()

        if aula is not None:
            return aula
        else:
            print(f"Índice {indice} não encontrado.")
            return None

    def atualizar_aula_por_indice(self, indice, novo_nome, nova_carga_horaria, novas_aulas_semana):
        # Obter aula pelo índice no banco de dados
        self.c.execute('''
            SELECT * FROM aulas
            LIMIT 1 OFFSET ?
        ''', (indice,))

        aula = self.c.fetchone()

        if aula is not None:
            # Atualizar aula no banco de dados
            self.c.execute('''
                UPDATE aulas
                SET nome = ?, carga_horaria = ?, aulas_semana = ?
                WHERE nome = ?
            ''', (novo_nome, nova_carga_horaria, novas_aulas_semana, aula[0]))

            # Salvar (commit) as alterações
            self.conn.commit()
        else:
            print(f"Índice {indice} não encontrado.")

    def get_all_aulas(self):
        # Buscar todas as aulas no banco de dados
        self.c.execute('''
            SELECT * FROM aulas
        ''')

        aulas = self.c.fetchall()

        return aulas