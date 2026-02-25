"""Exercise 3
Write a program that prompts twice for an integer.
The program should print the larger of the two numbers.
If the numbers are equal, then the program should indicate it as such."""

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))

if n1 > n2: 
    print(f"O número {n1} é maior que o {n2}")
elif n2 > n1: 
    print(f"O número {n2} é maior que o {n1}")
else: 
    print("Os números são iguais")

