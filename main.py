from calc import Disciplina, Aula, ListaDeAulas, Historico, Acao

# Criação da lista de aulas
lista_de_aulas = ListaDeAulas()
lista_de_aulas.adicionar_aula("Matemática", 60, 3)
lista_de_aulas.adicionar_aula("Física", 60, 3)

# Criação do histórico
historico = Historico()

# Adicionando faltas e registrando ações no histórico
aula_matematica = lista_de_aulas.head  # Supondo que a aula de Matemática seja a primeira na lista
mensagem = aula_matematica.adicionar_falta()
acao = Acao("falta", aula_matematica, mensagem)
historico.adicionar_acao(acao)

aula_fisica = aula_matematica.next  # Supondo que a aula de Física seja a segunda na lista
mensagem = aula_fisica.adicionar_falta()
acao = Acao("falta", aula_fisica, mensagem)
historico.adicionar_acao(acao)

# Mostrando o histórico de ações
historico.mostrar_historico()

# # Desfazendo a última ação e mostrando o histórico atualizado
# historico.desfazer_acao()
# historico.mostrar_historico()
