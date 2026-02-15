"""Exercise 1
Exercise 1
Write and test a function that is designed to validate input.
The function should prompt the user for a positive integer.
It should validate the information entered by the user is indeed a positive integer.
If number entered is valid, the function should return the number.
If the number entered is invalid, the function should return a zero (0) instead.
The application, not the function, should indicate with a message in the output each time an invalid entry is given.
"""

def validar_positivo():
    entrada = input("Digite um número inteiro positivo: ")
    
    if entrada.isdigit() and int(entrada) > 0:
        return int(entrada) 
    else:
        return 0 

#PROGRAMA PRINCIPAL 

resultado = validar_positivo()

if resultado == 0:
    print("Erro: Você não digitou um número válido!")
else:
    print(f"Muito bem! O número digitado foi {resultado}")