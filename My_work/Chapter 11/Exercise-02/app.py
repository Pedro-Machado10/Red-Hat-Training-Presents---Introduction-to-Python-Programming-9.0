"""Exercise 2
Write a program that saves a dictionary as a JSON file.
The dictionary should contain the word frequency (words as keys, frequency as values) read from the cyclone file.
When saving the JSON file, the indentation level should be tab characters.
The program should display the word that appeared most often in the file.
Sample output:
'the' occurred 93 times"""

import json

with open("ciclone.txt","r") as arquivo1:
    palavras = arquivo1.read()
    lista_palavras = palavras.split()
    dicionario = {}
   
    for palavra in lista_palavras:
        if palavra in dicionario:
            dicionario[palavra] += 1 
        else:
            dicionario[palavra] = 1

with open("catalogo.json","w") as arquivojs:      
    json.dump(dicionario,arquivojs,indent="\t") #Pega um Dicionário Python e salva direto num Arquivo JSON \ O indent serve para que o arquivo JSON n fique tudo em uma linha só

maior = 0
campea = ""

for p,v in dicionario.items():
    if v > maior:
        maior = v
        campea = p

print(f"A palavra campeã foi: '{campea}' e o número de vezes que ela apareceu foi: {maior}")