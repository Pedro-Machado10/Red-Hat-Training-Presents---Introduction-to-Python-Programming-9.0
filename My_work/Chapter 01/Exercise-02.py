"""Exercise 2
Write a program that prompts twice for text from the user.
The first input should be a first name.
The second input should be a last name.
The program should print the full name on one line and the person's initials on the second line."""


name = input("Digite seu primeiro nome: ")
name2 = input("Digite seu segundo nome: ")
print(name + " " + name2)
print("A letra inicial do seu nome é: " + name[0])