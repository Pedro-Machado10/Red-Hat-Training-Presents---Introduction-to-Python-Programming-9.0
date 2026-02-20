## 1. Dicionário de Sintaxe
Comandos fundamentais para importação e inspeção, agrupados por biblioteca.

### Gestão de Módulos e Sistema (`sys`)
| Comando | O que faz | Exemplo de uso curto |
| :--- | :--- | :--- |
| `import` | Carrega um módulo inteiro. | `import sys` |
| `from ... import` | Carrega funções específicas de um módulo. | `from math import sqrt` |
| `as` | Cria um alias (apelido) para o módulo. | `import datetime as dt` |
| `dir()` | Lista todos os símbolos (funções/variáveis) disponíveis num módulo. | `dir(sys)` |
| `sys.argv` | Lista de argumentos passados via linha de comando. | `args = sys.argv` |
| `sys.exit()` | Sai do programa. Aceita um código de erro ou mensagem. | `sys.exit(1)` ou `sys.exit("Erro")` |
| `sys.path` | Lista de strings com os caminhos de busca de módulos. | `print(sys.path)` |
| `sys.platform` | Identifica a plataforma (SO) em execução. | `if sys.platform == 'linux':` |

### Matemática e Aleatoriedade (`math`, `random`)
| Função | O que faz | Exemplo |
| :--- | :--- | :--- |
| `math.sqrt()` | Retorna a raiz quadrada (float). | `math.sqrt(64)` → `8.0` |
| `math.ceil()` | Arredonda para cima (teto). | `math.ceil(2.1)` → `3` |
| `math.hypot()` | Calcula a hipotenusa (Euclidiana). | `math.hypot(3, 4)` → `5.0` |
| `random.random()`| Retorna float aleatório entre 0.0 e 1.0. | `random.random()` |
| `random.choice()`| Escolhe um item aleatório de uma sequência. | `random.choice(['a', 'b'])` |
| `random.shuffle()`| Embaralha uma lista **in-place** (altera a original). | `random.shuffle(lista)` |

### Tempo e Data (`time`, `datetime`)
| Função | O que faz | Exemplo |
| :--- | :--- | :--- |
| `time.time()` | Retorna o tempo atual em segundos (Epoch). | `start = time.time()` |
| `time.sleep()` | Pausa a execução por N segundos. | `time.sleep(5)` |
| `time.ctime()` | Retorna string de data legível a partir de segundos. | `time.ctime()` |
| `datetime.date` | Cria objeto apenas com data (Ano, Mês, Dia). | `d = datetime.date(2023, 12, 25)` |
| `.today()` | Retorna a data atual local. | `datetime.date.today()` |
| `timedelta()` | Representa uma duração (diferença) de tempo. | `delta = datetime.timedelta(days=7)` |

---

## 2. Variáveis Especiais e Símbolos

### `__name__` e `__main__`
Variáveis usadas para controlar a execução de um módulo.

*   `__name__`: Variável global que armazena o nome do módulo.
    *   Se o arquivo é importado, `__name__` é o nome do arquivo (ex: `reusable`).
    *   Se o arquivo é executado diretamente, `__name__` vale `__main__`.

### `sys.argv`
Lista de argumentos de linha de comando.
*   `sys.argv`: É sempre o **nome do script** que está rodando.
*   `sys.argv[1]`: Primeiro argumento passado pelo usuário.

---

## 3. Estrutura de Código

### O Padrão de Execução Condicional
Estrutura essencial para criar módulos que podem ser tanto importados quanto executados como scripts.

```python
#!/usr/bin/env python3
import sys

# Funções reutilizáveis
def minha_funcao():
    print("Executando função do módulo.")

# Bloco principal de teste/execução
# Só roda se você chamar: python3 meu_script.py
if __name__ == "__main__":
    print("Este script está sendo executado diretamente.")
    minha_funcao()
    # Exemplo de uso de argumentos
    if len(sys.argv) > 1:
        print("Argumento recebido:", sys.argv[1])
Cálculo de Diferença de Datas (timedelta)
from datetime import date, timedelta

hoje = date.today()
uma_semana = timedelta(days=7)

futuro = hoje + uma_semana
print(futuro) # Imprime a data daqui a 7 dias

--------------------------------------------------------------------------------
4. Checklist de Aplicação
Use esta lista para decidir qual biblioteca usar com base no Módulo 5:
• Precisa ler opções que o usuário digitou no terminal ao rodar o programa?
    ◦ Use sys.argv. Lembre-se que o índice `` é o nome do script.
• O script precisa parar imediatamente devido a um erro grave?
    ◦ Use sys.exit("Mensagem de erro").
• Precisa saber quais funções existem dentro de um módulo desconhecido?
    ◦ Use dir(nome_do_modulo) no shell interativo ou print(dir(modulo)) no script.
• Precisa sortear um número ou escolher um vencedor em uma lista?
    ◦ Use random.randint() ou random.choice().
• Precisa medir quanto tempo seu código demorou para rodar?
    ◦ Use time.perf_counter() (ou time.time()) no início e no fim, e subtraia os valores.
• Precisa calcular "Data de hoje + 30 dias"?
    ◦ Use datetime.date somado a um datetime.timedelta.
• Precisa fazer seu código esperar/pausar por alguns segundos?
    ◦ Use time.sleep(segundos).