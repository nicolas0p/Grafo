
#vertices e um dict{nome:Vertice}
#arestas e um dict{nome vertice:set<Vertice>} que representa que existe uma aresta entre v1 e todos os vertices da lista
class Grafo:

    def __init__(self):
        self._vertices = {}
        self._arestas = {}

    def adicionar_vertice(self, vertice):
        self._vertices[vertice.nome] = vertice
        self._arestas[vertice.nome] = set()

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
        adjacentes_v1.add(vertice2)
        adjacentes_v2.add(vertice1)

    def desconectar(self, vertice1, vertice2):
        adjacentes_v1 = self._arestas[vertice1.nome]
        adjacentes_v2 = self._arestas[vertice2.nome]
        adjacentes_v1.remove(vertice2)
        adjacentes_v2.remove(vertice1)

    def estao_conectados(self, vertice1, vertice2):
        try:
            adjacentes_v1 = self._arestas[vertice1.nome]
            adjacentes_v2 = self._arestas[vertice2.nome]
            return vertice2 in adjacentes_v1 and vertice1 in adjacentes_v2
        except KeyError:
            return False

    def vertices(self):
        return self._vertices.copy()

    def vertice_qualquer(self):
        for vertice in self._vertices:
            return self._vertices[vertice]

    def adjacentes(self, vertice):
        return self._arestas[vertice.nome].copy()

    def grau(self, vertice):
        return len(self.adjacentes(vertice))

    def eRegular(self):
        if len(self._vertices) == 0:
            return False
        vertice1 = self.vertice_qualquer()
        grau = self.grau(vertice1)
        for nome in self._vertices:
            if not (self.grau(self._vertices[nome]) == grau):
                return False
        return True

class Vertice:

    def __init__(self, nome):
        self.nome = nome
