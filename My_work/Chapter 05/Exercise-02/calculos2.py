def validar_positivo():
    entrada = input("Digite um número inteiro positivo: ")
    
    if entrada.isdigit() and int(entrada) > 0:
        return int(entrada) 
    else:
        return 0 
    
    
def soma(*args):
    total = 0
    for n in args:
        total = total + n
    return total


def soma_e_media(*args):

    soma_e_media = ()
    total = 0
    for n in args:
        total += n
   
    media = total / len(args)
    soma_e_media = (total,media)

    return soma_e_media