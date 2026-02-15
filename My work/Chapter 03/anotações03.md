# Guia de Referência Rápida: Coleções Python (Módulo 3)

Este módulo aborda as quatro estruturas de dados fundamentais: Listas, Tuplas, Conjuntos (Sets) e Dicionários, além de ordenação [1, 2].

## 1. Dicionário de Sintaxe e Métodos

### Construtores e Funções Gerais
| Função | O que faz | Exemplo |
| :--- | :--- | :--- |
| `list()` | Cria uma lista vazia ou converte iterável em lista [3]. | `list("abc")` → `['a','b','c']` |
| `tuple()` | Cria uma tupla vazia ou converte iterável em tupla [4]. | `tuple([1, 2])` → `(1, 2)` |
| `set()` | Cria um conjunto vazio ou converte iterável (remove duplicatas) [5]. | `set([1, 2])` → `{1, 2}` |
| `dict()` | Cria um dicionário vazio ou converte lista de pares chave-valor [6]. | `dict([(k,v)])` |
| `enumerate()` | Retorna objeto enumerado (índice, valor) durante loops [4]. | `for i, v in enumerate(lista):` |
| `sorted()` | Função built-in que retorna uma **nova** lista ordenada [7]. | `nova_lista = sorted(lista)` |

### Métodos de Lista (Mutáveis e Ordenadas) [7, 8]
| Método | Descrição |
| :--- | :--- |
| `.append(x)` | Adiciona `x` ao final da lista. |
| `.insert(i, x)` | Insere `x` na posição `i`. |
| `.remove(x)` | Remove a primeira ocorrência de `x`. Erro se não existir. |
| `.pop(i)` | Remove e retorna o item na posição `i` (padrão: último). |
| `.sort()` | Ordena a lista **in-place** (altera a original). |
| `.reverse()` | Inverte a ordem dos itens **in-place**. |

### Métodos de Conjunto/Set (Não Ordenados e Únicos) [9, 10]
| Método | Descrição |
| :--- | :--- |
| `.add(x)` | Adiciona o elemento `x` ao conjunto. |
| `.update(x)` | Adiciona múltiplos elementos de um iterável `x`. |
| `.remove(x)` | Remove `x`. Gera `KeyError` se não existir. |
| `.discard(x)` | Remove `x`. **Não** gera erro se não existir. |
| `.pop()` | Remove e retorna um elemento arbitrário. |
| `.clear()` | Remove todos os elementos. |
| `.issubset()` | Verifica se é subconjunto de outro. |
| `.issuperset()` | Verifica se é superconjunto de outro. |

### Métodos de Dicionário (Chave-Valor) [11-13]
| Método | Descrição |
| :--- | :--- |
| `.get(k, default)`| Retorna valor da chave `k`. Retorna `default` (ou None) se `k` não existir (evita erro). |
| `.keys()` | Retorna uma visualização (view) de todas as chaves. |
| `.values()` | Retorna uma visualização de todos os valores. |
| `.items()` | Retorna uma visualização de tuplas `(chave, valor)`. |
| `.pop(k)` | Remove a chave `k` e retorna seu valor. |
| `.popitem()` | Remove e retorna o último par `(chave, valor)` inserido. |

---

## 2. Operadores e Símbolos

### Símbolos de Criação e Acesso [2-4, 6]
| Símbolo | Uso | Exemplo |
| :--- | :--- | :--- |
| `[]` | Criação de Listas ou Acesso por índice/chave. | `l = [1, 2]` ou `d['chave']` |
| `()` | Criação de Tuplas. | `t = (1, 2)` |
| `{}` | Criação de Dicionários (se tiver `:`) ou Sets. | `d = {'a':1}` ou `s = {1, 2}` |
| `,` | Vírgula (essencial para criar tuplas de 1 item). | `t = (1,)` |

### Operadores Matemáticos de Conjuntos (Sets) [14]
| Op | Nome | Descrição |
| :--- | :--- | :--- |
| `|` | União | Itens em A **ou** B (junta tudo). |
| `&` | Interseção | Itens em A **e** B (comuns). |
| `-` | Diferença | Itens em A mas **não** em B. |
| `^` | Dif. Simétrica | Itens em A ou B, mas **não em ambos**. |

---

## 3. Estrutura de Código

### Loops em Coleções

**Iterar com Índice (enumerate) [4]**
```python
# Útil para listas e tuplas quando precisa da posição
for indice, valor in enumerate(colecao):
    print("Posição {}: {}".format(indice, valor))
Iterar em Dicionários
dados = {'nome': 'Ana', 'idade': 25}

# Padrão (apenas chaves)
for k in dados: ...

# Chave e Valor (desempacotamento)
for chave, valor in dados.items():
    print(chave, valor)
Ordenação Personalizada (Sorting)
Estrutura para ordenar coleções complexas usando o parâmetro key.
# Ordenar lista de strings pelo tamanho (len)
nomes.sort(key=len)

# Ordenar reverso
nomes.sort(key=len, reverse=True)

# Ordenar por caractere específico (ex: último)
def ultimo_char(s): 
    return s[-1]
sorted(nomes, key=ultimo_char)

--------------------------------------------------------------------------------
4. Checklist de Aplicação
Use esta lista para escolher a estrutura de dados correta para o problema:
• Precisa manter a ordem de inserção e permitir duplicatas?
    ◦ Use Lista (list). É a "array" dinâmica do Python.
• Precisa de uma lista de itens que não deve ser alterada (imutável)?
    ◦ Use Tupla (tuple). Mais eficiente e segura para dados fixos.
• Precisa garantir que não existam duplicatas?
    ◦ Use Conjunto (set). Ótimo para remover repetidos de uma lista (list(set(lista_suja))).
• Precisa verificar se um item existe na coleção muito rápido?
    ◦ Use Conjunto (set) ou Dicionário (dict). A busca é muito mais rápida que na lista.
• Precisa associar valores a identificadores únicos (lookup)?
    ◦ Use Dicionário (dict). Ex: Agenda telefônica (Nome -> Número).
• Precisa remover um item de um Set sem arriscar quebrar o código se ele não existir?
    ◦ Use .discard() em vez de .remove().
• Precisa acessar um valor de Dicionário sem erro se a chave faltar?
    ◦ Use .get('chave') em vez de ['chave']. O get retorna None se falhar.
• Precisa ordenar sem alterar a lista original?
    ◦ Use a função sorted(lista). Use .sort() apenas se quiser alterar a própria lista.