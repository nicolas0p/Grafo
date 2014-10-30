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


def teste_e_arvore(self):
    a = Vertice('a')
    b = Vertice('b')
    c = Vertice('c')
    d = Vertice('d')
    e = Vertice('e')
    f = Vertice('f')

    for vertice in {a, b, c, d, e, f}:
        self.grafo.adicionar_vertice(vertice)

    self.grafo.conectar(a, b)
    self.grafo.conectar(a, d)
    self.grafo.conectar(d, c)
    self.grafo.conectar(d, f)
    self.grafo.conectar(c, e)

    self.assertTrue(self.grafo.e_arvore())

