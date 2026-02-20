"""
Exercise 12
Write and test a function that takes a number and a dictionary and adds the number to all values in the dictionary.

You can assume that all the values in the dictionary are numbers.

"""

def somar(num,dicionario):
    
    for n in dicionario.keys():
        dicionario[n] += num



#PRINCIPAL 
items = {'carro': 100,
           'peão': 10,
           'arroz': 25,
           'teclado': 40,
           }

print("ANTES\n",items)
somar(10,items) 
print("--------------------\n DEPOIS")
print(items)
