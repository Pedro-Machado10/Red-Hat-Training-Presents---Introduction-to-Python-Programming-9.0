"""Exercise 4
Suppose there is a file with three values per line.
The values are white space separated as follows.
OwnerName ComputerType ComputerValue
Read the lines and make a dictionary of dictionaries so the keys are the owner and the values are a dictionary consisting of the computer type as the key and the computer value as the value.
Finally, print the dictionary.

The dataset might look as follows:
Joe Desktop 500
Joe Laptop 200
Joe Desktop 400
Mary Desktop 200
Mary Laptop 800
Beth Laptop 500
Beth Tablet 250
Joe Tablet 250
The output might look as follows:

{
'Mary': {'Desktop': 200, 'Laptop': 800},
'Beth': {'Tablet': 250, 'Laptop': 500},
'Joe': {'Desktop': 900, 'Tablet': 250, 'Laptop': 200}
}"""


import sys
arquivo = sys.argv[1]

#NomeDono TipoComputador ValorComputador).

with open(arquivo,"r") as doc:

    catalogo = {}
    
    while True:
        linha = doc.readline()
        
        if not linha:
            break
            
        texto = linha.split()
        
        dono = texto[0]
        tipocomputador = texto[1]
        valorComputador = texto[2]
        
        if dono not in catalogo:
            catalogo[dono] = {}
        
        catalogo[dono][tipocomputador] = valorComputador
    
    
print(catalogo)
    
