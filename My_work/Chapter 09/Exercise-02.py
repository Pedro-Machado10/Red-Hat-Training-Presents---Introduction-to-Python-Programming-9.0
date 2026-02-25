"""Exercise 2
Write a list comprehension to create a list of tuples, of x and the factorial of x, for the numbers from 5 to 10 inclusive.
The math module has a factorial() function that can be used."""

#nova_lista = [ RESULTADO_QUE_EU_QUERO  for  ITEM  in  LISTA_ORIGINAL  if  CONDIÇÃO ]

import math

listatup = [(n,math.factorial(n)) for n in range(5,11)]
print(listatup)