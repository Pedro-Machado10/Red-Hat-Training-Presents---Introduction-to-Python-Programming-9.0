"""Exercise 4
Rewrite Exercise 3 such that the file names are obtained from the command line if two arguments are supplied.
If the number of arguments is not two, then it should fall back on prompting the user for the filenames.
The interface might look like:
python3 your_program_name.py inputfile outputfile"""


import sys

try:
    if len(sys.argv) > 0:
        texto = sys.argv
        ent = texto[1]
        sai = texto[2]
        
        entrada = ent
        saida = sai
        
except IndexError:
    print("Digite o nome dos arquivo de entrada e de saída, respectivamente:")
    entrada = input()
    saida = input()
    
with open(entrada,"r") as arquivo1, open(saida,"w") as copia:
    
    while True:
        linha = arquivo1.readline() #usamos o readline de uma linha de cada vez para não sobrecarregar a memoria RAM, 
        if not linha:               #pois se fosse muito texto e tentássemos colocar de uma só vez (usando o read()) poderia dar ruim
            break
        copia.write(linha)
    
    