# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:23:05 2023

@author: icalc
"""
from grafoMatriz import Grafo
from grafoMatriz import GrafoND

g = Grafo(4)
#insere as arestas do grafo
#A={(0,1),(0,2),(2,1),(2,3),(1,3)}
g.insereA(0,1)
g.insereA(0,2)
g.insereA(2,1)
g.insereA(2,3)
g.insereA(1,3)
# mostra o grafo preenchido
g.show()
g.showMin()

# --- EXERCÍCIO 1 ---
# Grau de entrada de um vértice
print("\n--- Exercício 1 ---")
for v in range(0, 4):
    print(f"Grau de entrada do vértice {v} -> {g.inDegree(v)}")

# --- EXERCÍCIO 2 ---
# Grau de saída de um vértice
print("\n--- Exercício 2 ---")
for v in range(0, 4):
    print(f"Grau de saída do vértice {v} -> {g.outDegree(v)}")

# --- EXERCÍCIO 3 ---
# Vértices fontes
print("\n--- Exercício 3 ---")
for v in range(0, 4):
    result = g.source(v)
    print(f"O vértice {v} {'é' if result == 1 else 'não é'} uma fonte ({result})")

# --- EXERCÍCIO 4 ---
# Vértices sorvedouros
print("\n--- Exercício 4 ---")
for v in range(0, 4):
    result = g.sink(v)
    print(f"O vértice {v} {'é' if result == 1 else 'não é'} um sorvedouro ({result})")

# --- EXERCÍCIO 5 ---
# Simetria do grafo
print("\n--- Exercício 5 ---")
result = g.isSymmetric()
print(f"O grafo abaixo {'é' if result == 1 else 'não é'} simétrico ({result})")
g.showMin()

# --- EXERCÍCIO 6 ---
# Leitura de arquivo
print("\n--- Exercício 6 ---")
fileGraph = Grafo.fromFile("C:\\Users\\tomas\\OneDrive - Instituto Presbiteriano Mackenzie\\6º Semestre [2024.1]\\Teoria dos Grafos\\Projetos\\Python\\grafo.txt")
# fileGraph.showMin()

# --- EXERCÍCIO 7 ---
print("\n--- Exercício 7 ---")
# gND = GrafoND(4)
# gND.insereA(0, 1)
# gND.insereA(0, 2)
# gND.insereA(2, 1)
# gND.insereA(2, 3)
# gND.insereA(1, 3)

# gND.show()
# gND.showMin()

# --- EXERCÍCIO 8 ---
print("\n--- Exercício 8 ---")
gND = GrafoND(4)
gND.insereA(0, 1, 3.5)
gND.insereA(1, 2, 2.0)
gND.insereA(2, 0, 1.0)
gND.insereA(2, 3, 4.7)

gND.show()
gND.showMin()