from representacao import ListaAdjacencia, MatrixAdjacencia

class Grafo:
    def __init__ (self, e_matrix, nome_arquivo):
        if e_matrix:
            self.escolha = MatrixAdjacencia (0, [])
        else:
            self.escolha = ListaAdjacencia (0, [])

    def bfs (self, node):
        arvore = [None] * self.escolha.n_nodes()
        fila = [(node, None, 0)]
        while len(fila) > 0:
            (no, pai, nivel) = fila.pop(0)
            if arvore[no] is None:      
                arvore[no] = (nivel, pai)
                for i in self.escolha.get_arestas(no):
                    fila.append((i, no, nivel+1))
        return arvore

    def dfs (self, node):
        arvore = [None] * self.escolha.n_nodes()
        pilha = [(node, None, 0)]
        while len(pilha) > 0:
            (no, pai, nivel) = pilha.pop()
            if arvore[no] is None:      
                arvore[no] = (nivel, pai)
                for i in self.escolha.get_arestas(no):
                    pilha.append((i, no, nivel+1))
        return arvore