# Guia de Referência Rápida: Funções em Python (Módulo 4)

Este módulo aborda a criação de código reutilizável, escopo de variáveis, programação funcional (map/filter) e recursão.

## 1. Dicionário de Sintaxe
Novas palavras-chave e funções *built-in* apresentadas para manipulação de funções.

| Comando/Keyword | O que faz | Exemplo de uso curto |
| :--- | :--- | :--- |
| `def` | Define uma nova função. | `def minha_funcao():` |
| `return` | Encerra a função e devolve um valor ao chamador. Se omitido, retorna `None`. | `return x + y` |
| `global` | Permite alterar uma variável do escopo global dentro de uma função local. | `global contador` |
| `nonlocal` | Permite alterar uma variável de um escopo "pai" (em funções aninhadas). | `nonlocal x` |
| `lambda` | Cria uma função anônima (sem nome) de uma linha só. | `lambda x: x * 2` |
| `map()` | Aplica uma função a **todos** os itens de um iterável (retorna um iterador). | `map(funcao, lista)` |
| `filter()` | Filtra itens de um iterável baseando-se em uma função que retorna True/False. | `filter(teste_logico, lista)` |
| `help()` | Exibe a *docstring* (documentação) de uma função definida pelo usuário. | `help(minha_funcao)` |

---

## 2. Operadores, Símbolos e Regras Especiais

### Símbolos de Argumentos e Parâmetros
| Símbolo | Nome | Função no Contexto de Funções |
| :--- | :--- | :--- |
| `*` | Asterisco (Splat) | Define **Argumentos Posicionais Variáveis**. Recebe múltiplos itens como uma **Tupla**. Ex: `def func(*args):` |
| `**` | Duplo Asterisco | Define **Argumentos Nomeados Variáveis**. Recebe pares chave=valor como um **Dicionário**. Ex: `def func(**kwargs):` |
| `"""` | Docstring | String literal logo após o `def` usada para documentação. Acessível via `help()`. |
| `=` | Valor Padrão | Define um valor *default* para um parâmetro caso ele não seja passado. Ex: `def func(cor="azul"):` |

### Regras de Escopo (Scope)
Python busca variáveis na seguinte ordem (LEGB):
1.  **L**ocal (dentro da função).
2.  **E**nclosing (função pai, se houver aninhamento).
3.  **G**lobal (nível do módulo).
4.  **B**uilt-in (sistema do Python).

### Passagem de Parâmetros (Mutabilidade)
*   **Tipos Imutáveis (int, str, tuple):** Passados por valor. Alterar dentro da função **não** muda fora.
*   **Tipos Mutáveis (list, dict):** Passados por referência. Alterar a lista dentro da função (ex: `append`) **altera** a lista original fora da função.

---

## 3. Estrutura de Código

### Definição Básica e Argumentos Opcionais
```python
def nome_funcao(parametro_1, opcional=10):
    """
    Esta é a docstring explicando a função.
    """
    resultado = parametro_1 * opcional
    return resultado
Argumentos Variáveis (*args e **kwargs)
Use para aceitar qualquer quantidade de dados.
def super_funcao(primeiro, *args, **kwargs):
    print(primeiro) # Argumento obrigatório
    print(args)     # Tupla com os extras posicionais (1, 2, 3)
    print(kwargs)   # Dicionário com extras nomeados {'cor': 'red'}
Funções Anônimas (Lambda)
Estrutura concisa para funções simples, usada frequentemente dentro de map ou filter.
# Sintaxe: lambda parametros: expressao_retorno
dobro = lambda x: x * 2
Recursão
Função que chama a si mesma. Exige uma condição de parada para evitar loop infinito.
def fatorial(n):
    if n == 1:          # Condição de parada (Base case)
        return 1
    else:
        return n * fatorial(n - 1) # Chamada recursiva

--------------------------------------------------------------------------------
4. Checklist de Aplicação
Use esta lista para decidir qual técnica do Capítulo 4 aplicar:
• Precisa processar/transformar todos os itens de uma lista (ex: converter tudo para int)?
    ◦ Use map(funcao, lista).
• Precisa selecionar apenas alguns itens de uma lista (ex: apenas números pares)?
    ◦ Use filter(funcao_teste, lista).
• A função precisa modificar uma variável que está fora dela?
    ◦ Declare a variável como global (ou nonlocal se estiver aninhada) dentro da função antes de usá-la.
• Precisa de uma função rápida para usar dentro de um sort ou map sem defini-la com def?
    ◦ Use uma lambda.
• Não sabe quantos argumentos o usuário vai enviar?
    ◦ Use *args para listas de valores ou **kwargs para configurações nomeadas.
• Quer evitar que o código quebre se o usuário esquecer um argumento?
    ◦ Use valores padrão na definição: def func(x=0):.
• A função deve alterar uma lista original passada para ela?
    ◦ Sim, métodos como .append() dentro da função afetarão a lista original (passagem por referência).
• A função deve resolver um problema dividindo-o em subproblemas menores iguais?
    ◦ Considere usar Recursão, mas lembre-se sempre de definir a condição de parada (if) no início.