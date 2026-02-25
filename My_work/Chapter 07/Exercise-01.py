"""
Exercise 1
Create a list in your program that has 10 numbers.
Then, in a loop, ask the user for a number.
Use this number as an index into your list and print the value located at that index.
End the program when the user enters end.
Handle the case of an illegal number.
Handle the case of an illegal subscript."""

lista = [1,2,3,4,5,6,7,8,9,10]

while True:
    
    try:
        texto = input("Digite uma posição na lista de 0 - 9 (ou 'end' para sair): ")
        
        if texto == 'end':
            break
        indice = int(texto)
        if indice < 0:
            raise IndexError("Índices negativos não são permitidos")
        
        print(lista[indice])
    
    except ValueError:
        print("Não digite letras, apenas números")
    except IndexError as erro:
        print(f"Erro detectado: {erro}")
        
