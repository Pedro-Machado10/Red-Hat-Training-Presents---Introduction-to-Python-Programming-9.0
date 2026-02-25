"""Exercise 8
Now, create a few more files with one name per line.
The program in this exercise should read all these files and print the number of times each line occurs over all the files.
The file names should be supplied on the command line.
The following files are available in the AD141-apps repository, within the io/starter directory, and you can use them in the exercise:

names_a.txt
names_b.txt
names_c.txt
names_d.txt
The output from the program might be as follows:

Alice       4
Bart        2
Beverly     1
Bill        4
Chris       2
Dave        1
Frank       3
Jane        3
John        2
Mary        1
Mike        4
Peter       3
Susan       2"""

import sys

arquivos = sys.argv[1:]

listatodos = []

for arqui in arquivos:
    with open(arqui,"r") as nomes1:
        while True:
            linha = nomes1.readline()
            linha1_limpa = linha.strip()
            if not linha:
                break
            listatodos.append(linha1_limpa)

dicionario = {}

for nome in listatodos:
    
    if nome in dicionario:
        dicionario[nome] += 1
    else:
        dicionario[nome] = 1


for nomes, valor in sorted(dicionario.items()):
    print(f"{nomes:<10} {valor}") #em prints que usamos o f"" se colocarmos : logo após uma variavel, juntamente com <(esquerda) >(direita) e um valor (10) 
                                  #ele vai escrever aquela variácel ocupando 10 espaços, se a variavel tiver 6char ele preenche os 4 restantes