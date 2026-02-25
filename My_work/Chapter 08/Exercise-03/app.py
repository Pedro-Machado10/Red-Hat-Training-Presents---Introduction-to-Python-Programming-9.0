"""Exercise 3
Write a program that asks the user for the names of an input and an output file.

Open both of these files and then have the program read from the input file (by using readline()) and write to the output file (by using write()).

In effect, this is a copy program, whose interface to the program might look like:

Enter the name of the input file: myinput
Enter the name of the output file: myoutput"""

print("Digite o nome dos arquivo de entrada e de saída, respectivamente:")
entrada = input()
saida = input()

with open(entrada,"r") as arquivo1, open(saida,"w") as saida:
    
    while True:
        linha = arquivo1.readline() #usamos o readline de uma linha de cada vez para não sobrecarregar a memoria RAM, 
        if not linha:               #pois se fosse muito texto e tentássemos colocar de uma só vez (usando o read()) poderia dar ruim
            break
        saida.write(linha)
    
    