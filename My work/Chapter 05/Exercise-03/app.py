import sys

# script de teste: python app.py Pedro Marcelo Ana Julia

def main():
    lista = sys.argv
    print(lista)
    nomes = lista[1:]
    nomes.sort()
    print("Nomes em ordem alfabética:", nomes)
    

if __name__ == "__main__":
    main()