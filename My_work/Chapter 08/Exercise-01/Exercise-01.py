"""Exercise 1
Write a program that counts the number of lines, words, and characters in each file named on the command line."""

import sys #pega o que o usuario digitar PELO terminal
nome_do_arquivo = sys.argv[1] 
print(f"O arquivo que vou abrir é o: {nome_do_arquivo}")

with open(nome_do_arquivo,"r") as leitor:
    
    conteudo = leitor.readlines() #lista que cada indice é uma linha do texto
    print(conteudo)
    numlinhas = len(conteudo)
    print(f"O número de linhas é: {numlinhas}")
    
    numwords = []
    for n in conteudo:
        numwords += n.split()
    print(f"O número de palavras é: {len(numwords)}")
    
    numchar = 0
    for n in conteudo:
        numchar += len(n)
    print(f"O número de characteres é: {numchar}")


    