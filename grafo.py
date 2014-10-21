
#vertices é um dict{nome:Vertice}
#arestas é um dict{vertice v1:Lista<Vertice>} que representa que existe uma aresta entre v1 e todos os vertices da lista
class Grafo:

    def __init__(self):
        self._vertices = {}
        self._arestas = {}

    def adicionar_vertice(self, vertice):
        self._vertices[vertice.nome] = vertice
        self._arestas[vertice.nome] = []

    def remover_vertice(self, vertice):
        adjacentes = self._arestas[vertice.nome]
        for adjacente in adjacentes:
            self._arestas[adjacente.nome].remove(vertice)
        del self._vertices[vertice.nome]
        del self._arestas[vertice.nome]

    def ordem(self):
        return len(self._vertices)

    def conectar(self, vertice1, vertice2):
        adjacentes_v1 = self._arestas[vertice1.nome]
        adjacentes_v2 = self._arestas[vertice2.nome]
        adjacentes_v1.append(vertice2)
        adjacentes_v2.append(vertice1)

    def estao_conectados(self, vertice1, vertice2):
        adjacentes_v1 = self._arestas[vertice1.nome]
        adjacentes_v2 = self._arestas[vertice2.nome]
        return vertice2 in adjacentes_v1 and vertice1 in adjacentes_v2

class Vertice:

    def __init__(self, nome):
        self.nome = nome