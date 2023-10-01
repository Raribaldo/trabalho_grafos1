class ListaAdjacencia:
    def __init__ (self, n_Vertices, Arestas):
        self.nodes = []
        for K in range (n_Vertices):
            self.nodes.append([])
        for Aresta in Arestas:
            (inicio, fim) = Aresta
            self.nodes[inicio].append(fim)
            self.nodes[fim].append(inicio)
    def getArestas(self, node):
        return self.nodes[node]
    
class MatrixAdjacencia:
    def __init__ (self, n_Vertices, Arestas):
        self.nodes = []
        for i in range (n_Vertices):
            matrix = []
            for j in range (n_Vertices):
                matrix.append(0)
            self.nodes.append(matrix)
        
        for Aresta in Arestas:
            (inicio, fim) = Aresta
            self.nodes[inicio][fim] = 1
            self.nodes[fim][inicio] = 1
    def getArestas(self, node):
        nos = []
        index = 0
        for i in self.nodes[node]:
            if i != 0:
                nos.append(index)
            index += 1
        return nos
    

        
                



