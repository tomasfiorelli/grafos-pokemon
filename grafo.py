# TEORIA DOS GRAFOS
# Projeto: Análise em Grafos dos Tipos de Pokémon

# Professor Ivan Carlos Alcântara de Oliveira

# RA: 10396285 | Raphael Iniesta Reis
# RA: 10395687 | Tomás Fiorelli Barbosa

class Grafo:
    # construtor da classe 'Grafo'
    def __init__(self) -> None:
        # tipo do grafo -> [6] Grafo Direcionado com Peso nas Arestas
        self.tipo_grafo: int = 6
        
        # número de vértices e arestas
        self.qtde_vertices: int = 0
        self.qtde_arestas: int = 0
        
        # matriz de adjacência
        self.matriz: dict[str, dict[str, float]] = {}

    # montagem do grafo a partir de um arquivo na mesma pasta
    def ler_arquivo(self, nome_arquivo: str) -> None:
        with open(nome_arquivo, 'r', encoding="utf-8") as arquivo:
            # verifica se tipo do grafo é suportado
            self.tipo_grafo = int(arquivo.readline())
            if self.tipo_grafo != 6:
                print(f'Grafo não suportado. Esperado: [6] | Obtido: [{self.tipo_grafo}]')
                print('\nLeia outro arquivo que possua suporte...')
                return None

            # leitura dos vértices
            quantidade_vertices = int(arquivo.readline().strip())
            for _ in range(quantidade_vertices):
                self.insere_vertice(arquivo.readline().strip())

            # leitura das arestas
            quantidade_arestas = int(arquivo.readline())
            for _ in range(quantidade_arestas):
                origem, destino, peso = arquivo.readline().split()
                peso_float = float(peso)
                self.insere_aresta(origem, destino, peso_float)

    def salvar_arquivo(self, nome_arquivo: str):
        # o nome do arquivo é contemplado apenas na pasta base
        with open(nome_arquivo, 'w', encoding="utf-8") as arquivo:
            # tipo do grafo
            arquivo.write("6\n")

            # quantidade de vertices e seus respectivos rótulos
            arquivo.write(f"{len(self.matriz)}\n")
            
            for vertice in self.matriz.keys():
                arquivo.write(f"{vertice}\n")

            # quantidade de arestas e suas formações
            total_arestas = sum(len(vizinhos) for vizinhos in self.matriz.values())
            arquivo.write(f"{total_arestas}\n")

            for vertice, vizinhos in self.matriz.items():
                for vizinho, peso in vizinhos.items():
                    arquivo.write(f"{vertice} {vizinho} {peso}\n")

    # inserção de vértices
    def insere_vertice(self, vertice: str) -> None:
        if vertice not in self.matriz:
            self.matriz[vertice] = {}
            self.qtde_vertices += 1
            print(f'"{vertice}" foi adicionado na lista!')
        else:
            print(f'"{vertice}" já estava na lista.')
    
    # remoção de vértices
    def remove_vertice(self, vertice: str) -> None:
        if vertice in self.matriz:
            # remoção do vértice
            del self.matriz[vertice]
            self.qtde_vertices -= 1
            # remoção de todas as arestas que conectavam no vértice
            for v in self.matriz:
                if vertice in self.matriz[v]:
                    del self.matriz[v][vertice]
                    self.qtde_arestas -= 1
            print(f'"{vertice}" foi removido!')
        else:
            print(f'"{vertice}" não existe na lista.')
        
    # inserção de arestas
    def insere_aresta(self, origem: str, destino: str, peso: float) -> None:
        # 'if's adicionados para menos impressão da linha 51
        if origem not in self.matriz.keys():
            self.insere_vertice(origem)
        if destino not in self.matriz.keys():
            self.insere_vertice(destino)
        
        # texto para formatação
        verbo: str = 'adicionado' if destino not in self.matriz[origem].keys() else 'modificado'
        
        self.matriz[origem][destino] = peso
        self.qtde_arestas += 1
        
        print(f'{origem}: [{destino} -> {peso}] foi {verbo}!')

    # remoção de arestas
    def remove_aresta(self, origem: str, destino: str) -> None: 
        if origem in self.matriz and destino in self.matriz[origem]:
            # obter o peso para formatação da resposta
            peso = self.matriz[origem][destino]
            
            del self.matriz[origem][destino]
            self.qtde_arestas -= 1
            print(f'{origem}: [{destino} -> {peso}] foi removido!')
        else:
            print(f'Não foi possível encontrar "{origem}" e/ou "{destino}".')

    def mostrar(self) -> None:
        # impressão título e dados 
        print(f"\n{' Grafo Completo ':=^30}")
        print(f"Quantidade de vértices: {self.qtde_vertices}")
        print(f"Quantidade de arestas: {self.qtde_arestas}\n")
        
        for v, vizinhos in self.matriz.items():
            print(f"{v[:3]}: ", end="")
            for vizinho, peso in vizinhos.items():
                print(f"{vizinho[:3]} = {peso}", end=" | ")
            print()
        print("\nFim da impressão do grafo completo")

    def mostrar_minimo(self) -> None:
        # impressão título e dados 
        print(f"\n{' Grafo Mínimo ':=^30}")
        print(f"Quantidade de vértices: {self.qtde_vertices}")
        print(f"Quantidade de arestas: {self.qtde_arestas}\n")
        
        vertices = self.matriz.keys()
        print(" " * 4, end="")
        for v in vertices:
            print(f"{v[:3]:^6}", end="")
        print()
        for v1 in vertices:
            print(f"{v1[:3]:<4}", end="")
            for v2 in vertices:
                if v2 in self.matriz.get(v1, {}):
                    print(f"{self.matriz[v1][v2]:^6.1f}", end="")
                else:
                    print(f"{'-':^6}", end="")
            print()
        print("\nFim da impressao do grafo mínimo")



#     def salvarArquivo(self, nome_arquivo):
#         with open(nome_arquivo, 'w', encoding="utf-8") as arquivo:
#             # Escreve o tipo de grafo
#             arquivo.write("6\n")

#             # Escreve a quantidade de vértices
#             arquivo.write(f"{len(self.adj)}\n")

#             # Escreve os rótulos dos vértices
#             for vertice in self.adj.keys():
#                 arquivo.write(f"{vertice}\n")

#             # Escreve a quantidade de arestas
#             total_arestas = sum(len(vizinhos) for vizinhos in self.adj.values())
#             arquivo.write(f"{total_arestas}\n")

#             # Escreve as arestas e pesos
#             for vertice, vizinhos in self.adj.items():
#                 for vizinho, peso in vizinhos.items():
#                     arquivo.write(f"{vertice} {vizinho} {peso}\n")

#     def fconex(self):
#         if not self.adj:
#             print("Grafo vazio.")
#             return

#         # Verifica se o grafo é direcionado ou não
#         direcionado = self._verificar_direcionado()

#         if direcionado:
#             # Grafo direcionado
#             componentes = self._kosaraju()
#             num_componentes = len(componentes)
#             if num_componentes == 1:
#                 print("O grafo é fortemente conexo (C3).")
#             elif num_componentes == 2:
#                 print("O grafo é semi-fortemente conexo (C2).")
#             elif num_componentes > 2:
#                 print(f"O grafo possui {num_componentes} componente(s) fortemente conexa(s) (C3).")
#             else:
#                 print("O grafo é desconexo (C0).")
#             print("Apresentando o grafo reduzido:")
#             self._apresentar_grafo_reduzido(componentes)
#         else:
#             # Grafo não direcionado
#             visitados = set()
#             fila = deque()
#             vertice_inicial = next(iter(self.adj.keys()))  # Seleciona o primeiro vértice do grafo
#             fila.append(vertice_inicial)
#             visitados.add(vertice_inicial)

#             while fila:
#                 vertice = fila.popleft()
#                 for vizinho in self.adj.get(vertice, {}):
#                     if vizinho not in visitados:
#                         fila.append(vizinho)
#                         visitados.add(vizinho)

#             if len(visitados) == len(self.adj):
#                 print("O grafo é simplesmente conexo (C1).")
#             else:
#                 print("O grafo é desconexo (C0).")

#     def _verificar_direcionado(self):
#         for vertice, vizinhos in self.adj.items():
#             for vizinho in vizinhos:
#                 if vertice not in self.adj[vizinho]:
#                     return False  # Se não existe uma aresta de volta, é um grafo direcionado
#         return True

#     def _kosaraju(self):
#         visitados = set()
#         ordem_final = []
#         for vertice in self.adj.keys():
#             if vertice not in visitados:
#                 self._dfs(vertice, visitados, ordem_final)
        
#         grafo_transposto = self._transpor_grafo()
#         visitados.clear()
#         componentes = []

#         for vertice in reversed(ordem_final):
#             componente = []
#             if vertice not in visitados:
#                 self._dfs_transposto(vertice, visitados, componente, grafo_transposto)
#                 componentes.append(componente)

#         return componentes

#     def _dfs(self, vertice, visitados, ordem_final):
#         visitados.add(vertice)
#         for vizinho in self.adj.get(vertice, {}):
#             if vizinho not in visitados:
#                 self._dfs(vizinho, visitados, ordem_final)
#         ordem_final.append(vertice)

#     def _transpor_grafo(self):
#         grafo_transposto = Grafo()
#         for vertice, vizinhos in self.adj.items():
#             for vizinho in vizinhos:
#                 grafo_transposto.insereA(vizinho, vertice)
#         return grafo_transposto

#     def _dfs_transposto(self, vertice, visitados, componente, grafo_transposto):
#         visitados.add(vertice)
#         componente.append(vertice)
#         for vizinho in grafo_transposto.adj.get(vertice, {}):
#             if vizinho not in visitados:
#                 self._dfs_transposto(vizinho, visitados, componente, grafo_transposto)

#     def _apresentar_grafo_reduzido(self, componentes):
#         grafo_reduzido = Grafo()
#         for componente in componentes:
#             for vertice in componente:
#                 grafo_reduzido.qtde_vertices += 1
#                 for vizinho, peso in self.adj.get(vertice, {}).items():
#                     if vizinho in componente:
#                         grafo_reduzido.insereA(vertice, vizinho, peso)
#         grafo_reduzido.show()