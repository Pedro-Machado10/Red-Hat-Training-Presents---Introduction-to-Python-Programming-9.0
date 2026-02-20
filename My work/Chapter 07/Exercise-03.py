"""Exercise 3
Write a program that uses a loop to prompt the user and get an integer value.
The program should print the sum of all the integers entered.
If the user enters a blank line or any other line that cannot be converted to an integer, the program should handle this ValueError.
If the user uses Ctrl+C to terminate the program, then it should be trapped with a KeyboardInterrupt, and a suitable message should be printed."""

soma = 0

while True:
    try:
        texto = input("Digite um número: ")
        numero = int(texto)
        soma += numero
    
    except ValueError:
        print("você não digitou um número")
    except EOFError:
        print(soma)
        break
    except KeyboardInterrupt:
        print("Programa encerrado pelo usuario")
        break