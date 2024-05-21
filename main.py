import os
from grafo import Grafo

def menu():
    print("=== RELAÇÃO DOS TIPOS DE POKÉMON EM GRAFO ===\n")
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
    print("[0] Encerrar a aplicação")

def main():
    grafo = Grafo()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        menu()
        opcao = input("\nOpção: ")
        
        # 1
        if opcao == "1":
            arquivo = input("Digite o nome do arquivo: ")
            try:
                grafo.ler_arquivo(arquivo)
                print(f"\nDados do arquivo {arquivo} lidos com sucesso.")
            except:
                print(f"[ERRO] Não foi possível realizar a leitura do arquivo {arquivo}.")
        
        # 2
        elif opcao == "2":
            arquivo = input("Digite o nome do arquivo: ")
            try:
                grafo.salvar_arquivo(arquivo)
                print(f"Dados gravados no arquivo {arquivo} com sucesso.")
            except:
                print(f"Não foi possível gravar os dados no arquivo {arquivo}.")

        # 3
        elif opcao == "3":
            vertice = input("Digite o nome do vértice: ")
            grafo.insere_vertice(vertice)
            print(f"Vértice '{vertice}' inserido com sucesso.")
            input("\nPressione [ENTER] para voltar")
        
        # 4
        elif opcao == "4":
            origem = input("Digite o vértice de origem: ")
            destino = input("Digite o vértice de destino: ")
            peso = float(input("Digite o peso da aresta: "))
            grafo.insere_aresta(origem, destino, peso)
            print(f"Aresta de '{origem}' para '{destino}' com peso {peso} inserida com sucesso.")
        
        # 5
        elif opcao == "5":
            vertice = input("Digite o nome do vértice a ser removido: ")
            grafo.remove_vertice(vertice)
        
        # 6
        elif opcao == "6":
            origem = input("Digite o vértice de origem da aresta a ser removida: ")
            destino = input("Digite o vértice de destino da aresta a ser removida: ")
            grafo.remove_aresta(origem, destino)
            print(f"Aresta de '{origem}' para '{destino}' removida com sucesso.")
        
        # 7
        elif opcao == "7":
            grafo.mostrar()
        
        # 8
        elif opcao == "8":
            grafo.mostrar_minimo()
        
        # 9
        elif opcao == "9":
            grafo.fconex()
        
        # 0
        elif opcao == "0":
            print("\nEncerrando a aplicação...")
            break
        
        # DEFAULT
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")
        
        input("\nPressione [ENTER] para voltar")

if __name__ == "__main__":
    main()
