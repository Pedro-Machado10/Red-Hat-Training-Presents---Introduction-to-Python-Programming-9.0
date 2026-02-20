"""
Exercise 10
    Re-write your solution to either Exercise 8 or 9 so that it uses a lambda expression as the nested function.

    """

def funcao_pai():
    return lambda n1, n2: n1 + n2 

#PROGRAMA PRINCIPAL 
ferramenta_soma = funcao_pai()
print(ferramenta_soma(5, 5)) 