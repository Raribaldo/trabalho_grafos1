class ListaAdjacencia:
    def __init__ (self, n_vertices, arestas):
        self.n_arestas = len(arestas)
        self.nodes = []
        for K in range (n_vertices):
            self.nodes.append([])
        for aresta in arestas:
            (inicio, fim) = aresta
            self.nodes[inicio].append(fim)
            self.nodes[fim].append(inicio)
    def get_arestas(self, node):
        return self.nodes[node]
    
    def n_nodes (self):
        return len(self.nodes)
    
class MatrixAdjacencia:
    def __init__ (self, n_vertices, arestas):
        self.n_arestas = len(arestas)
        self.nodes = []
        for i in range (n_vertices):
            matrix = []
            for j in range (n_vertices):
                matrix.append(0)
            self.nodes.append(matrix)
        
        for aresta in arestas:
            (inicio, fim) = aresta
            self.nodes[inicio][fim] = 1
            self.nodes[fim][inicio] = 1
    def get_arestas(self, node):
        nos = []
        index = 0
        for i in self.nodes[node]:
            if i != 0:
                nos.append(index)
            index += 1
        return nos
    
    def n_nodes (self):
        return len(self.nodes)
    

        
                



