from representacao import ListaAdjacencia, MatrixAdjacencia
import json

class Grafo: # inicia o grafo #
    def __init__ (self, e_matrix, nome_arquivo):
        arquivo = open(nome_arquivo, "r") # lê o arquivo #
        n_nodes = arquivo.readline() # lê linha por linha #
        n_nodes = int(n_nodes) # lê a primeira linha como um número inteiro #
        arestas = [] #lista de arestas #
        for linha in arquivo: # quebra as linhas #
            strings = linha.split(" ")
            m = int(strings[0]) - 1
            n = int(strings[1]) - 1
            arestas.append((m, n)) # introduz a tupla na lista #
        arquivo.close() #fecha o arquivo #
        graph = (n_nodes, arestas) # uma tupla com o número de vértices e todas as arestas do grafo #
        if e_matrix: # inicia como matriz se for true #
            self.escolha = MatrixAdjacencia (n_nodes, arestas)
        else: # inicia como lista de adjcencia se for false #
            self.escolha = ListaAdjacencia (n_nodes, arestas)

    def bfs (self, node): # inicia a bfs #
        arvore = [None] * self.escolha.n_nodes() # cria a árvore e marca como não explorado #
        fila = [(node, None, 0)] # cria uma fila que tem o primeiro vértice, marcador não explorado e grau #
        while len(fila) > 0: # enquanto a fila não estiver vazia #
            (no, pai, nivel) = fila.pop(0) # tira o primeiro vértice da fila e coloca na árvore #
            if arvore[no] is None: # se o vértice não for explorado #   
                arvore[no] = (nivel, pai) # marca como explorado #
                for i in self.escolha.get_arestas(no): # procura as arestas do vértice #
                    fila.append((i, no, nivel+1)) # adiciona na fila os vértices descobertos e adiciona 1 no grau das arestas #
        return arvore # retorna a árvore geradora #

    def dfs (self, node): # inicia a dfs #
        arvore = [None] * self.escolha.n_nodes() # cria a árvore e marca como não explorado #
        pilha = [(node, None, 0)] # cria uma pilha que tem o primeiro vértice, marcador não explorado e grau #
        while len(pilha) > 0: # enquanto a pilha não estiver vazia #
            (no, pai, nivel) = pilha.pop() # tira o último vértice da pilha e coloca na árvore #
            if arvore[no] is None: # se o vértice não for explorado #   
                arvore[no] = (nivel, pai) # marca como explorado #
                for i in self.escolha.get_arestas(no): # procura as arestas do vértice #
                    pilha.append((i, no, nivel+1)) # adiciona na fila os vértices descobertos e adiciona 1 no grau das arestas #
        return arvore # retorna a árvore geradora #
    
    def distancia (self, no1, no2): # procura a distância entre 2 vértices #
        arvore = self.bfs(no1) # inicia a bfs começando pelo nó 1 #
        if arvore[no2] is None: # se não tiver conexão entre os vértices #
            return None # retorna que não há distância #
        else: # se houver conexão #
            return arvore[no2][0] # retorna o valor da distância #
        
    def diametro (self): # procura o diametro do grago #
        big_diametro = 0 # inicia a variável que guarda a maior distancia encontrada até o momento #
        for i in range (0, self.escolha.n_nodes()): # percorre todos os vértices #
            k = self.bfs(i) # inicia a variável que faz uma bfs no vértice atual #
            maior = max([no[0] for no in k if no is not None]) # procura o maior grau da bfs feita naquele vértice #
            if maior > big_diametro: # se o grau for maior que o grau guardado em big_diametro #
                big_diametro = maior # a variável recebe o novo maior grau #
        return big_diametro # retorna o valor do diametro #
    
    def comp_conexas (self): # procura todas as componentes conexas do grafo #
        visitados = [] # inicia a lista de vértices visitados #
        componentes = [] # inicia a lista com cada componente conexa #
        n_componentes = 0 # variavel para contar o número de componentes conexas #
        while len(visitados) < self.escolha.n_nodes(): # enquanto a quantidade de vértices visitados for menor que a quantidade de vértices do grafo # 
            for i in range (0, self.escolha.n_nodes()): # percorre todos os vértices #
                if i not in visitados: # se o vertice não foi visitado #
                    k = self.bfs(i) # é colocado na variavel todos os vertices encontrados na bfs #
                    break
            vert_comp = [] # inicia uma lista temporária com os vertices de k #
            index = 0 # contador de vértices #
            for j in k: # percorre os vértices em uma componente #
                if j is not None: # se o vertice não tiver sido explorado #
                    vert_comp.append(index) # adiciona o vertice na componente #
                index += 1 # o numero de vertices na componente é adicionado 1 #
            visitados = visitados + vert_comp # adiciona à lista os vertices da componente #
            componentes.append({ # escreve o resultado na variável #
                "Numero de nos": len(vert_comp), # numero de nós #
                "Nos": vert_comp # quais vértices estão na componente #
            })
            n_componentes += 1 # adiciona 1 ao número de componentes
        componentes.sort(reverse=True, key=lambda x:x["Numero de nos"]) # ordena as componentes por tamanho #
        for componente in componentes: # para cada componente na lista de componentes
            componente["Nos"] = [no + 1 for no in componente["Nos"]] # corretude da subtração da inicialização do grafo #
            
        return{ # retorna o resultado #
            "Numero de componentes": n_componentes, # número de componentes #
            "Componentes": componentes # lista de dicionários que são cada componente #
        }
    
    def saida (self): # saída do grafo #
        graus = [] # inicia uma lista com os graus dos vértices #
        for i in range (0, self.escolha.n_nodes()): # percorre os graus de cada vértice #
            k = len(self.escolha.get_arestas(i)) # guarda o número de arestas existentes no grafo #
            graus.append(k) # guarda o grau do vértice atual #
        graus.sort() # ordena os graus em ordem crescente #
        text = { # escreve a saída do grafo #
            "Numero de vertices": self.escolha.n_nodes(), #número de vértices #
            "Numero de arestas": self.escolha.n_arestas, # número de arestas #
            "Grau minimo": min(graus), # Grau mínimo #
            "Grau maximo": max(graus), # Grau máximo #
            "Grau medio": sum(graus)/(self.escolha.n_nodes()), # grau médio #
            "Mediana dos graus": graus[(len(graus)//2)], # mediana dos graus #
            "Informacoes das componentes conexas": self.comp_conexas() # resultado da função de componentes conexas #
        }
        
arquivo = open("saida.txt", "w") # cria um arquivo texto #
json.dump(text, arquivo) # escreve a saída do grafo no arquivo texto #
arquivo.close() # fecha o arquivo #
