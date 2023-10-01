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
    
    def distancia (self, no1, no2):
        arvore = self.bfs(no1)
        if arvore[no2] is None:
            return None
        else:
            return arvore[no2][0]
        
    def diametro (self):
        big_diametro = 0
        for i in self.escolha.n_nodes():
            k = self.bfs(i)
            maior = max([no[0] for no in k if no is not None])
            if maior > big_diametro:
                big_diametro = maior
        return big_diametro
        