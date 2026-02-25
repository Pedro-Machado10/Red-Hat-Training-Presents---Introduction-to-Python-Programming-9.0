"""Exercise 1
Write a program that prompts for a lucky number. The program should print out a message if the number entered is not an integer."""

n1 = input("Digite um número inteiro: ")

if n1.isdigit():
   n2 = int(n1)
   print("Voce digitou um número inteiro, o número é: ",n2)

else: 
    print("Você não digitou um número inteiro")
