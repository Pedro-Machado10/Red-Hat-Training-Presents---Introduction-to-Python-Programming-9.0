# Guia de Referência Rápida: Exceções (Módulo 7)

Este módulo foca no tratamento de erros em tempo de execução, permitindo que o programa se recupere de falhas sem travar (crash), além da criação de exceções personalizadas.

## 1. Dicionário de Sintaxe
Comandos e palavras-chave essenciais para o controle do fluxo de erros.

| Comando / Keyword | O que faz | Exemplo de uso curto |
| :--- | :--- | :--- |
| `try` | Define o bloco de código que será monitorado quanto a possíveis erros. | `try:` <br> `  x = int(input())` |
| `except` | Define o bloco que tratará uma exceção específica caso ela ocorra no `try`. | `except ValueError:` |
| `else` | Bloco opcional que executa **apenas se nenhuma exceção ocorrer** no bloco `try`. | `else:` <br> `  print("Sucesso!")` |
| `finally` | Bloco opcional que executa **sempre**, ocorrendo erro ou não. Útil para limpar recursos . | `finally:` <br> `  print("Fim.")` |
| `as` | Atribui a instância do erro capturado a uma variável, permitindo inspecioná-la. | `except ValueError as ve:` |
| `raise` | Força (dispara) intencionalmente uma exceção especificada no código. | `raise Exception("Erro")` |
| `assert` | Avalia se uma expressão é Verdadeira/Falsa. Se for Falsa, dispara um `AssertionError`. | `assert max >= a, "Falhou"` |

---

## 2. Regras e Conceitos do Modelo de Exceções

### Hierarquia de Exceções
As exceções em Python fazem parte de uma árvore de hierarquia.
*   `BaseException` é a raiz, mas as exceções padrão do sistema e as criadas pelo usuário herdam da classe `Exception`.
*   Você pode capturar múltiplas exceções diferentes empilhando vários blocos `except` um após o outro.

### O Comando `raise` Isolado
Se a palavra-chave `raise` for usada sozinha **dentro de um bloco `except`**, ela relançará (reraise) a exceção original que acabou de ser capturada.

### A Sintaxe do `assert`
Usado primariamente para checar o estado interno do programa por desenvolvedores (debugging).
**Sintaxe:** `assert expressao[, "mensagem opcional"]`
Se a `expressao` resultar em `False`, a "mensagem opcional" será exibida no `AssertionError`.

---

## 3. Estrutura de Código (Visual)

### Tratamento Completo de Exceções (`try / except / else / finally`)
Pelo menos um bloco `except` ou `finally` deve seguir obrigatoriamente um bloco `try`.

```python
try:
    # Código que pode gerar um erro
    total += int(value)
except ValueError as e:
    # Código para tratar um tipo específico de erro
    print("Erro de valor: ", e)
except EOFError:
    # Trata outro tipo de erro
    print("Fim do fluxo inesperado")
else:
    # Roda se o 'try' funcionou perfeitamente
    print("Deu tudo certo, nenhum erro!")
finally:
    # Roda sempre, independente do que aconteceu acima
    print("Sempre executado no final.")
Criando Exceções Personalizadas (User-Defined Exceptions)
Ao criar erros específicos para o seu aplicativo, as classes de exceção devem ser derivadas direta ou indiretamente da classe Exception, e não de BaseException.
# Classe base para os erros do módulo
class PasswordError(Exception):
    pass

# Exceção específica herdando da base criada acima
class TrivialPasswordError(PasswordError):
    def __init__(self, msg):
        super().__init__("Trivial Password: " + msg)

--------------------------------------------------------------------------------
4. Checklist de Aplicação
Use esta lista para decidir qual técnica de tratamento aplicar no seu código:
• Precisa evitar que o programa quebre porque o usuário digitou uma letra onde deveria ser um número?
    ◦ Envolva a conversão int(input()) em um bloco try e use except ValueError:.
• O programa acessa um recurso externo (arquivos, rede) que precisa ser finalizado adequadamente mesmo se der erro no meio?
    ◦ Coloque a ação de finalização no bloco finally:.
• Você tem validações de regras de negócio complexas (ex: "Senha muito curta" ou "Senha repetitiva")?
    ◦ Crie suas próprias exceções usando class MinhaExcecao(Exception): e dispare com o comando raise quando a regra for violada.
• Precisa acessar os detalhes intrínsecos de um erro capturado?
    ◦ Capture a exceção como um objeto usando a palavra-chave as (ex: except Exception as err:) e use-a dentro do bloco.
• Você está desenvolvendo e quer testar agressivamente se uma variável possui o valor esperado (ex: se X não pode nunca ser menor que 0)?
    ◦ Insira afirmações de depuração usando assert x >= 0, "X ficou negativo!".




