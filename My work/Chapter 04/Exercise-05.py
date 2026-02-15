"""
Exercise 5
Write a calculator application that presents the following menu:

Calculator options:
      1. Add
      2. Subtract
      3. Multiply
      4. Divide
      5. Quit
The user is expected to enter a number from the above menu.

After choosing the operation, the user should be prompted twice for 2 numbers and the chosen operation performed on them with the result being displayed on the screen.

Each of the above options should be implemented as its own function.

"""

def soma(a,b):
       resultado = a + b
       return resultado

def menos(a,b):
       resultado = a - b
       return resultado

def multi(a,b):
       resultado = a * b
       return resultado

def divide(a,b):
       resultado = a /  b
       return resultado


#principal

escolha = 0
while escolha != 5:

      print("Escolha de um número de 1 a 5:")
      print("1. Soma\n2. subtração\n3. Multiplicação\n4. Divisão\n5. Sair")
      escolha = int(input())

      if escolha == 1:
            print("Digite dois números:")
            a = int(input())
            b = int(input())
            print(f"O resultado é: {soma(a,b)}")
            print("----------------------------------")

      elif escolha == 2:
            print("Digite dois números:")
            a = int(input())
            b = int(input())
            print(f"O resultado é: {menos(a,b)}")
            print("----------------------------------")

      elif escolha == 3:
            print("Digite dois números:")
            a = int(input())
            b = int(input())
            print(f"O resultado é: {multi(a,b)}")
            print("----------------------------------")

      elif escolha == 4:
            print("Digite dois números:")
            a = int(input())
            b = int(input())
            print(f"O resultado é: {divide(a,b)}")
            print("----------------------------------")

      elif escolha == 5:
            print("Você saiu das operaçoes!")
            print("----------------------------------")

      
      