"""Exercise 5
Add exception handling to the previous exercise so that if a file open fails, an OSError exception is handled, and the program is halted."""

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

try: 
    with open(entrada,"r") as arquivo1, open(saida,"w") as copia:
        
        while True:
            linha = arquivo1.readline() #usamos o readline de uma linha de cada vez para não sobrecarregar a memoria RAM, 
            if not linha:               #pois se fosse muito texto e tentássemos colocar de uma só vez (usando o read()) poderia dar ruim
                break
            copia.write(linha)
except OSError: 
    print("O arquivo de entrada não está funcionando")