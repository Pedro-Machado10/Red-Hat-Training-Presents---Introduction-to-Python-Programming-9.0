# Guia de Referência Rápida: JSON (Módulo 11)

Este módulo foca na integração, processamento e saída de dados formatados em JSON (JavaScript Object Notation) usando a biblioteca padrão do Python.

## 1. Dicionário de Sintaxe (`import json`)

A biblioteca `json` possui 4 funções principais, divididas entre operações com Strings (terminadas em `s`) e operações diretas com Arquivos.

| Função | O que faz (Descrição Curta) | Exemplo de código |
| :--- | :--- | :--- |
| `json.loads()` | **Deserializar String:** Converte uma string formatada em JSON para um dicionário ou lista Python. | `dict_py = json.loads('{"k": "v"}')` |
| `json.dumps()` | **Serializar String:** Converte um objeto Python (dict/list) para uma string em formato JSON. | `str_json = json.dumps(meu_dict)` |
| `json.load()` | **Ler de Arquivo:** Deserializa dados JSON diretamente de um arquivo de texto (file pointer). | `json.load(arquivo_aberto)` |
| `json.dump()` | **Escrever em Arquivo:** Serializa um objeto Python e escreve a saída diretamente em um arquivo. | `json.dump(meu_dict, arquivo_aberto)` |

---

## 2. Regras de Conversão e Formatação

### Tabela de Conversão de Tipos (Python ↔ JSON)
O módulo `json` realiza automaticamente as seguintes conversões de tipo:

| Tipo no Python | Tipo no JSON |
| :--- | :--- |
| `dict` | object (`{}`) |
| `list`, `tuple` | array (`[]`) |
| `str` | string (`""`) |
| `int`, `float` | number |
| `True` / `False` | `true` / `false` |
| `None` | `null` |

### Regras Importantes
* **Chaves são sempre Strings:** No JSON, as chaves de um par chave-valor devem ser strings. Se você converter um dicionário Python que usa números como chaves, a função converterá todas as chaves para strings.
* **Tratamento de Erros:** Se a função `loads` ou `load` tentar deserializar um dado inválido, o Python levantará uma exceção `json.decoder.JSONDecodeError`.

---

## 3. Estrutura de Código (Visual)

### Lendo e Escrevendo Arquivos JSON
Uso das funções `load` e `dump` em conjunto com o gerenciador de contexto `with open`,.

```python
import json

# Lendo de um arquivo JSON (.load)
with open("colors.json", "r") as m:
    dados = json.load(m)
    print(dados["colors"])

# Escrevendo em um arquivo JSON (.dump) com formatação
meus_dados = {"nome": "Maria", "idade": 30}
with open("data.json", "w") as r:
    # indent=2 formata o arquivo com quebras de linha e recuos
    json.dump(meus_dados, r, indent=2, sort_keys=True)
Formatando a Saída (Pretty Print com dumps)
A função dumps aceita parâmetros extras para deixar a string mais legível.
import json

dicionario = {"c": 3, "a": 1, "b": 2}
# sort_keys ordena alfabeticamente, indent cria recuos de espaço
texto_formatado = json.dumps(dicionario, sort_keys=True, indent=4)
print(texto_formatado)

--------------------------------------------------------------------------------
4. Checklist de Aplicação
Use esta lista para decidir qual técnica do módulo aplicar:
• Você recebeu um texto (string) de uma API na internet e precisa extrair dados dele?
    ◦ Use json.loads(texto_da_api) para transformá-lo em um dicionário Python.
• Você tem um dicionário no seu script e precisa transformá-lo em texto para enviar pela rede?
    ◦ Use json.dumps(seu_dicionario).
• Você quer ler as configurações do seu programa que estão salvas em um arquivo .json no disco?
    ◦ Abra o arquivo com open() e use json.load(arquivo).
• Você quer salvar os resultados do seu script permanentemente em um arquivo .json?
    ◦ Abra o arquivo em modo de escrita (w) e use json.dump(dados, arquivo).
• A saída do seu JSON está ilegível, tudo em uma linha só?
    ◦ Adicione os argumentos opcionais indent=4 e separators=(',', ': ') dentro da função dumps ou dump.