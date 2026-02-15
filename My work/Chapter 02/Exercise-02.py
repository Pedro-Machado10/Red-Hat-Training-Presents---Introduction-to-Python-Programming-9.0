"""Exercise 2
Rewrite the preceding exercise to additionally print out how many digits are in the number, if the number is an integer."""

n1 = input("Digite um número inteiro: ")

if n1.isdigit():
   n2 = int(n1)
   caracteres = len(str(n2))
   print("Voce digitou um número inteiro, o número é: ",n2, f"A numero tem uma quantidade de {caracteres} digitos")

else: 
    print("Você não digitou um número inteiro")