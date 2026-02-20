"""
Exercise 11
Write and test a function that takes two lists as parameters and returns a list of the elements that are common to both.
"""

def intercecao(lista1,lista2):
    listatotal = []
    for n in lista1:
        listatotal.append(n)
    for n in lista2:
        listatotal.append(n)
        
    lista3 = []
    for n in listatotal:
        if n in lista1 and n in lista2:
            if n in lista3:
                pass
            else:
                lista3.append(n)
    
    return lista3


#PROGRAMA PRINCIPAL 
lista1 = ["pedro","marcelo","maria","Alan minda","jarvis","Hulk"]
lista2 = ["pedro","mariana","maria","alan Kardec","jemerson","Hulk"]

resultado = intercecao(lista1,lista2)
print(resultado)