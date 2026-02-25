import sys #pega o que o usuario digitar PELO terminal

def main():
    
    soma = 0
    lista = sys.argv
    numeros = lista[1:]
    numerosint = []
    
    for n in numeros:
        num = int(n)
        numerosint.append(num)
    
    for n in numerosint:
        soma += n
    
    media = soma / len(numerosint)
    print("A media é:",media)


if __name__ == "__main__":
    main()