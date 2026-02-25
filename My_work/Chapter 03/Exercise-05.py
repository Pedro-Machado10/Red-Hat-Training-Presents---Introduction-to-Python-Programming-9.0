"""
exercise 5
Use a dictionary to create a mapping from the digits 0-9 to the words zero, one, two, etc.
• Next, ask the user to input a number.
• If the user enters 1437, then the program should print one four three seven.

"""


numeros = {'0': 'zero',
           '1': 'um',
           '2': 'dois',
           '3': 'três',
           '4': 'quatro',
           '5': 'cinco',
           '6': 'seis',
           '7': 'sete',
           '8': 'oito',
           '9': 'nove'}

print("digite um número que colocarei por extenso")
num = input()

separa = list(num)
#print(separa)

for n in separa: 
    print(numeros[n], end=" ")