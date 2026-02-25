"""Exercise 2
• Use the list command with no arguments at some point when debugging the preceding code again. Display the code around the currently executing line.
• Repeat the process by passing a range large enough to the list command to display the entire file on the screen."""

n1 = input("Digite um número inteiro: ")

if n1.isdigit():
   n2 = int(n1)
   print("Voce digitou um número inteiro, o número é: ",n2)

else: 
    print("Você não digitou um número inteiro")