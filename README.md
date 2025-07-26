<div align="center" id="topo">

<img src="https://media.giphy.com/media/iIqmM5tTjmpOB9mpbn/giphy.gif" width="200px" alt="Gif animado"/>

# <code><strong> Simulador de Autômato Finito Determinístico (AFD)</strong></code>

<em>Trabalho da disciplina de Linguagens Formais e Autômatos para simular o funcionamento de um AFD.</em>

<!-- adicionar aqui o uso das linguagens que eu passar-->
[![Python Usage](https://img.shields.io/badge/Python-100%25-blue?style=for-the-badge&logo=python)]()
[![Status](https://img.shields.io/badge/Status-Concluído-green?style=for-the-badge)]()
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Visite%20meu%20perfil-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/rian-carlos-valcanaia-b2b487168/)

</div>


## Índice

- [📌 Objetivos](#-objetivos)
- [📥 Entradas do sistema](#-entradas-do-sistema)
- [🧱 Estruturas de Dados](#-estruturas-de-dados)
- [🧰 Funcionalidades](#-funcionalidades)
- [📊 Exemplo de Execução](#-exemplo-de-execução)
- [📂 Como executar](#-como-executar)
- [👨‍🏫 Envolvidos](#-envolvidos)
- [📅 Curso](#-curso)
- [📄 Código-fonte](#-código-fonte)

## 📌 Objetivos
* Implementar um simulador de Autômato Finito Determinístico (AFD) em Python.
* Criar uma classe que represente a 5-tupla de um AFD (alfabeto, estados, função programa, estado inicial e estados finais).
* Desenvolver uma função que processe uma cadeia de entrada (fita) e determine se ela é aceita ou rejeitada pelo autômato.
* Testar o simulador com um exemplo de AFD que reconhece palavras com o sufixo "abc".

[⬆ Voltar ao topo](#topo)

## 📥 Entradas do sistema
* O autômato e as fitas de teste são definidos diretamente no código-fonte (`simulador_AFD.py`).
* **Alfabeto**: Um conjunto de caracteres.
* **Estados**: Uma lista com os nomes dos estados.
* **Função Programa**: Um dicionário aninhado que representa a tabela de transição.
* **Estado Inicial**: Uma string que representa o estado inicial.
* **Estados Finais**: Uma lista de estados de aceitação.
* **Fitas de Teste**: Uma lista de strings a serem processadas pelo autômato.

[⬆ Voltar ao topo](#topo)

## 🧱 Estruturas de Dados
### 🔸 `AFD`
A classe `AFD` é a estrutura central do programa. Ela armazena os cinco componentes que definem um autômato finito determinístico e contém o método para simular seu comportamento. Seus atributos são: `alfabeto`, `estados`, `programa`, `estado_inicial` e `estados_finais`.

```python
class AFD:
    def __init__(self, alfa, estados, programa, estado_inicial, estados_finais):
        # Atributos
        self.alfabeto = alfa
        self.estados = estados
        self.programa = programa
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.tem_maquina = True

    # Método principal
    def aceita(self, fita): ...

```

[⬆ Voltar ao topo](#topo)

## 🧰 Funcionalidades

### 🔹 Funções Principais
* `__init__()`: Construtor da classe `AFD`, responsável por inicializar o autômato com a 5-tupla fornecida.
* `aceita(fita)`: Simula o processamento da fita. Começando do estado inicial, consome cada símbolo da fita e transita entre os estados de acordo com a função programa. Retorna `True` se a fita é aceita (termina em um estado final) e `False` caso contrário.

[⬆ Voltar ao topo](#topo)

## 📊 Exemplo de Execução
1. O script define um AFD que reconhece a linguagem de palavras terminadas em `abc`.
2. A definição completa do autômato (alfabeto, estados, tabela de transição) é impressa no console.
3. O programa então processa uma lista pré-definida de fitas de teste (`["aaaacb", "abcabc", "abccba", "aaaabc", "abcde"]`).
4. Para cada fita, o resultado da simulação é exibido, indicando se a palavra foi `Aceita` ou `Rejeita`.

[⬆ Voltar ao topo](#topo)

## 📂 Como executar
Para executar o simulador, use o seguinte comando em um terminal que tenha Python instalado:
```python
python simulador_AFD.py
```

[⬆ Voltar ao topo](#topo)

## 👨‍🏫 Envolvidos
* **Professor**: Ricardo Ferreira Martins
* **Estudantes**:
  * [Rian Valcanaia](https://github.com/RianValcanaia)

[⬆ Voltar ao topo](#topo)

## 📅 Curso

* **Universidade**: Universidade do Estado de Santa Catarina (UDESC)
* **Disciplina**: Linguagens Formais e Autômatos
* **Semestre**: 4º

[⬆ Voltar ao topo](#topo)

## 📄 Código-fonte

🔗 [https://github.com/RianValcanaia/LFA_Simulador_AFD](https://github.com/RianValcanaia/LFA_Simulador_AFD)

[⬆ Voltar ao topo](#topo)
