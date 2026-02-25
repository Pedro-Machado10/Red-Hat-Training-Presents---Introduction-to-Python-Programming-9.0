"""Exercise 4
Write a program that asks the user to enter a sentence.
The program should determine and print the following information:
The first character in the string of text and the number of times it occurs in the string.
The last character in the string of text and the number of times it occurs in the string."""


frase = input("Escreva uma frase: ")
print("O primeiro caractere da frase é: " + frase[0]) 
print("O numero de vezes que ele aparece é: ", frase.count(frase[0]))
print("O ultimo caractere da frase é: " + frase[-1])
print("O numero de vezes que ele aparece é: ", frase.count(frase[-1]))