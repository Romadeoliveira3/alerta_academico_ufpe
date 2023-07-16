import sys
sys.path.append(r'.\models')

import unittest
from aula import Aula
from lista_de_aulas import ListaDeAulas


class TestAulaMethods(unittest.TestCase):

    def setUp(self):
        self.aula = Aula('Matemática', 40, 4)

    def test_adicionar_falta(self):
        self.aula.adicionar_falta()
        self.assertEqual(self.aula.mostrar_faltas(), 1)

    def test_verificar_situacao(self):
        for _ in range(11):
            self.aula.adicionar_falta()
        self.assertEqual(self.aula.verificar_situacao(), "Alerta! Você ultrapassou o limite de faltas na disciplina Matemática. Percentual de faltas: 27.5%")

class TestListaDeAulasMethods(unittest.TestCase):

    def setUp(self):
        self.lista_de_aulas = ListaDeAulas()
        self.lista_de_aulas.adicionar_aula('Matemática', 40, 4)
        self.lista_de_aulas.adicionar_aula('Português', 40, 4)

    def test_adicionar_aula(self):
        self.lista_de_aulas.adicionar_aula('História', 40, 4)
        self.assertIsNotNone(self.lista_de_aulas.buscar_aula('História'))

    def test_adicionar_falta(self):
        self.lista_de_aulas.adicionar_falta('Matemática')
        aula = self.lista_de_aulas.buscar_aula('Matemática')
        self.assertEqual(aula.mostrar_faltas(), 1)

    def test_remover_aula(self):
        self.lista_de_aulas.remover_aula('Português')
        self.assertIsNone(self.lista_de_aulas.buscar_aula('Português'))

if __name__ == '__main__':
    unittest.main()
