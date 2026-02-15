"""
Exercise 6
Write and test a function that receives a list as its only parameter and returns a new list of the positive elements only.

"""

def num_positivos(lista):

    lista_apenas_positivos = []

    for n in lista:
        if n > 0:
            lista_apenas_positivos.append(n)

    return lista_apenas_positivos

    
#PROGRAMA PRINCIPAL

numeros = [1,2,3,-1,-2,-3,-4,-5,-6]

resultado = num_positivos(numeros)
print(resultado)