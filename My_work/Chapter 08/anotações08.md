# Guia de Referência Rápida: Input e Output (Módulo 8)

Este módulo aborda a leitura e escrita de fluxos de dados (arquivos de texto e binários), acesso aleatório ao conteúdo do arquivo e a interação com o sistema operacional para manipulação de arquivos e diretórios.

## 1. Dicionário de Sintaxe

### Manipulação de Arquivos e Streams
| Comando/Método | O que faz | Exemplo |
| :--- | :--- | :--- |
| `sys.stdout` | Stream de saída padrão (console). Pode ser usado em vez de `print()`. | `sys.stdout.write("Olá\n")` |
| `open()` | Abre um arquivo e retorna um stream de dados. | `f = open("saida.txt", "w")` |
| `.close()` | Fecha o stream de dados (libera o arquivo). | `f.close()` |
| `.read()` | Lê o stream inteiro (ou *N* bytes) e retorna como string. | `texto = f.read()` |
| `.readline()` | Lê uma única linha do arquivo (mantendo o `\n`). | `linha = f.readline()` |
| `.readlines()`| Lê o arquivo todo e retorna uma **lista de strings** (uma por linha). | `linhas = f.readlines()` |
| `.write()` | Escreve uma string no arquivo. Não adiciona `\n` automaticamente. | `f.write("Teste\n")` |
| `.writelines()`| Escreve uma lista de strings no arquivo de uma vez. | `f.writelines(lista)`  |

### Acesso Aleatório e Arquivos Binários
| Comando/Método | O que faz | Exemplo |
| :--- | :--- | :--- |
| `bytes()` | Cria um objeto imutável de bytes (usado em arquivos binários). | `bytes("Olá", "utf-8")` |
| `bytearray()` | Cria um objeto mutável de bytes. | `bytearray("Olá", "utf-8")` |
| `.encode()` | Converte string para bytes. | `texto.encode()` |
| `.decode()` | Converte bytes de volta para string. | `buffer.decode()` |
| `.tell()` | Retorna a posição atual do cursor (byte offset) dentro do arquivo. | `pos = f.tell()`  |
| `.seek()` | Move o cursor para uma posição específica no arquivo. | `f.seek(0, os.SEEK_SET)`  |

### Módulo OS e OS.PATH (`import os`)
| Função | O que faz | Exemplo |
| :--- | :--- | :--- |
| `os.getcwd()` | Retorna o diretório de trabalho atual. | `pasta = os.getcwd()`  |
| `os.listdir()`| Retorna uma lista com os arquivos e pastas no diretório. | `os.listdir(".")`  |
| `os.mkdir()` | Cria um novo diretório. | `os.mkdir("nova_pasta")`  |
| `os.remove()` | Apaga um arquivo. | `os.remove("lixo.txt")`  |
| `os.stat()` | Retorna status do arquivo (tamanho, permissões, modificação). | `os.stat("arq.txt")`  |
| `os.path.join()`| Junta partes de um caminho de forma compatível com o SO. | `os.path.join("a", "b.txt")`  |
| `os.path.exists()`| Verifica se um caminho (arquivo/pasta) existe. | `os.path.exists("arq.txt")`  |
| `os.path.isdir()` | Verifica se o caminho é um diretório. | `os.path.isdir("pasta")`  |

---

## 2. Operadores, Símbolos e Regras

### Modos de Abertura de Arquivo (`open`)
O modo determina o que você pode fazer com o arquivo aberto .
*   `r`: Leitura (Padrão). Falha se o arquivo não existir.
*   `w`: Escrita. **Trunca (apaga)** o arquivo se ele já existir.
*   `x`: Criação exclusiva. Falha se o arquivo já existir.
*   `a`: Append (Adição). Escreve no final do arquivo sem apagar o existente.
*   `b`: Binário. Usado em conjunto com outros (ex: `rb`, `wb`).
*   `t`: Texto (Padrão).
*   `+`: Atualização. Abre para leitura e escrita (ex: `r+`, `w+`).

### Constantes de Posicionamento (`whence` no `.seek()`)
Usados no comando `seek(offset, whence)` :
*   `os.SEEK_SET` (Valor `0`): Início do arquivo (Padrão).
*   `os.SEEK_CUR` (Valor `1`): Posição atual do cursor.
*   `os.SEEK_END` (Valor `2`): Final do arquivo.

---

## 3. Estrutura de Código (Visual)

### O uso da declaração `with` (Melhor Prática)
Garante que o arquivo seja fechado adequadamente após o processamento, mesmo que ocorra uma exceção (erro) no meio do processo.

```python
# Lendo um arquivo de texto de forma segura e iterando linha por linha
with open("output.txt", "r") as a_file:
    for a_line in a_file:
        # a_line já inclui a quebra de linha \n
        print(a_line, end="") 
# O arquivo é fechado automaticamente aqui
Lendo e Escrevendo Arquivos Binários
Para lidar com arquivos que não são texto (imagens, dados estruturados), o processo requer o modo binário e conversão de strings.
# Escrevendo binário
with open("binarydata", "wb") as the_file:
    # Precisa converter string para bytes usando .encode()
    the_file.write("Hello".encode())
    the_file.write(b" -- bytes diretos") # Ou usar prefixo b""

# Lendo binário
with open("binarydata", "rb") as the_file:
    buffer = the_file.read(10) # Lê 10 bytes
    print(buffer.decode())     # Converte bytes de volta para texto

--------------------------------------------------------------------------------
4. Checklist de Aplicação
• Precisa ler um arquivo gigantesco sem usar toda a memória do computador?
    ◦ Itere diretamente sobre o objeto stream: for line in f:,. Não use .readlines(), pois ele carrega tudo na memória.
• Gostaria de garantir que seu arquivo seja fechado corretamente se o programa der erro?
    ◦ Use o bloco with open("arquivo", "modo") as f:.
• Seu código precisa manipular caminhos de arquivos tanto no Windows quanto no Linux?
    ◦ Use os.path.join("pasta", "arquivo.txt") para que o Python coloque as barras corretas automaticamente.
• Precisa processar uma imagem ou arquivo zipado?
    ◦ Use modos binários como rb e wb e manipule objetos do tipo bytes ou bytearray.
• Você precisa voltar ao início de um arquivo que já acabou de ler para ler novamente?
    ◦ Use o método de acesso aleatório f.seek(0).
• Quer descobrir o tamanho de um arquivo em bytes ou a data em que foi modificado?
    ◦ Use o objeto retornado por os.stat("arquivo.txt"), como os.stat().st_size,.