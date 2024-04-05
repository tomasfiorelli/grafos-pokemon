from collections import deque 

class Grafo:
    def __init__(self):
        # Dicionário para armazenar os vizinhos e pesos das arestas
        self.tipo_grafo = 6
        self.qtde_vertices = 0
        self.qtde_arestas = 0
        self.adj = {}

    def insereV(self, v):
        if v not in self.adj:
            self.adj[v] = {}
        self.qtde_vertices += 1
    
    def removeV(self, vertice):
        if vertice in self.adj:
            del self.adj[vertice]
            self.qtde_vertices -= 1
            for v in self.adj:  # Remove todas as arestas que envolvem o vértice
                if vertice in self.adj[v]:
                    del self.adj[v][vertice]
                    self.qtde_arestas -= 1
            print(f"Vértice '{vertice}' removido com sucesso e todas as suas arestas relacionadas.")
        else:
            print(f"O vértice '{vertice}' não existe no grafo.")

    def insereA(self, v, w, peso=1.0):
        if v not in self.adj:
            self.adj[v] = {}
        if w not in self.adj:
            self.adj[w] = {}
        self.adj[v][w] = peso
        self.qtde_arestas += 1

    def removeA(self, v, w):
        if v in self.adj and w in self.adj[v]:
            del self.adj[v][w]
        self.qtde_arestas -= 1

    def show(self):
        print("\nGRAFO [6] - grafo orientado com peso na aresta")
        print(f"Quantidade de vértices: {self.qtde_vertices}")
        print(f"Quantidade de arestas: {self.qtde_arestas}\n")
        for v, vizinhos in self.adj.items():
            print(f"{v[:3]}: ", end="")
            for vizinho, peso in vizinhos.items():
                print(f"[{vizinho[:3]}] = {peso}", end=" | ")
            print()
        print("\nFim da impressao do grafo.\n\n")

    def showMin(self):
        vertices = self.adj.keys()
        print("\n === MATRIZ DE ADJACÊNCIA ===")
        print(" " * 4, end="")
        for v in vertices:
            print(f"{v[:3]:^6}", end="")
        print()
        for v1 in vertices:
            print(f"{v1[:3]:<4}", end="")
            for v2 in vertices:
                if v2 in self.adj.get(v1, {}):
                    print(f"{self.adj[v1][v2]:^6.1f}", end="")
                else:
                    print(f"{'-':^6}", end="")
            print()
        print("\nFim da impressao da matriz de adjacência.\n\n")

    def lerArquivo(self, nome_arquivo):
        with open(nome_arquivo, 'r', encoding="utf-8") as arquivo:
            self.tipo_grafo = int(arquivo.readline())
            
            quantidade_vertices = int(arquivo.readline().strip())
            for _ in range(quantidade_vertices):
                self.insereV(arquivo.readline().strip())
            
            quantidade_arestas = int(arquivo.readline())
            for _ in range(quantidade_arestas):
                origem, destino, peso = arquivo.readline().split()
                peso_float = float(peso)
                self.insereA(origem, destino, peso_float)

    def salvarArquivo(self, nome_arquivo):
        with open(nome_arquivo, 'w', encoding="utf-8") as arquivo:
            # Escreve o tipo de grafo
            arquivo.write("6\n")

            # Escreve a quantidade de vértices
            arquivo.write(f"{len(self.adj)}\n")

            # Escreve os rótulos dos vértices
            for vertice in self.adj.keys():
                arquivo.write(f"{vertice}\n")

            # Escreve a quantidade de arestas
            total_arestas = sum(len(vizinhos) for vizinhos in self.adj.values())
            arquivo.write(f"{total_arestas}\n")

            # Escreve as arestas e pesos
            for vertice, vizinhos in self.adj.items():
                for vizinho, peso in vizinhos.items():
                    arquivo.write(f"{vertice} {vizinho} {peso}\n")

    def fconex(self):
        if not self.adj:
            print("Grafo vazio.")
            return

        # Verifica se o grafo é direcionado ou não
        direcionado = self._verificar_direcionado()

        if direcionado:
            # Grafo direcionado
            componentes = self._kosaraju()
            num_componentes = len(componentes)
            if num_componentes == 1:
                print("O grafo é fortemente conexo (C3).")
            elif num_componentes == 2:
                print("O grafo é semi-fortemente conexo (C2).")
            elif num_componentes > 2:
                print(f"O grafo possui {num_componentes} componente(s) fortemente conexa(s) (C3).")
            else:
                print("O grafo é desconexo (C0).")
            print("Apresentando o grafo reduzido:")
            self._apresentar_grafo_reduzido(componentes)
        else:
            # Grafo não direcionado
            visitados = set()
            fila = deque()
            vertice_inicial = next(iter(self.adj.keys()))  # Seleciona o primeiro vértice do grafo
            fila.append(vertice_inicial)
            visitados.add(vertice_inicial)

            while fila:
                vertice = fila.popleft()
                for vizinho in self.adj.get(vertice, {}):
                    if vizinho not in visitados:
                        fila.append(vizinho)
                        visitados.add(vizinho)

            if len(visitados) == len(self.adj):
                print("O grafo é simplesmente conexo (C1).")
            else:
                print("O grafo é desconexo (C0).")

    def _verificar_direcionado(self):
        for vertice, vizinhos in self.adj.items():
            for vizinho in vizinhos:
                if vertice not in self.adj[vizinho]:
                    return False  # Se não existe uma aresta de volta, é um grafo direcionado
        return True

    def _kosaraju(self):
        visitados = set()
        ordem_final = []
        for vertice in self.adj.keys():
            if vertice not in visitados:
                self._dfs(vertice, visitados, ordem_final)
        
        grafo_transposto = self._transpor_grafo()
        visitados.clear()
        componentes = []

        for vertice in reversed(ordem_final):
            componente = []
            if vertice not in visitados:
                self._dfs_transposto(vertice, visitados, componente, grafo_transposto)
                componentes.append(componente)

        return componentes

    def _dfs(self, vertice, visitados, ordem_final):
        visitados.add(vertice)
        for vizinho in self.adj.get(vertice, {}):
            if vizinho not in visitados:
                self._dfs(vizinho, visitados, ordem_final)
        ordem_final.append(vertice)

    def _transpor_grafo(self):
        grafo_transposto = Grafo()
        for vertice, vizinhos in self.adj.items():
            for vizinho in vizinhos:
                grafo_transposto.insereA(vizinho, vertice)
        return grafo_transposto

    def _dfs_transposto(self, vertice, visitados, componente, grafo_transposto):
        visitados.add(vertice)
        componente.append(vertice)
        for vizinho in grafo_transposto.adj.get(vertice, {}):
            if vizinho not in visitados:
                self._dfs_transposto(vizinho, visitados, componente, grafo_transposto)

    def _apresentar_grafo_reduzido(self, componentes):
        grafo_reduzido = Grafo()
        for componente in componentes:
            for vertice in componente:
                grafo_reduzido.qtde_vertices += 1
                for vizinho, peso in self.adj.get(vertice, {}).items():
                    if vizinho in componente:
                        grafo_reduzido.insereA(vertice, vizinho, peso)
        grafo_reduzido.show()