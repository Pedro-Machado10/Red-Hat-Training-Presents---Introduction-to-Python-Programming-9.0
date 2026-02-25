"""Exercise 3
Write a program that reads lines from the user one at a time to see if they are formatted according to the following criteria.
Correctly formatted lines should consist of a four character identifier, any number of spaces or tabs, and a description.
The four character identifier should consist of two digits followed by two uppercase characters.
For each correctly formatted line, print the two digits, the two characters, and the descriptions.
Print all of these pieces of information on separate lines.


Aqui estão os blocos de montar mais comuns que o PDF nos apresenta:

\d: Representa qualquer dígito (0 a 9).
+: É um "quantificador". Significa que o item anterior deve aparecer uma ou mais vezes.
^: Indica o início exato da string.
$: Indica o fim exato da string.
?: Outro quantificador. Significa que o item anterior pode aparecer zero ou uma vez (ou seja, é opcional).
.: qualquer caractere
*: quantificador que significa que o item anterior qualquer quantidade deles



"""

#Exemplo: "12AB    Servidor de Banco de Dados"

import re

while True:
    print("Digite um padrao")
    num = input()
    
    if not num:
        break
        
    padrao = "^(\d{2})([A-Z]{2})\s+(.*)$"
    resultado = re.search(padrao,num)
    
    if resultado:
        print(f"Números: {resultado.group(1)}") #Saída: 12
        print(f"Letras: {resultado.group(2)}")  #Saída: AB
        print(f"texto: {resultado.group(3)}")  #Saída: Servidor de Banco de Dados



        
