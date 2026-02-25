"""
Exercise 4
Rewrite the function in Exercise 3 above to return a tuple instead of a sum.

The tuple should be the sum and the average of all of the arguments passed to the function.

"""

def soma_e_media(*args):

    soma_e_media = ()
    total = 0
    for n in args:
        total += n
   
    media = total / len(args)
    soma_e_media = (total,media)

    return soma_e_media


#principal

resultado = soma_e_media(1,2,3)
print(resultado)