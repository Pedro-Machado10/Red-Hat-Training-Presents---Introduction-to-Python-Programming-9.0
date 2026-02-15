"""
Exercise 2

Write a program that creates a loop asking the user to input a number.
Repeat this process until the user enters the value end.
The following can be used to loop through the user input.
prompt = "Enter a number (or the word 'end' to quit) "
while True:
    data = input(prompt)
    if data == "end":
        break
    #Remainder of while loop goes here
Add each iteration number to a list.
Just before the program ends, print the following:
The contents of the list on one line
The sum of the elements in the list on the second line

"""


lista = []
total = 0
print("Digite vários números, quando quiser parar digite 'end'")
while True: 
    valores = input()
    
    if valores == "end":
        break
    else: 
        lista.append(int(valores))

for n in lista:
    total = total + n
print("O total de números em sua lista é: ",lista)
print(f"O valor total da soma de todos os números é: {total}")