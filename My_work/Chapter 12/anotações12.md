# Guia de Referência Rápida: Debugging (Módulo 12)

Este módulo foca na utilização da biblioteca padrão `pdb` (Python Debugger) para rastrear e corrigir erros no código, permitindo a execução passo a passo e a inspeção de variáveis em tempo real.

## 1. Dicionário de Sintaxe (Iniciando o Debugger)
Formas de invocar a ferramenta de depuração no seu código.

| Comando / Parâmetro | O que faz | Exemplo de uso curto |
| :--- | :--- | :--- |
| `import pdb` | Importa o módulo do depurador interativo padrão do Python. | `import pdb` |
| `pdb.run()` | Inicia o depurador a partir do shell interativo do Python, passando a função que será testada como strin. | `pdb.run('main()')` |
| `-m pdb` | Opção usada no terminal do sistema para rodar um script inteiro sob o controle do depurador. | `python3 -m pdb script.py` |

---

## 2. Comandos Internos do PDB (Operadores)
Quando o programa pausa e o prompt do depurador `(Pdb)` aparece, você usa atalhos de teclado para controlar o fluxo de execuçã.

| Tecla / Comando | Nome | Ação |
| :--- | :--- | :--- |
| `s` | **Step** | Executa a linha atual e avança. Se houver uma chamada de função na linha, o depurador **entra** dentro da funçã. |
| `n` | **Next** | Executa a linha atual e avança, mas **não entra** em funções. Ele executa a função inteira e para na próxima linha do escopo atual. |
| `l` | **List** | Exibe o código-fonte ao redor da linha que está sendo executada no momento. Aceita intervalos de linhas. |
| `b` | **Break** | Cria um ponto de parada (*breakpoint*) em uma linha específica do código. |
| `c` | **Continue** | Continua a execução automática do programa até encontrar o próximo ponto de parada (*breakpoint*). |
| `p` | **Print** | Avalia e imprime o valor atual de uma variável ou expressão no contexto em que o depurador está pausado. |

---

## 3. Estrutura de Código (Visual)

### Iniciando o Debugger pelo Shell Interativo
Útil para testar funções específicas que já foram carregadas na memóri.
```python
$ python3
>>> import simple_program
>>> import pdb
# Passa a função como string para o método run
>>> pdb.run('simple_program.main()')
> <string>(1)<module>()
(Pdb) step
--Call--
> /caminho/do/arquivo/simple_program.py(11)main()
(Pdb) 
Iniciando o Debugger pela Linha de Comando (Recomendado)
A forma mais comum para rodar scripts inteiros em modo de depuração direto do terminal.
# O script é carregado e o depurador pausa imediatamente na primeira linha executável
$ python3 -m pdb simple_program.py
> /caminho/do/arquivo/simple_program.py(4)<module>()
-> def sum_args(args):
(Pdb) b 7       # Cria um breakpoint na linha 7
(Pdb) continue  # Roda o programa até bater na linha 7
(Pdb) p variavel # Inspeciona o valor de 'variavel'

--------------------------------------------------------------------------------
4. Checklist de Aplicação
Use esta lista para decidir qual comando do pdb utilizar para resolver seu problema:
• O código está quebrando e você quer avançar linha por linha para ver onde falha?
    ◦ Inicie o programa no depurador e vá digitando n (Next).
• O programa chamou uma função e você suspeita que o erro está dentro do cálculo dela?
    ◦ Quando o depurador chegar na linha que chama a função, digite s (Step) para entrar no código dela,.
• O script é gigante e você só quer inspecionar o que acontece a partir da linha 150?
    ◦ Use o comando b 150 para criar um breakpoint e depois digite c (Continue). O programa rodará rápido e só pausará quando chegar na linha 150.
• Você se perdeu no meio dos saltos e não sabe mais qual parte do código está rodando?
    ◦ Digite l (List) para imprimir as linhas de código acima e abaixo de onde você está agora.
• Você acha que uma variável recebeu o valor errado (ex: um texto em vez de número)?
    ◦ Com o programa pausado na linha suspeita, digite p nome_da_variavel para visualizar o valor exato que está guardado na memória naquele exato milissegundo.