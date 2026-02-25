# Guia de Referência Rápida: Estruturas de Dados (Módulo 9)

Este módulo aborda formas concisas e avançadas de criar, processar e ordenar coleções de dados usando *Comprehensions*, *Generators*, processamento paralelo (`zip`) e ordenações customizadas.

## 1. Dicionário de Sintaxe
Palavras-chave e funções introduzidas para manipulação otimizada de coleções.

| Comando/Keyword | O que faz | Exemplo de uso curto |
| :--- | :--- | :--- |
| `yield` | Usado dentro de uma função para transformá-la em um *Generator*. Retorna um valor e pausa a execução até a próxima iteração. | `yield x` |
| `zip()` | Itera através de múltiplas coleções em paralelo, agrupando seus itens. | `zip(dias, meses, anos)` |
| `operator.itemgetter()` | Função de conveniência para extrair itens (índices) de uma sequência. Muito usada no parâmetro `key` de ordenações. | `key=itemgetter(4, 1, 0)` |
| `operator.attrgetter()` | Extrai atributos nomeados de um objeto. Usada no parâmetro `key` para ordenar listas de objetos. | `key=attrgetter('last_name')` |

---

## 2. Operadores, Símbolos e Regras

### Símbolos de Construção Rápida (Comprehensions e Expressions)
O tipo de parêntese ou chaves define qual estrutura será gerada de forma concisa:

| Símbolo | Estrutura Gerada | Característica Principal | Exemplo |
| :--- | :--- | :--- | :--- |
| `[]` | **List Comprehension** | Cria uma lista inteira na memória de uma só vez [1]. | `[x*2 for x in lista]` |
| `{}` com `:` | **Dictionary Comprehension** | Requer duas expressões separadas por dois-pontos (`chave: valor`). | `{k: v for k,v in lista}`  |
| `()` | **Generator Expression** | Não cria a coleção inteira na memória; avalia e gera um item por vez sob demanda. | `(x*2 for x in lista)` |

### Regra de Ouro da Memória
*   Se a quantidade de dados for **pequena/média**, *List/Dict Comprehensions* são as formas mais concisas.
*   Se a quantidade de dados for **enorme ou infinita**, o uso de listas se torna impossível ou muito custoso. Nesses casos, **obrigatoriamente** use *Generators* (Expressões ou Funções com `yield`) para evitar o overhead de memória.

---

## 3. Estrutura de Código (Visual)

### List Comprehension com Filtro (`if`)
Sintaxe: `[expressão for item in iterável if condição]`.
```python
# Cria uma lista apenas com os quadrados dos números pares
quadrados_pares = [x * x for x in range(1, 16) if x % 2 == 0] 
Dictionary Comprehension
Sintaxe: {expressao_chave: expressao_valor for item in iterável}.
nomes = ["Ashley", "Emma", "Jayden", "Ethan"]
# Cria um dicionário onde a chave é o nome e o valor é o tamanho do nome
tamanhos = {name: len(name) for name in nomes}
Generator Function (Função Geradora)
Qualquer função contendo a palavra-chave yield se torna um gerador.
def seguindo_dias(quantos): 
    hoje = datetime.date.today() 
    for i in range(1, quantos + 1):
        # Retorna o valor atual, mas salva o estado para o próximo loop
        yield hoje + datetime.timedelta(days=i)
Ordenação Especializada (Tertiary Sort)
Como ordenar uma lista usando múltiplos critérios (ex: ordenar por Estado, depois Sobrenome, depois Nome).
from operator import attrgetter

# Opção A: Usando uma função lambda retornando uma tupla com a ordem de prioridade
customer_list.sort(key=lambda x: (x[6], x[10], x))

# Opção B: Usando attrgetter (mais limpo para listas de objetos da sua própria classe)
customer_list.sort(key=attrgetter('address.state', 'last_name', 'first_name'))

--------------------------------------------------------------------------------
4. Checklist de Aplicação
Use esta lista para decidir qual estrutura usar baseada nos requisitos do Capítulo 9:
• Precisa criar uma lista filtrando e modificando dados de outra lista em uma única linha?
    ◦ Use List Comprehensions (sintaxe com colchetes []).
• Precisa criar um dicionário rapidamente a partir de uma lista ou tupla (ex: inverter chaves/valores)?
    ◦ Use Dictionary Comprehensions (sintaxe com chaves {k: v}).
• O conjunto de dados que você precisa processar é gigante (ou infinito) e vai travar a memória do computador?
    ◦ Use Generators. Se for simples, use uma Generator Expression com (); se for complexo, crie uma função com yield.
• Precisa percorrer duas ou mais listas paralelamente no mesmo loop for?
    ◦ Use a função zip(lista1, lista2). O menor argumento dita o número de iterações.
• Precisa ordenar uma lista baseada em dois ou três critérios seguidos (ex: ordenar por preço e depois por nome)?
    ◦ Use o método .sort(key=...) passando uma função lambda que retorne uma tupla com os critérios ou use operator.itemgetter() / operator.attrgetter().