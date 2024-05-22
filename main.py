import os
import networkx as nx
import matplotlib.pyplot as plt
from grafo import Grafo

def menu():
    print(f"{' RELAÇÃO DOS TIPOS DE POKÉMON EM GRAFO ':=^50}\n")
    print("Selecione uma opção:")
    print("[1] Menu de edição")
    print("[2] Menu de análises")
    print("[0] Encerrar a aplicação")

def menu_editor():
    print(f"{' MENU DE EDIÇÃO ':=^50}\n")
    print("Selecione uma opção:")
    print("[1] Ler dados de arquivo")
    print("[2] Gravar dados nem arquivo")
    print("[3] Inserir vértice")
    print("[4] Inserir aresta")
    print("[5] Remover vértice")
    print("[6] Remover aresta")
    print("[7] Mostrar conteúdo do arquivo")
    print("[8] Mostrar grafo")
    print("[9] Apresentar a conexidade do grafo e o reduzido")
    print("[0] <- Voltar")

def menu_analises():
    print(f"{' MENU DE ANÁLISES ':=^50}\n")
    print("Selecione uma opção:")
    print("[1] Triângulos perfeitos")
    print("[2] Relações completas")
    print("[3] Grafos de Efetividade")
    print("[0] <- Voltar")

def main():
    grafo = Grafo()
    
    flag_externa = True
    flag_editor = False
    flag_analises = False
    
    while flag_externa:
        # impressão menu externo
        os.system('cls' if os.name == 'nt' else 'clear')
        menu()
        opcao_externa = input("\nOpção: ")
        
        if opcao_externa == "1":
            flag_editor = True
            
            while flag_editor:
                # impressão menu editor
                os.system('cls' if os.name == 'nt' else 'clear')
                menu_editor()
                opcao_editor = input("\nOpção: ")

                # 1
                if opcao_editor == "1":
                    arquivo = input("Digite o nome do arquivo: ")
                    try:
                        grafo.ler_arquivo(arquivo)
                        print(f"\nDados do arquivo {arquivo} lidos com sucesso.")
                    except:
                        print(f"[ERRO] Não foi possível realizar a leitura do arquivo {arquivo}.")
                
                # 2
                elif opcao_editor == "2":
                    arquivo = input("Digite o nome do arquivo: ")
                    try:
                        grafo.salvar_arquivo(arquivo)
                        print(f"Dados gravados no arquivo {arquivo} com sucesso.")
                    except:
                        print(f"Não foi possível gravar os dados no arquivo {arquivo}.")

                # 3
                elif opcao_editor == "3":
                    vertice = input("Digite o nome do vértice: ")
                    grafo.insere_vertice(vertice)
                    print(f"Vértice '{vertice}' inserido com sucesso.")
                    input("\nPressione [ENTER] para voltar")
                
                # 4
                elif opcao_editor == "4":
                    origem = input("Digite o vértice de origem: ")
                    destino = input("Digite o vértice de destino: ")
                    peso = float(input("Digite o peso da aresta: "))
                    grafo.insere_aresta(origem, destino, peso)
                    print(f"Aresta de '{origem}' para '{destino}' com peso {peso} inserida com sucesso.")
                
                # 5
                elif opcao_editor == "5":
                    vertice = input("Digite o nome do vértice a ser removido: ")
                    grafo.remove_vertice(vertice)
                
                # 6
                elif opcao_editor == "6":
                    origem = input("Digite o vértice de origem da aresta a ser removida: ")
                    destino = input("Digite o vértice de destino da aresta a ser removida: ")
                    grafo.remove_aresta(origem, destino)
                    print(f"Aresta de '{origem}' para '{destino}' removida com sucesso.")
                
                # 7
                elif opcao_editor == "7":
                    grafo.mostrar()
                
                # 8
                elif opcao_editor == "8":
                    grafo.mostrar_minimo()
                
                # 9
                elif opcao_editor == "9":
                    pass
                
                # 0
                elif opcao_editor == "0":
                    flag_editor = False

                # Default
                else:
                    print("Opção inválida. Por favor, selecione uma opção válida.")
                
                if opcao_editor != "0":
                    input("\nPressione [ENTER] para voltar")
        
        elif opcao_externa == "2":
            flag_analises = True

            while flag_analises:
            # impressão menu análises
                os.system('cls' if os.name == 'nt' else 'clear')
                menu_analises()
                opcao_analises = input("\nOpção: ")

                # 1
                if opcao_analises == "1":
                    grafo.triangulos()
                
                # 2
                elif opcao_analises == "2":
                    tipo: str = input("Digite o nome do vertice: ")
                    grafo.relacoes(tipo)
                
                # 3
                elif opcao_analises == "3":
                    nome_imagem = input("\nNome da imagem para salvar: ")
                    efetividade = 0
                    
                    while efetividade not in ['1', '2', '3', '4']:
                        print("Qual grafo de efetividade você quer gerar?")
                        print("[1] Super efetivo")
                        print("[2] Efetivo")
                        print("[3] Não efetivo")
                        print("[4] Sem efeito")
                        efetividade = input("\nOpção:")
                        if efetividade not in ['1', '2', '3', '4']:
                            print("Opção inválida.\n")
                    
                    if efetividade == '1':
                        grafo.gerar_imagem_grafo(nome_imagem, efetivo=False, nao_efetivo=False, sem_efeito=False)
                    elif efetividade == '2':
                        grafo.gerar_imagem_grafo(nome_imagem, super_efetivo=False, nao_efetivo=False, sem_efeito=False)
                    elif efetividade == '3':
                        grafo.gerar_imagem_grafo(nome_imagem, super_efetivo=False, efetivo=False, sem_efeito=False)
                    elif efetividade == '4':
                        grafo.gerar_imagem_grafo(nome_imagem, super_efetivo=False, efetivo=False, nao_efetivo=False)

                # 0
                elif opcao_analises == "0":
                    flag_analises = False

                # Default
                else:
                    print("Opção inválida. Por favor, selecione uma opção válida.")
                
                if opcao_analises != "0":
                    input("\nPressione [ENTER] para voltar")

        elif opcao_externa == "0":
            print("\nEncerrando a aplicação...")
            break

        # Default
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")
        
        if opcao_externa != "0" and opcao_editor != "0" and opcao_analises != "0":
            input("\nPressione [ENTER] para voltar")

if __name__ == "__main__":
    main()
