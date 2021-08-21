class Graph :

    def __init__(self, edges, directed=False): # Espera => edges = [('A', 'B'), ('B', 'C'), ('A','C')]
        self.directed = directed
        self.neighbors = {}
        self.add_edges(edges)

    def add_edges(self, edges): #Adiciona as arestas em forma de dicionario de listas  
        for x, y, weight in edges:
            self.neighbors.setdefault(x, {}).update({y : weight}) #adiciona a aresta alvo e seu respectivo peso
            if self.directed:
                self.neighbors.setdefault(y, {})
            else:
                self.neighbors.setdefault(y, {}).update({x : weight})

    def get_edges(self): #Devolve todas as arestas do grafo
        edges = []
        for key in self.neighbors.keys():
            for value in self.neighbors[key]:
                edges.append((key, value, self.neighbors[key][value]))
        return edges

    def get_vertices(self): #Devolve todos os vertices
        return list(self.neighbors.keys())

    def egde_exists(self, edge:tuple): #Devolve se uma aresta existe no grafo ou não
        return edge[0] in self.neighbors and edge[1] in self.neighbors[edge[0]]

    def get_neighbors(self):
        return self.neighbors