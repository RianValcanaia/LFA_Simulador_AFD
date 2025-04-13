'''
caso de teste -> aceita palavras com sufixo abc
Q = ["q0","q1", "q2", "q3"]
alfabeto = "abc"
programa = {
    'q0': {'a': 'q1', 'b': 'q0', 'c': 'q0'},
    'q1': {'a': 'q1', 'b': 'q2', 'c': 'q0'},
    'q2': {'a': 'q1', 'b': 'q0', 'c': 'q3'},
    'q3': {'a': 'q1', 'b': 'q2', 'c': 'q0'}
}
estado_inicial = "q0"
F = ["q3"]

q0 q1 q2 q3
abc
q0 a q1
q0 b q0
q0 c q0
q1 a q1 
q1 b q2
q1 c q0
q2 a q1
q2 b q0
q2 c q3
q3 a q1
q3 b q2
q3 c q0
.
q0
q3
'''
def limpa_tela():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# ENTRADA
continuar = True
tem_maquina = False

while(continuar):
    limpa_tela()
    print("1 - Adicionar AFD")
    print("2 - Rodar palavra")
    print("3 - Sair")

    opcao = input("Digite uma opcao: ")

    limpa_tela()
    if opcao == '1':
        # ADICIONA UMA MAQUINA
        linha = input("Digite os estados separando por espacos (ex: q0 q1 q2 ...):\n")
        Q = linha.split()
        
        alfabeto = input("Digite o alfabeto, em string sem espacos: \n")

        print("Digite a funcao programa (ex q0 a q1), '.' para terminar:")
        programa = {}
        linha = input() 
        while (linha != '.'):
            estado_origem, simbolo, estado_destino = linha.split()
        
            if estado_origem not in programa:
                programa[estado_origem] = {}
        
            programa[estado_origem][simbolo] = estado_destino

            linha = input()

        estado_inicial = input("Digite o estado inicial: \n")
        
        linha = input("Digite os estados finais separando por espacos (ex: q0 q1 q2 ...):\n") 
        F = linha.split()
        
        tem_maquina = True
    elif opcao == '2':
        # testa palavras
        if tem_maquina:
            fita = input("Digite a palavra: ")

            estado_atual = estado_inicial
            try: 
                for simbolo in fita:
                    estado_atual = programa[estado_atual][simbolo]

                if estado_atual in F:
                    print("\nPalavra aceita na linguagem definida pelo AFD!")
                else:
                    print("\nPalavra não aceita na linguagem!")
            except KeyError:
                print("Transição inválida: símbolo ou estado não encontrado.")
        else:
            print("Adicione uma AFD!")
        
        input("\nPressione enter para continuar...")
    elif opcao == '3':
        # SAIR
        continuar = False
    else:
        limpa_tela()