from representacao import ListaAdjacencia, MatrixAdjacencia
import json

class Grafo: # inicia o grafo #
    def __init__ (self, e_matrix, nome_arquivo):
        arquivo = open(nome_arquivo, "r") # lê o arquivo #
        n_nodes = arquivo.readline() # lê linha por linha #
        n_nodes = int(n_nodes) # lê a primeira linha como um número inteiro #
        arestas = []
        for linha in arquivo:
            strings = linha.split(" ")
            m = int(strings[0]) - 1
            n = int(strings[1]) - 1
            arestas.append((m, n))
        arquivo.close()
        graph = (n_nodes, arestas)
        if e_matrix: # inicia como matriz se for uma #
            self.escolha = MatrixAdjacencia (n_nodes, arestas)
        else: # inicia como lista de adjcencia se for uma #
            self.escolha = ListaAdjacencia (n_nodes, arestas)

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
        for i in range (0, self.escolha.n_nodes()):
            k = self.bfs(i)
            maior = max([no[0] for no in k if no is not None])
            if maior > big_diametro:
                big_diametro = maior
        return big_diametro
    
    def comp_conexas (self):
        visitados = []
        componentes = []
        n_componentes = 0
        while len(visitados) < self.escolha.n_nodes():
            for i in range (0, self.escolha.n_nodes()):
                if i not in visitados:
                    k = self.bfs(i)
                    break
            vert_comp = []
            index = 0
            for j in k:
                if j is not None:
                    vert_comp.append(index) 
                index += 1
            visitados = visitados + vert_comp
            componentes.append({ 
                "Numero de nos": len(vert_comp),
                "Nos": vert_comp
            })
            n_componentes += 1
        componentes.sort(reverse=True, key=lambda x:x["Numero de nos"])
        for componente in componentes:
            componente["Nos"] = [no + 1 for no in componente["Nos"]]
            
        return{
            "Numero de componentes": n_componentes,
            "Componentes": componentes
        }
    
    def saida (self):
        graus = []
        for i in range (0, self.escolha.n_nodes()):
            k = len(self.escolha.get_arestas(i))
            graus.append(k)
        graus.sort()
        text = {
            "Numero de vertices": self.escolha.n_nodes(),
            "Numero de arestas": self.escolha.n_arestas,
            "Grau minimo": min(graus),
            "Grau maximo": max(graus),
            "Grau medio": sum(graus)/(self.escolha.n_nodes()),
            "Mediana dos graus": graus[(len(graus)//2)],
            "Informacoes das componentes conexas": self.comp_conexas()
        }
        
        arquivo = open("saida.txt", "w")
        json.dump(text, arquivo)
        arquivo.close()

Grafo(True, "grafo_1.txt").saida()
