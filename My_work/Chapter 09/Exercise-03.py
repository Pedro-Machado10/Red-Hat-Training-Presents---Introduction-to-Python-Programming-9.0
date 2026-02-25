"""Exercise 3
Write a dictionary comprehension that generates a dictionary of numbers and their factorials in the range (1,10).
Using that dictionary, multiply 6 factorial times 5 factorial."""

import math

dicionario = {n: math.factorial(n) for n in range(1,10)}
mult = dicionario[6] * dicionario[5]
print(mult)