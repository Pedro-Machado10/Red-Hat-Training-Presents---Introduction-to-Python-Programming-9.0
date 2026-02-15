"""Exercise 8
Rewrite exercise # 4 such that the program takes into account the case where the first number entered is bigger than the last.
For example, if the user inputs the numbers 10 and 15, then the sum would be 75.
10 + 11 + 12 + 13 + 14 + 15 = 75
If the user inputs the numbers 15 and 10, then the sum would be still be 75."""

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))

total = 0

if n1 > n2: 
    maior = n1
    menor = n2
else: 
    maior = n2
    menor = n1

for variavel in range(menor,maior + 1): 
    total = variavel + total

print("O valor final da soma dos numeros é: ", total)