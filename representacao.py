class ListaAdjacencia:
    def __init__ (self, n_vertices, arestas):
        self.n_arestas = len(arestas) # numero de arestas #
        self.nodes = [] # lista com os nós #
        for K in range (n_vertices):
            self.nodes.append([]) # lista com os índices dos vértices #
        for aresta in arestas: # declaração das arestas #
            (inicio, fim) = aresta 
            self.nodes[inicio].append(fim) 
            self.nodes[fim].append(inicio)
    def get_arestas(self, node): 
        return self.nodes[node] # retorna as arestas do nó #
    
    def n_nodes (self):
        return len(self.nodes) # número de vértices #
    
class MatrixAdjacencia:
    def __init__ (self, n_vertices, arestas):
        self.n_arestas = len(arestas) # numero de arestas #
        self.nodes = [] # lista com os nós #
        for i in range (n_vertices):
            matrix = []
            for j in range (n_vertices):
                matrix.append(0)
            self.nodes.append(matrix)
        
        for aresta in arestas: # declaração das arestas #
            (inicio, fim) = aresta
            self.nodes[inicio][fim] = 1 # define em 1 se dois vértices estiverem ligados #
            self.nodes[fim][inicio] = 1 # define em 1 se dois vértices estiverem ligados #
    def get_arestas(self, node): # retorna as arestas do nó #
        nos = [] # lista com os vértices #
        index = 0
        for i in self.nodes[node]: #
            if i != 0:
                nos.append(index)
            index += 1
        return nos
    
    def n_nodes (self):
        return len(self.nodes) # número de vértices #
    

        
                



