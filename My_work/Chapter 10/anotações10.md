# Guia de Referência Rápida: Expressões Regulares (Módulo 10)

Este módulo foca na utilização da biblioteca `re` para buscar, combinar, modificar e extrair textos com base em padrões complexos de strings.

## 1. Dicionário de Sintaxe (`import re`)

A biblioteca `re` possui várias funções para aplicar expressões regulares, gerando objetos do tipo `Match` ou retornando listas/strings modificadas.

| Função | O que faz (Ação) | Retorno |
| :--- | :--- | :--- |
| `re.search()` | Busca o padrão da esquerda para a direita, procurando o **primeiro** local onde ocorre a combinação. | Objeto Match ou `None` |
| `re.match()` | Verifica se o padrão ocorre estritamente no **início** da string. | Objeto Match ou `None` |
| `re.fullmatch()`| Exige que a **string inteira** corresponda perfeitamente ao padrão. | Objeto Match ou `None` |
| `re.findall()` | Encontra **todas** as substrings que dão match no padrão. | Lista de strings |
| `re.split()` | Divide a string original usando o padrão como delimitador. | Lista de strings |
| `re.sub()` | Substitui as ocorrências do padrão por uma nova string. | String modificada |
| `re.compile()` | Compila a string de expressão regular em um objeto para maior eficiência em usos múltiplos. | Objeto Regex Compilado |

---

## 2. Operadores, Símbolos e Regras Especiais

### Metacaracteres e Âncoras
Caracteres que possuem significados especiais na sintaxe da expressão regular.
*   `.` : Qualquer caractere (exceto nova linha).
*   `^` : Início da string.
*   `$` : Fim da string.
*   `|` : Operador "OU" lógico (Alternativa). Ex: `Anne|Chris`.
*   `\` : Caractere de escape (remove o significado especial de um metacaractere, ex: `\.` busca um ponto final literal).

### Classes de Caracteres Predefinidas
Atalhos para conjuntos comuns de caracteres.
| Símbolo | Significado | Símbolo Inverso (Negação) |
| :--- | :--- | :--- |
| `\d` | Qualquer dígito (0-9) | `\D` (Qualquer NÃO dígito) |
| `\w` | Caractere de palavra (a-z, A-Z, 0-9, _) | `\W` (NÃO palavra) |
| `\s` | Espaço em branco (espaço, tab `\t`, quebra de linha `\n`) | `\S` (NÃO espaço em branco) |

### Quantificadores (Repetições)
Definem quantas vezes o elemento anterior deve se repetir.
*   `*` : Zero ou mais vezes.
*   `+` : Uma ou mais vezes.
*   `?` : Zero ou uma vez (Opcional).
*   `{m,n}` : No mínimo `m` e no máximo `n` vezes.
*   **Comportamento Guloso (Greedy):** Por padrão, quantificadores tentam englobar a maior parte possível da string. Colocar um `?` logo após o quantificador (ex: `*?` ou `+?`) o torna **Não-Guloso (Non-Greedy)**, casando a menor parte possível.

---

## 3. Estrutura de Código (Visual)

### Testando e Acessando Grupos (`Match Object`)
Grupos criados com parênteses `()` permitem extrair pedaços específicos do texto encontrado.

```python
import re

texto = "O número de telefone é 123-4567."
# Usa-se r"" (Raw String) para que o Python não tente processar as barras invertidas \
padrao = r"(\d{3})-(\d{4})" 

# Executa a busca
resultado = re.search(padrao, texto)

if resultado:
    print(resultado.group(0))  # '123-4567' (O match inteiro)
    print(resultado.group(1))  # '123' (Apenas o primeiro grupo de parênteses)
    print(resultado.group(2))  # '4567' (O segundo grupo de parênteses)
    print(resultado.span())    # (23, 31) (A posição de início e fim do match na string original)
Substituição e Uso de Flags
As Flags alteram o comportamento padrão da busca (ex: ignorar maiúsculas/minúsculas).
import re

texto = "A cor é Vermelho, mas também Gosto de VERMELHO e vermelho."
padrao = r"vermelho"

# re.IGNORECASE ou re.I faz com que não diferencie maiúsculas de minúsculas
# Substitui todas as variações da palavra "vermelho" por "azul"
novo_texto = re.sub(padrao, "azul", texto, flags=re.IGNORECASE)

print(novo_texto) # "A cor é azul, mas também Gosto de azul e azul."

--------------------------------------------------------------------------------
4. Checklist de Aplicação
• Precisa verificar se uma string contém um pedaço específico de texto com variações de formato?
    ◦ Use re.search(padrao, string). Retornará o objeto Match se encontrar ou None se falhar.
• Quer extrair todas as instâncias de um formato (ex: todos os CPFs em um documento gigante)?
    ◦ Use re.findall(), que devolverá uma lista limpa com todas as strings capturadas.
• Precisa censurar ou padronizar dados, trocando um padrão por outro?
    ◦ Use re.sub(padrao, substituto, string). Se quiser reutilizar partes da string original no substituto, use referências como \1 na string de substituição.
• Seu código Regex está com comportamento estranho por causa de barras duplas (\\)?
    ◦ Certifique-se de definir seu padrão como uma Raw String, colocando um r antes das aspas (ex: r"\w+").
• Quer que o padrão case tanto com "A" quanto com "a" sem precisar duplicar a lógica?
    ◦ Passe o argumento opcional flags=re.IGNORECASE (ou re.I) na função chamada.
• Precisa validar se a entrada do usuário está exatamente no formato esperado (ex: CEP) sem nenhum caractere extra no começo ou no fim?
    ◦ Use re.fullmatch() em vez de re.search().
