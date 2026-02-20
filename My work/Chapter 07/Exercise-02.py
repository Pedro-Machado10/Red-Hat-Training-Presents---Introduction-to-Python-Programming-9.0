"""Exercise 2
Test Exercise 1 again by using a few negative numbers as the index.

Eliminate negative numbers as legitimate subscripts by raising the IndexError exception when a negative number is given."""

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