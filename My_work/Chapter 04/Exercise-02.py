"""
Exercise 2
Write and test a function that takes a collection of strings and returns the length of the longest string in the collection.

The application should loop through the collection of strings and rely on the value returned by the function to 
format all of the strings to the output such that they are all right justified to the width of the longest string.

"""


def comprimento_da_string(lista_string): 
    contagem = 0
    maior = 0
    for n in lista_string: 
        contagem = len(n)
        if contagem > maior:
            maior = contagem
            string = n
    return maior
    
#Progama principal

lista = ["Pedro", "PUC", "coração"]
largura = comprimento_da_string(lista)

print(f"Alinhando à direita com largura {largura}:\n")
for palavra in lista:

    print("{:>{}}".format(palavra, largura)) #{1} onde a variavel sera colocada (padrão) {:>} indica o alinhamento dessa variavel, 

