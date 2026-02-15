# Guia de Referência Rápida: Componentes da Linguagem (Capítulo 2)

Este módulo foca no controle de fluxo (decisões e loops), identação e lógica booleana.

## 1. Dicionário de Sintaxe
Palavras-chave e funções essenciais introduzidas para controle de fluxo e iteração.

| Comando/Keyword | O que faz | Exemplo de uso curto |
| :--- | :--- | :--- |
| `if` | Inicia uma estrutura de decisão. Executa o bloco se a condição for `True`. | `if x > 10: print("Maior")` |
| `elif` | "Else If". Testa uma nova condição se o `if` anterior for `False`. | `elif x == 10: print("Igual")` |
| `else` | Executa um bloco caso todas as condições anteriores (`if`/`elif`) sejam falsas. | `else: print("Menor")` |
| `while` | Cria um loop que repete *enquanto* a condição for verdadeira. | `while x < 10: x += 1` |
| `for` | Cria um loop que itera sobre uma sequência (lista, string, range). | `for i in "texto": print(i)` |
| `in` | Usado no `for` para iterar sobre itens de uma coleção. | `for item in lista:` |
| `break` | Interrompe imediatamente o loop (`for` ou `while`) e sai dele. | `if x == 5: break` |
| `continue` | Pula o restante da iteração atual e volta ao início do loop. | `if x % 2 == 0: continue` |
| `range()` | Gera uma sequência de números (frequentemente usado com `for`). | `range(0, 10, 2)` |
| `.split()` | Método de string que divide texto em lista (padrão: separa por espaços). | `"a b c".split()` → `['a','b','c']` |

---

## 2. Operadores e Símbolos

### Operadores Relacionais (Comparação)
Usados para comparar valores. Retornam sempre `True` ou `False` [1].

| Símbolo | Significado | Exemplo (x=10, y=5) |
| :--- | :--- | :--- |
| `<` | Estritamente menor que | `y < x` (True) |
| `<=` | Menor ou igual a | `y <= 5` (True) |
| `>` | Estritamente maior que | `x > y` (True) |
| `>=` | Maior ou igual a | `x >= 10` (True) |
| `==` | Igual a (valor) | `x == 10` (True) |
| `!=` | Diferente de | `x != y` (True) |
| `is` | Identidade do objeto (mesmo local na memória) | `x is y` (False) |
| `is not` | Negação da identidade | `x is not y` (True) |

### Operadores Lógicos
Usados para combinar condições [1, 2].

| Operador | Tipo | Resultado é True quando... | Exemplo |
| :--- | :--- | :--- | :--- |
| `not` | Unário | O operando é Falso (inverte o valor). | `not (5 > 10)` → True |
| `and` | Binário | **Ambos** os operandos são True. | `(x > 0) and (x < 20)` |
| `or` | Binário | **Pelo menos um** operando é True. | `(x == 0) or (x == 10)` |

> **Nota sobre Lógica:** Python considera `False` valores como: `0`, `False`, `None`, strings vazias `""` ou listas vazias `[]`. Qualquer outro valor é considerado `True` [2].

---

## 3. Estrutura de Código

### A Regra da Identação
Python exige alinhamento visual para definir o que está "dentro" do comando.
*   **Header:** A linha que termina com dois pontos `:`.
*   **Suite:** O bloco de código indentado (geralmente 4 espaços) [3].

### Estrutura Condicional (`if`)
```python
if condicao:
    # Executa se condicao for True
    acao_1()
elif outra_condicao:
    # (Opcional) Executa se a primeira falhou e esta for True
    acao_2()
else:
    # (Opcional) Executa se nenhuma acima for True
    acao_padrao()
Estrutura de Repetição (while)
Use quando não souber quantas vezes vai repetir, apenas a condição de parada.
while condicao_for_true:
    # Executa repetidamente
    if condicao_de_saida:
        break  # Sai do loop
Estrutura de Repetição (for e range)
Use para iterar um número fixo de vezes ou sobre itens.
Sintaxe do Range: range(início, fim, passo)
• Início: Inclusivo (Padrão 0).
• Fim: Exclusivo (Obrigatório).
• Passo: Incremento (Padrão 1).
# Ex: Imprime 0, 2, 4
for i in range(0, 6, 2):
    print(i)

--------------------------------------------------------------------------------
4. Checklist de Aplicação
Use esta lista para decidir qual estrutura usar baseada nos requisitos do Capítulo 2:
• Precisa repetir um código um número exato de vezes?
    ◦ Use for i in range(N):.
• Precisa repetir algo até que algo aconteça (ex: usuário digitar "sair")?
    ◦ Use while condicao:.
• Precisa processar cada palavra de uma frase individualmente?
    ◦ Use for palavra in frase.split():.
• Precisa pular uma execução específica dentro de um loop (ex: não imprimir números pares)?
    ◦ Use continue dentro de um if no loop.
• Precisa sair de um loop imediatamente quando encontrar um valor?
    ◦ Use break.
• Precisa testar múltiplas condições exclusivas (ex: nota A, B, C ou D)?
    ◦ Use if seguido de múltiplos elif. Evite muitos if aninhados (um dentro do outro).
• Precisa verificar se uma variável tem valor (não é zero nem vazia)?
    ◦ Use a verificação direta: if variavel: (Python trata 0 e vazio como False).