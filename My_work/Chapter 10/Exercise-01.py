"""Exercise 1
Write a program that reads a line at a time and determines whether the input consists solely of an integer number that is positive or negative.
Specify whether it is positive or negative."""

import re

while True:
    print("Digite um número:")
    num = input()
    
    if not num:
        break
        
    padrao = "^[+-]?\d+$"
    resultado = re.search(padrao,num)
    
    if resultado:
        num_convertido = int(num)

    if resultado and num_convertido > 0:
        print("Numéro válido, ele é positivo")
    elif resultado and num_convertido < 0:
        print("Número válido, ele é negativo")
    else:
        print("Número inválido")