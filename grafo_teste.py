import unittest

from grafo import Graph
from grafo import Vertice
from grafo import VerticeNaoPodeSeConectarComEleMesmoException
from grafo import VerticeNaoPertenceAoGrafoException
from grafo import ArestaNaoExisteException


class GrafoTeste(unittest.TestCase):

    def setUp(self):
        self.grafo = Graph()

    def adicionar_vertices(self):
        a = Vertice('a')
        b = Vertice('b')
        c = Vertice('c')
        conj = {'a': a, 'b': b, 'c': c}
        for key in conj:
            self.grafo.adicionar_vertice(conj[key])
        return conj

    def teste_adicionar_vertice_aumenta_tamanho(self):
        self.grafo.adicionar_vertice(Vertice('a'))
        self.assertEqual(self.grafo.ordem(), 1)

    def teste_remover_vertice_diminui_tamanho(self):
        a = Vertice('a')
        self.grafo.adicionar_vertice(a)
        self.grafo.remover_vertice(a)
        self.assertEqual(self.grafo.ordem(), 0)

    def teste_remover_aresta_inexistente(self):
        a = Vertice('a')
        b = Vertice('b')
        self.grafo.adicionar_vertice(a)
        self.grafo.adicionar_vertice(b)
        self.assertRaises(ArestaNaoExisteException, self.grafo.desconectar, a, b)

    def teste_vertice_nao_pode_ser_conectado_com_ele_mesmo(self):
        a = Vertice('a')
        self.grafo.adicionar_vertice(a)
        self.assertRaises(VerticeNaoPodeSeConectarComEleMesmoException, self.grafo.conectar, a,a)

    def teste_remover_vertice_remove_arestas_conectadas_nele(self):
        conj = self.adicionar_vertices()
        self.grafo.conectar(conj['a'], conj['b'])
        self.grafo.conectar(conj['b'], conj['c'])
        self.grafo.remover_vertice(conj['a'])
        self.assertFalse(self.grafo.estao_conectados(conj['a'], conj['b']))
        self.assertTrue(self.grafo.estao_conectados(conj['b'], conj['c']))

    def teste_conectar_dois_vertices(self):
        a = Vertice('a')
        b = Vertice('b')
        self.grafo.adicionar_vertice(a)
        self.grafo.adicionar_vertice(b)
        self.grafo.conectar(a, b)
        self.assertTrue(self.grafo.estao_conectados(a, b))

    def teste_ordem(self):
        self.adicionar_vertices()
        self.assertEqual(self.grafo.ordem(), 3)

    def teste_obter_todos_os_vertices(self):
        conj = self.adicionar_vertices()
        self.assertDictEqual(self.grafo.vertices(), conj)

    def teste_adjacentes(self):
        conj = self.adicionar_vertices()
        a = conj['a']
        b = conj['b']
        c = conj['c']
        self.grafo.conectar(a, b)
        self.grafo.conectar(a, c)
        self.assertSetEqual(self.grafo.adjacentes(a), {b, c})

    def teste_grau_de_vertice(self):
        conj = self.adicionar_vertices()
        a = conj['a']
        b = conj['b']
        c = conj['c']
        self.grafo.conectar(a, b)
        self.grafo.conectar(a, c)
        self.assertEqual(self.grafo.grau(a), 2)

    def teste_grafo_vazio_nao_e_regular(self):
        grafo = Graph()
        self.assertFalse(grafo.e_regular())

    def teste_nao_regular(self):
        conj = self.adicionar_vertices()
        self.grafo.conectar(conj['a'], conj['b'])
        self.grafo.conectar(conj['a'], conj['c'])
        self.assertFalse(self.grafo.e_regular())

    def teste_e_regular(self):
        conj = self.adicionar_vertices()
        self.grafo.conectar(conj['a'], conj['b'])
        self.grafo.conectar(conj['a'], conj['c'])
        self.grafo.conectar(conj['b'], conj['c'])
        self.assertTrue(self.grafo.e_regular())

    def teste_e_completo(self):
        conj = self.adicionar_vertices()
        for v1 in conj:
            for v2 in conj:
                if v1 != v2:
                    self.grafo.conectar(conj[v1], conj[v2])
        self.assertTrue(self.grafo.e_completo())

    def teste_nao_completo(self):
        conj = self.adicionar_vertices()
        for v1 in conj:
            for v2 in conj:
                if v1 != v2:
                    self.grafo.conectar(conj[v1], conj[v2])
        self.grafo.desconectar(conj['a'], conj['b'])
        self.assertFalse(self.grafo.e_completo())

    def teste_fecho_transitivo_com_ciclo(self):
        a = Vertice('a')
        b = Vertice('b')
        c = Vertice('c')
        d = Vertice('d')

        self.grafo.adicionar_vertice(a)
        self.grafo.adicionar_vertice(b)
        self.grafo.adicionar_vertice(c)
        self.grafo.adicionar_vertice(d)
        self.grafo.adicionar_vertice(Vertice('e'))
        self.grafo.adicionar_vertice(Vertice('f'))

        self.grafo.conectar(a, b)
        self.grafo.conectar(a, c)
        self.grafo.conectar(c, b)
        self.grafo.conectar(c, d)
        self.grafo.conectar(Vertice('e'), Vertice('f'))

        self.assertSetEqual(self.grafo.fecho_transitivo(a), {a, b, c, d})

    def teste_fecho_transitivo_sem_ciclo(self):
        a = Vertice('a')
        b = Vertice('b')
        c = Vertice('c')
        d = Vertice('d')

        self.grafo.adicionar_vertice(a)
        self.grafo.adicionar_vertice(b)
        self.grafo.adicionar_vertice(c)
        self.grafo.adicionar_vertice(d)
        self.grafo.adicionar_vertice(Vertice('e'))
        self.grafo.adicionar_vertice(Vertice('f'))

        self.grafo.conectar(a, b)
        self.grafo.conectar(a, c)
        self.grafo.conectar(c, d)
        self.grafo.conectar(Vertice('e'), Vertice('f'))

        self.assertSetEqual(self.grafo.fecho_transitivo(a), {a, b, c, d})

    def teste_e_conexo(self):
        a = Vertice('a')
        b = Vertice('b')
        c = Vertice('c')
        d = Vertice('d')

        self.grafo.adicionar_vertice(a)
        self.grafo.adicionar_vertice(b)
        self.grafo.adicionar_vertice(c)
        self.grafo.adicionar_vertice(d)

        self.grafo.conectar(a, b)
        self.grafo.conectar(a, c)
        self.grafo.conectar(c, b)
        self.grafo.conectar(c, d)

        self.assertTrue(self.grafo.e_conexo())

    def teste_nao_e_conexo(self):
        a = Vertice('a')
        b = Vertice('b')
        c = Vertice('c')
        d = Vertice('d')
        e = Vertice('e')

        self.grafo.adicionar_vertice(a)
        self.grafo.adicionar_vertice(b)
        self.grafo.adicionar_vertice(c)
        self.grafo.adicionar_vertice(d)
        self.grafo.adicionar_vertice(e)

        self.grafo.conectar(a, b)
        self.grafo.conectar(a, c)
        self.grafo.conectar(c, b)
        self.grafo.conectar(c, d)

        self.assertFalse(self.grafo.e_conexo())


if __name__ == '__main__':
    unittest.main()
