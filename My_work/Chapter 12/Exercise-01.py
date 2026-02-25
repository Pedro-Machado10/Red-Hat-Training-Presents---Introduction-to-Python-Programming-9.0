"""
Exercise - 01 
• Debug an example from previous chapters by starting the debugger from within the interactive Python shell.
• Step through the code by using a combination of the step and next commands to get used to their behavior."""

n1 = input("Digite um número inteiro: ")

if n1.isdigit():
   n2 = int(n1)
   print("Voce digitou um número inteiro, o número é: ",n2)

else: 
    print("Você não digitou um número inteiro")
