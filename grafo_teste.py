import unittest

from grafo import Grafo
from grafo import Vertice

class GrafoTeste(unittest.TestCase):

    def setUp(self):
        self.grafo = Grafo()

    def teste_adicionar_vertice_aumenta_tamanho(self):
        self.grafo.adicionar_vertice(Vertice('a'))
        self.assertEqual(self.grafo.ordem(), 1)

    def teste_remover_vertice_diminui_tamanho(self):
        a = Vertice('a')
        self.grafo.adicionar_vertice(a)
        self.grafo.remover_vertice(a)
        self.assertEqual(self.grafo.ordem(), 0)

    def teste_conectar_dois_vertices(self):
        a = Vertice('a')
        b = Vertice('b')
        self.grafo.adicionar_vertice(a)
        self.grafo.adicionar_vertice(b)
        self.grafo.conectar(a,b)
        self.assertTrue(self.grafo.estao_conectados(a,b))

if __name__ == '__main__':
    unittest.main()
