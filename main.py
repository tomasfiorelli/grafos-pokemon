from grafoMatriz import Grafo

def menu():
    opcao = -1
    
    while True:
        print("""\n=== ANÁLISE EM GRAFO DOS TIPOS DE POKÉMON ===\n
[1] Leitura do arquivo "grafo.txt"
[2] Gravação de dados em "grafo.txt"
[3] Inserir vértice
[4] Inserir aresta
[5] Remover vértice
[6] Remover aresta
[7] Mostrar conteúdo 
[8] Conexidade e grafo reduzido
[0] Encerrar""")
        
        opcao = input("\nOpção >> ")

        match opcao:
            case "1":
                # TODO
                fileGraph = Grafo.fromFile("grafo.txt")
                fileGraph.show()

            # case 2:
            #     # TODO 
                
            # case 3:
            #     # TODO 
                
            # case 4:
            #     # TODO 
                
            # case 5:
            #     # TODO 
                
            # case 6:
            #     # TODO 
                
            # case 7:
            #     # TODO 
                
            # case 8:
            #     # TODO
                
            case "0":
                print("Encerrando programa")
                break
            case _:
                # TODO default
                print("Opção inválida")
    
    

menu()