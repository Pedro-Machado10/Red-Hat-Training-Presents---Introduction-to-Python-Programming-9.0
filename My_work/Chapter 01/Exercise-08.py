"""Exercise 8
Write a program that prompts the user twice for a number.
The first number will be the base, and the second number will be the exponent.
Print the result of raising the base to the exponent."""

base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))

resultado = base ** expoente
print("O resultado da operação é: ", resultado)