"""
Exercise 3
There is a built-in function in Python called sum that will return the sum of all of the numbers of an iterable object.

Write a similar function, but instead of taking a collection as a parameter, the function should take a variable number of arguments and return the sum of them.

"""

def soma(*args):
    total = 0
    for n in args:
        total = total + n
    return total

#principal

resultado = soma(6,6)
print(resultado)