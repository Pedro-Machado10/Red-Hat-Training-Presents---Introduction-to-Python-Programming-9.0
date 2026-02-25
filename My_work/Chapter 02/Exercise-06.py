"""Exercise 6
Ask the user to input three numbers representing a lower limit, a higher limit, and a step value.

The program should use a range object to loop through and print the numbers from low to high (inclusive), taking into consideration the step."""

print("digite um limite menor, maior e um valor de salto para pular entre os números")

lower = int(input())
high = int(input())
step = int(input())

for n in range(lower,high + 1,step): 
    print(n)

