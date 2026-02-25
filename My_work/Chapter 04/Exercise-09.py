"""Exercise 9
    Re-write your solution to Exercise 8 such that the outer function receives no parameters, and the nested function is defined as taking the two parameters."""

def funcao_pai():
    def filha(n1,n2):
        resultador = n1 + n2
        return resultador
    
    return filha

#PRINCIPAL 

soma = funcao_pai()
oi = soma(5,5)
print(oi)