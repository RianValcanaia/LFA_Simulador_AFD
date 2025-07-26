class AFD:
    def __init__(self, alfa, estados, programa, estado_inicial, estados_finais):
        self.alfabeto = alfa
        self.estados = estados
        self.programa = programa
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.tem_maquina = True
    
    def aceita(self, fita):
        if self.tem_maquina == True:
            estado_atual = self.estado_inicial
            try: 
                for simbolo in fita:
                    estado_atual = self.programa[estado_atual][simbolo]

                if estado_atual in self.estados_finais:
                    return True
                else:
                    return False
            except KeyError:
                print(f"\tTransição inválida: símbolo ou estado não encontrado na palavra {fita}")
                return False
        else:
            print("Adicione uma AFD!")


if __name__ == "__main__":
    print("Definindo AFD:")
    print("\tCaso exemplo: aceita palavras com sufixo abc")
    
    print("\tAlfabeto: {a, b, c}")
    alfabeto = "abc"

    print("\tConjunto de estados: {q0, q1, q2, q3}")
    estados = ["q0","q1","q2","q3"]

    print("\tFunção Programa:")
    print("\t\t|    |  a   |  b   |  c")
    print("\t\t| q0 |  q1  |  q0  |  q0")
    print("\t\t| q1 |  q1  |  q2  |  q0")
    print("\t\t| q2 |  q1  |  q0  |  q3")
    print("\t\t| q3 |  q1  |  q2  |  q0")
    programa = {
        'q0': {'a': 'q1', 'b': 'q0', 'c': 'q0'},
        'q1': {'a': 'q1', 'b': 'q2', 'c': 'q0'},
        'q2': {'a': 'q1', 'b': 'q0', 'c': 'q3'},
        'q3': {'a': 'q1', 'b': 'q2', 'c': 'q0'}
    }

    print("\tEstado inicial = q0")    
    estado_inicial = "q0"
    
    print("\tConjunto de estados finais: {q3}")
    estados_finais = ["q3"]

    # iniciando AFD
    automato = AFD(alfabeto, estados, programa, estado_inicial, estados_finais)

    # testes
    print("\n Testes:")
    testes = ["aaaacb", "abcabc", "abccba", "aaaabc", "abcde"]

    for tt in testes:
        if automato.aceita(tt):
            print(f"\tAceita palavra {tt}")
        else:
            print(f"\tRejeita palavra {tt}")

