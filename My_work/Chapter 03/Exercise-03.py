"""Exercise 3
Write a program that creates a loop asking the user to input a number.
Repeat this process until the user enters the value end.
Enter each number into a set.
Before you enter the number, verify if the number is already in the set.
If the number is already in the set, then update a counter that tracks how many entries are not added to the set.
Just before the program ends, print the following:
The contents of the set on one line
The number of elements that were NOT added to the set on the second line"""


novoset = set()
naoadicionou = [] 

print("Digite vários números, quando quiser parar digite 'end'")
while True: 
    entrada = input()

    if entrada == "end":
        break
    numeros = int(entrada)

    if numeros in novoset:
        naoadicionou.append(numeros) 
    else:
            novoset.add(numeros)

print("Os números no seu set são: ",novoset)
print("Os numeros que não foram adicionados, pois estavam repetidos foram: ",naoadicionou)

