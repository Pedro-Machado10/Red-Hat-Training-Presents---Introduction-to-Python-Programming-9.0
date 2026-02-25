"""Exercise 7
Create two data files, each with a set of names, one per line.
Now, write a program that reads both files and lists only those names that are in both files.
The two file names should be supplied on the command line."""

import sys 

arquivo1 = sys.argv[1]
print(arquivo1)
arquivo2= sys.argv[2]
lista1 = []
lista2 = []

with open(arquivo1,"r") as nomes1, open(arquivo2,"r") as nomes2:
    
    while True:
        linha = nomes1.readline()
        linha1_limpa = linha.strip()
        if not linha:
            break
        lista1.append(linha1_limpa)
        
    print(lista1)

    while True:
        linha2 = nomes2.readline()
        linha2_limpa = linha2.strip() #limpa os "  " e /n da string
        if not linha2:
            break
        lista2.append(linha2_limpa)
       
    print(lista2)

nomescomum = []

for n in lista1:
    if n in lista2:
        nomescomum.append(n)

print(f"Os nomes em comum são: {nomescomum}")




