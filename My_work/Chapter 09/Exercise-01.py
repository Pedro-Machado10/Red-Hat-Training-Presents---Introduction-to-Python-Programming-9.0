"""Exercise 1
Write list comprehensions to produce the following lists:
A list of elements 0,1,2,3,4,…,99
A list from the preceding comprehension of those values that are evenly divisible by 5."""

#nova_lista = [ RESULTADO_QUE_EU_QUERO  for  ITEM  in  LISTA_ORIGINAL  if  CONDIÇÃO ]

listanum = [ i for i in range(100)]
lista5 = [n for n in listanum if n % 5 == 0]
print(lista5)
