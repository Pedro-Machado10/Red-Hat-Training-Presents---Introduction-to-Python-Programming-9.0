"""
Exercise 4
Write a program that prompts twice for an integer.
The program should output the sum of the integers within the range of those two numbers inclusively.
For example, if the user inputs the numbers 10 and 15, then the sum would be 75.
10 + 11 + 12 + 13 + 14 + 15 = 75
"""

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))

total = 0

for variavel in range(n1,n2 + 1): 
    total = variavel + total

print("O valor final da soma dos numeros é: ", total)