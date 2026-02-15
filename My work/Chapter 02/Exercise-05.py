"""
Exercise 5
Ask the user to input multiple numbers on one input line.
Split the numbers into a list.
Write a loop that examines each element of the list and displays the ones that are greater than zero.

"""

numeros = input("Digite vários números: ")
lista = numeros.split(" ")

for n in lista:
    nint = int(n)

    if nint > 0: 
        print(n)


