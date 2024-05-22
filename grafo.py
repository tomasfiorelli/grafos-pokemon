# TEORIA DOS GRAFOS
# Projeto: Análise em Grafos dos Tipos de Pokémon

# Professor Ivan Carlos Alcântara de Oliveira

# RA: 10396285 | Raphael Iniesta Reis
# RA: 10395687 | Tomás Fiorelli Barbosa

import networkx as nx
import matplotlib.pyplot as plt

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

    # -------

    # Parte 2
    def triangulos(self):
        # relações de um triângulo perfeito
        # TIPO_1 TIPO_2: 2.0
        # TIPO_2 TIPO_3: 2.0
        # TIPO_3 TIPO_1: 2.0
        # TIPO_2 TIPO_1: 0.5
        # TIPO_3 TIPO_2: 0.5
        # TIPO_1 TIPO_3: 0.5

        triangulos = []
        vertices = list(self.matriz.keys())
        for i in range(len(vertices)):
            for j in range(len(vertices)):
                for k in range(len(vertices)):
                    v1 = vertices[i]
                    v2 = vertices[j]
                    v3 = vertices[k]

                    if v1 == v2 or v1 == v3 or v2 == v3:
                        continue

                    # Verifica relações
                    if (self.matriz[v1][v2] == 2.0 and
                        self.matriz[v2][v3] == 2.0 and
                        self.matriz[v3][v1] == 2.0 and
                        self.matriz[v2][v1] == 0.5 and
                        self.matriz[v3][v2] == 0.5 and
                        self.matriz[v1][v3] == 0.5):
                        # adiciona e ordena caso seja adicionado um
                        # trio já existente e que esteja deslocado 
                        triangulos.append(tuple(sorted((v1, v2, v3))))

        # remove trios repetidos
        triangulos = set(triangulos)

        print(f"\n{' Triângulos ':=^25}")
        if triangulos:
            for triangulo in triangulos:
                print(f"{triangulo[0]} >> {triangulo[1]} >> {triangulo[2]}")
        else:
            print("Nenhum triângulo encontrado.")
        print(f"{' ':=^25}")

    def relacoes(self, vertice: str):
        # relações de ataque
        # forte (relação 2.0 | vertice -> outros)
        # fraco (relação 0.5 | vertice -> outros)
        # não afeta (relação 0.0 | vertice -> outros)

        # relações de defesa
        # Resistente (relação 0.5 | outros -> vertice)
        # vulnerável (relação 2.0 | outros -> vertice)
        # imune (relação 0.0 | outros -> vertice)

        if vertice not in self.matriz:
            print(f'O vértice "{vertice}" não existe no grafo.')
            return

        forte_contra = []
        fraco_contra = []
        nao_afeta = []

        resistente = []
        vulneravel = []
        imune = []

        for destino in self.matriz[vertice].keys():
            if self.matriz[vertice][destino] == 2.0:
                forte_contra.append(destino)
            elif self.matriz[vertice][destino] == 0.5:
                fraco_contra.append(destino)
            elif self.matriz[vertice][destino] == 0.0:
                nao_afeta.append(destino)
            
        for origem in self.matriz.keys():
            if origem == vertice:
                continue

            if self.matriz[origem][vertice] == 0.5:
                resistente.append(origem)
            elif self.matriz[origem][vertice] == 2.0:
                vulneravel.append(origem)
            elif self.matriz[origem][vertice] == 0.0:
                imune.append(origem)

        print(f"\n{' Relações de ' + vertice + ' ':=^45}")
        print(f"{vertice} -> atacando")
        print(f"- Forte contra:\t {', '.join(forte_contra) or '---'}")
        print(f"- Fraco contra:\t {', '.join(fraco_contra) or '---'}")
        print(f"- Não afeta:\t {', '.join(nao_afeta) or '---'}")
        print(f"\n{vertice} -> defendendo")
        print(f"- Resistente a:\t {', '.join(resistente) or '---'}")
        print(f"- Vulnerável a:\t {', '.join(vulneravel) or '---'}")
        print(f"- Imune a:\t {', '.join(imune) or '---'}")

    def gerar_imagem_grafo(self, nome_arquivo: str,
                           super_efetivo=True,
                           efetivo=True,
                           nao_efetivo=True,
                           sem_efeito=True):

        grafo = nx.DiGraph()

        for vertice in self.matriz.keys():
            grafo.add_node(vertice)

        # atribuicao de cores
        for origem, vizinhos in self.matriz.items():
            for destino, peso in vizinhos.items():
                if peso == 2.0 and super_efetivo:
                    cor = 'green'
                    grafo.add_edge(origem, destino, color=cor)
                elif peso == 1.0 and efetivo:
                    cor = 'black'
                    grafo.add_edge(origem, destino, color=cor)
                elif peso == 0.5 and nao_efetivo:
                    cor = 'red'
                    grafo.add_edge(origem, destino, color=cor)
                elif peso == 0.0 and sem_efeito:
                    cor = 'purple'
                    grafo.add_edge(origem, destino, color=cor)

        pos = nx.circular_layout(grafo)

        nx.draw(grafo, pos, with_labels=True, node_color='lightblue', font_size=8,
                font_weight='bold', node_size=500, edge_color=[data['color'] for (u, v, data) in grafo.edges(data=True)],
                # Define o formato dos nodos como retângulos com bordas arredondadas
                node_shape='o')
                # # Define o arredondamento das bordas do quadrado
                # node_border_roundness=0.5)
        
        plt.title("Grafo de Tipos de Pokémon")
        plt.tight_layout()

        plt.savefig(nome_arquivo)
        plt.close()
        print(f'A imagem do grafo foi salva em {nome_arquivo}.')