
#vertices é um dict{nome:Vertice}
#arestas é um dict{vertice v1:Lista<Vertice>} que representa que existe uma aresta entre v1 e todos os vertices da lista
class Grafo:

    def __init__(self):
        self._vertices = {}
        self._arestas = {}

    def adicionar_vertice(self, vertice):
        self._vertices[vertice.nome] = vertice

    def remover_vertice(self, nome_do_vertice):
        del self._vertices[nome_do_vertice]

    def ordem(self):
        return len(self._vertices)


class Vertice:

    def __init__(self, nome):
        self.nome = nome
