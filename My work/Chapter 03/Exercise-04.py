"""Exercise 4
Use a single set to determine the number of unique words in the user's input.
You can use the same sample while loop from Exercise 1.
Each time through the loop, the individual words should be added to the single set.
When done looping, output the contents of the set sorted alphabetically.
Also, output the number of unique words."""

words = set()

print("Digite frases ou palavras (ou 'end' para sair):")

while True: 
    entrada = input() 
    if entrada == "end":
        break
    
    dados = entrada.split()
    
    words.update(dados)

lista_ordenada = sorted(words)

print("\nAs palavras em ordem alfabética são:")
print(lista_ordenada)

print("\nA quantidade de palavras únicas é:")
print(len(words)) 