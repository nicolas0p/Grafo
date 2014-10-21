import unittest

from grafo import Grafo
from grafo import Vertice

class TesteGrafo(unittest.TestCase):

    def setUp(self):
        self.grafo = Grafo()

    def teste_adicionar_vertice_aumenta_tamanho(self):
        self.grafo.adicionar_vertice(Vertice('a'))
        self.assertEqual(self.grafo.ordem(), 1)

    def teste_remover_vertice_diminui_tamanho(self):
        self.grafo.adicionar_vertice(Vertice('a'))
        self.grafo.remover_vertice('a')
        self.assertEqual(self.grafo.ordem(), 0)

if __name__ == '__main__':
    unittest.main()
