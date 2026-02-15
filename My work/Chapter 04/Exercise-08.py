"""
Exercise 8
Write a function that returns a nested function.
• When the nested function is executed it should return the sum of two integers.
• The two parameters should be passed to the outer function and used by the inner function.

"""

def funcao_pai(n1,n2):
    def filha():
        resultador = n1 + n2
        return resultador
    
    return filha

#PRINCIPAL 
print(funcao_pai(1,4))