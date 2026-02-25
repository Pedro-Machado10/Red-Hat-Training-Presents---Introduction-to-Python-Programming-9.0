"""Exercise 2
Revise Exercise 1 so that it accepts as an optional first command line argument a -t option."""

import sys #pega o que o usuario digitar PELO terminal

total = 0
dados = sys.argv[1:]
totalizar = False
loop = 0

if dados[0] == '-t':
    totalizar = True

if totalizar == True:
    dados = dados[1:]
    loop = len(dados)
else:
    print("Primeiro Arquivo:")

totallinhas = 0
totalwords = 0
totalchar = 0

for n in dados:
    with open(n,"r") as leitor:
        conteudo = leitor.readlines() #lista que cada indice é uma linha do texto / Conteudo = [Primeiro exercício de teste, Pedro é bonito]
        numlinhas = len(conteudo)
        totallinhas += numlinhas
        
        numwords = []
        for palavra in conteudo:
            numwords += palavra.split()
        totalwords += len(numwords)
        
        numchar = 0
        for cher in conteudo:
            numchar += len(cher)
        totalchar += numchar
        
        if totalizar == False:
            print(f"O número de linhas é: {numlinhas}")
            print(f"O número de palavras é: {len(numwords)}")
            print(f"O número de characteres é: {numchar}")
            print("\nPróximo Arquivo:")

        
if totalizar == True: 
    print("-------- TOTALIZAR ABAIXO:-----------------")
    print(f"O número de linhas é: {totallinhas}")

    print(f"O número de palavras é: {totalwords}")

    print(f"O número de characteres é: {totalchar}")


    