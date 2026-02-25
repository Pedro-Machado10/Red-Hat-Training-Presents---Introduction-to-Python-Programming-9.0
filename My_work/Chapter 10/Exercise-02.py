"""Exercise 2
Repeat the previous exercise, but this time use a floating point number.
A floating point number should have at least one digit to the left and to the right of the decimal point.
Specify whether the number is positive or negative."""

#1.5 = exemplo

import re

while True:
    print("Digite um número decimal:")
    num = input()
    
    if not num:
        break
        
    padrao = "^[+-]?\d+[.]\d+$"
    resultado = re.search(padrao,num)
    
    if resultado:
        num_convertido = float(num)

    if resultado and num_convertido > 0:
        print("Numéro válido, ele é positivo")
    elif resultado and num_convertido < 0:
        print("Número válido, ele é negativo")
    else:
        print("Número inválido, não é decimal")