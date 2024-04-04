# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:59:10 2023

@author: icalc
"""
class Grafo:
    TAM_MAX_DEFAULT = 100 # qtde de vértices máxima default
    # construtor da classe grafo
    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n # número de vértices
        self.m = 0 # número de arestas
        # matriz de adjacência
        self.adj = [[0 for i in range(n)] for j in range(n)]

    # Insere uma aresta no Grafo tal que
    # v é adjacente a w
    def insereA(self, v, w):
        if self.adj[v][w] == 0:
            self.adj[v][w] = 1
            self.m+=1 # atualiza qtd arestas
    
    # remove uma aresta v->w do Grafo	
    def removeA(self, v, w):
        # testa se temos a aresta
        if self.adj[v][w] == 1:
            self.adj[v][w] = 0
            self.m-=1; # atualiza qtd arestas

    # Apresenta o Grafo contendo
    # número de vértices, arestas
    # e a matriz de adjacência obtida	
    def show(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] == 1:
                    print(f"Adj[{i:2d},{w:2d}] = 1 ", end="") 
                else:
                    print(f"Adj[{i:2d},{w:2d}] = 0 ", end="")
            print("\n")
        print("fim da impressao do grafo." )

    # Apresenta o Grafo contendo
    # número de vértices, arestas
    # e a matriz de adjacência obtida 
    # Apresentando apenas os valores 0 ou 1	
    def showMin(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] == 1:
                    print(" 1 ", end="") 
                else:
                    print(" 0 ", end="")
            print("\n")
        print("fim da impressao do grafo." )
    
    # --- EXERCÍCIO 1 ---
    # Função que retorna o grau
    # de entrada de um vértice v,
    # total de arestas que chegam
    def inDegree(self, v):
        in_degree = 0
        for i in range(self.n):
            in_degree += self.adj[i][v]
        return in_degree

    # --- EXERCÍCIO 2 ---
    # Função que retorna o grau
    # de entrada de um vértice v,
    # total de arestas que saem
    def outDegree(self, v):
        out_degree = 0
        for j in range(self.n):
            out_degree += self.adj[v][j]
        return out_degree

    # --- EXERCÍCIO 3 ---
    # Função que retorna se
    # o vértice v é fonte
    def source(self, v):
        return 1 if (self.outDegree(v) > 0 and self.inDegree(v) == 0) else 0 

    # --- EXERCÍCIO 4 ---
    # Função que retorna se
    # o vértice v é sorvedouro
    def sink(self, v):
        return 1 if (self.inDegree(v) > 0 and self.outDegree(v) == 0) else 0 
    
    # --- EXERCÍCIO 5 ---
    # Função que retorna se
    # o grafo g é simétrico
    def isSymmetric(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.adj[i][j] != self.adj[j][i]:
                    return 0
        return 1
    
    # --- EXERCÍCIO 6 ---
    # Leitura do grafo no
    # arquivo gerado
    @classmethod
    def fromFile(cls, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                num_vertices = int(lines[0].strip())
                num_edges = int(lines[1].strip())
                graph = cls(num_vertices)
                for line in lines[2:]:
                    v, w = map(int, line.split())
                    graph.insereA(v, w)
            print(f"Leitura do arquivo: <{filename}>")
            # graph.showMin()
            return graph
        except:
            print(f"Falha na leitura do arquivo: <{filename}>")
            return None

# Grafo Não-Direcionado
class GrafoND:
    TAM_MAX_DEFAULT = 100
    
    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n 
        self.m = 0 
        self.adj = [[0.0 for i in range(n)] for j in range(n)]

    def insereA(self, v, w, valor):
        if self.adj[v][w] == 0 and self.adj[w][v] == 0: 
            self.adj[v][w] = valor
            self.adj[w][v] = valor 
            self.m += 1 
    
    def removeA(self, v, w):
        if self.adj[v][w] != 0 and self.adj[w][v] != 0: 
            self.adj[v][w] = 0
            self.adj[w][v] = 0 
            self.m -= 1 
    
    def show(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                print(f"Adj[{i:2d},{w:2d}] = {self.adj[i][w]} ", end="")
            print("\n")
        print("fim da impressao do grafo." )
    
    def showMin(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] != 0:
                    print(" 1 ", end="")
                else:
                    print(" 0 ", end="")
            print("\n")
        print("fim da impressao do grafo." )