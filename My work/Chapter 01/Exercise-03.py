"""
Exercise 3

Write a program that accepts a string from the user.
Determine and print the following information about the string:
Does it end in a period?
Does it contain all alphabetic characters?
Is there an 'x' in the string?
Create and print a new string that has all occurrences of e changed to E."""


frase = input("Escreva uma Frase: ")

print("A frase termina com ponto final?", frase.endswith("."))
print("A frase possui apenas letras do alfabeto?", frase.isalpha())
print("A frase possui a letra x?", "x" in frase)
print(frase.replace('e','E'))


