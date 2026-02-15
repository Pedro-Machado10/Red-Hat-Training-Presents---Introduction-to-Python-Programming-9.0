# Guia de Referência Rápida: Introdução ao Python (Módulo 1)

Este guia cobre a sintaxe, operadores e funções fundamentais apresentadas no Módulo 1.

## 1. Conceitos Iniciais e Regras de Sintaxe
Regras fundamentais para que o código funcione e seja legível.

*   **Identação:** Python usa espaços (padrão 4 espaços) para definir blocos de código, e não chaves `{}` [1].
*   **Comentários:**
    *   `#`: Comentário de linha única (o interpretador ignora tudo após o símbolo) [2].
    *   `"""`: Strings de aspas triplas usadas para comentários de múltiplas linhas ou docstrings [2].
*   **Case Sensitive:** `variavel` é diferente de `Variavel` [3].
*   **Shebang:** `#!/usr/bin/env python3` (primeira linha em scripts Linux/Unix para definir o interpretador) [4].

---

## 2. Funções Built-in (Entrada, Saída e Sistema)
Comandos nativos para interação básica e inspeção de objetos.

| Função | O que faz | Exemplo de Uso |
| :--- | :--- | :--- |
| `print()` | Exibe dados na saída padrão. Aceita argumentos `sep` e `end`. | `print("A", "B", sep="-")` [5] |
| `input()` | Lê dados do teclado. **Sempre retorna uma string.** | `nome = input("Digite: ")` [6] |
| `type()` | Retorna a classe (tipo de dado) do objeto. | `type(10)` → `<class 'int'>` [7] |
| `id()` | Retorna o endereço de memória único do objeto. | `id(var)` [7] |
| `help()` | Acessa o sistema de ajuda/documentação. | `help(str)` ou `help("modules")` [8] |
| `len()` | Retorna o comprimento de uma sequência (ex: string). | `len("Python")` → 6 [9] |
| `exit()` | Encerra o interpretador Python. | `exit()` [10] |

---

## 3. Números e Operadores Matemáticos
Operações suportadas por tipos numéricos (`int`, `float`) [11].

| Operador | Nome | Descrição | Exemplo (x=10, y=3) |
| :--- | :--- | :--- | :--- |
| `+` | Adição | Soma valores. | `x + y` → `13` |
| `-` | Subtração | Subtrai valores. | `x - y` → `7` |
| `*` | Multiplicação | Multiplica valores. | `x * y` → `30` |
| `/` | Divisão Real | Divide e retorna sempre float. | `x / y` → `3.333...` |
| `//` | Divisão Inteira | Divide e descarta a parte decimal (piso). | `x // y` → `3` |
| `%` | Módulo | Retorna o resto da divisão. | `x % y` → `1` |
| `**` | Exponenciação | Eleva à potência. | `x ** y` → `1000` |
| `abs()` | Valor Absoluto | Retorna valor positivo. | `abs(-5)` → `5` |

---

## 4. Funções de Conversão de Tipos (Casting)
Funções para transformar dados de um tipo para outro [12], [13].

| Função | O que faz | Exemplo |
| :--- | :--- | :--- |
| `int()` | Converte string/float para inteiro. | `int("10")` ou `int(9.9)` → `9` |
| `float()` | Converte string/int para ponto flutuante. | `float("5")` → `5.0` |
| `str()` | Converte objeto para texto. | `str(123)` → `"123"` |
| `divmod()` | Retorna tupla com (quociente, resto). | `divmod(10, 3)` → `(3, 1)` |
| `ord()` | Retorna código Unicode do caractere. | `ord("A")` → `65` |
| `chr()` | Retorna caractere dado o código. | `chr(65)` → `"A"` |
| `hex()` | Converte int para string hexadecimal. | `hex(255)` → `"0xff"` |

---

## 5. Strings e Manipulação de Texto
Operações específicas para o tipo `str`.

### Operadores de Sequência [14]
*   `+`: Concatenação (junta strings). Ex: `"Red" + "Hat"`.
*   `*`: Repetição. Ex: `"-" * 10`.
*   `in`: Verifica pertinência (True/False). Ex: `"a" in "banana"`.

### Principais Métodos
Usados com a sintaxe `objeto.metodo()`.

| Método | O que faz | Exemplo |
| :--- | :--- | :--- |
| `.upper()` | Converte para maiúsculas. | `"abc".upper()` [15] |
| `.startswith()` | Verifica início da string. | `"img.jpg".startswith("img")` [15] |
| `.endswith()` | Verifica fim da string. | `"img.jpg".endswith(".jpg")` [15] |
| `.find()` | Retorna índice da 1ª ocorrência ou -1. | `"banana".find("na")` → `2` [16] |
| `.replace()` | Substitui trechos do texto. | `"1-2".replace("-", ":")` [16] |
| `.strip()` | Remove espaços das extremidades. | `"  oi  ".strip()` [9] |
| `.split()` | Divide string em lista (padrão: espaço).| `"a,b".split(",")` → `['a', 'b']` [16] |
| `.format()` | Insere valores em placeholders `{}`. | `"Olá {}".format("Mundo")` [17] |
| `.count(x)` | Retorna o número de ocorrências de "x" na sequência. | `"banana".count("a")` → `3` |

---

## 6. Estrutura de Código: Fatiamento (Slicing)
Visualização da extração de partes de uma sequência (strings) [18].

**Sintaxe:** `variavel[início : fim : passo]`

*   **Início (Start):** Índice onde começa (inclusivo). Padrão = 0.
*   **Fim (Stop):** Índice onde para (exclusivo - não inclui este item). Padrão = final da string.
*   **Passo (Step):** De quanto em quanto pular. Padrão = 1.

```python
texto = "PYTHON"
# Índices: P(0) Y(1) T(2) H(3) O(4) N(5)

texto[0:2]   # "PY"   (Do 0 até antes do 2)
texto[2:]    # "THON" (Do 2 até o fim)
texto[:2]    # "PY"   (Do começo até antes do 2)
texto[::2]   # "PTO"  (String toda, pulando de 2 em 2)
texto[::-1]  # "NOHTYP" (Inverte a string)
