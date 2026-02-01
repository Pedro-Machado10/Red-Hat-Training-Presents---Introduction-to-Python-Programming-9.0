"""Exercise 7
Write a program that prompts the user for a string and then prompts again for a number.
The program should create and print a new string by using the repetition operator on the string and the number.
For example, if the string is hello and the number is 3, then hellohellohello should be printed."""

text = input("Digite um texto ")
n1 = int(input("Digite um número "))

print(text * n1)

"OBS: Tentando utilizar o float, a multiplicação não funciona, tem que ser um número inteiro"