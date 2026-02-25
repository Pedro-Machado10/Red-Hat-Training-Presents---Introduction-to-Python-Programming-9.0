"""Exercise 6
Rewrite Exercise 4 to count the frequency of each word in the user's input.
• A dict provides the perfect data structure for this problem.
• Let the words be the keys, and let the counts be the values.
• Print the results sorted by the counts.
• Finally, print the results sorted by the words."""


palavras = {}
print("Digite frases ou palavras (ou 'end' para sair):")

while True: 
    entrada = input() 
    if entrada == "end":
        break
    
    dados = entrada.split()

for n in dados: #['pedro', 'pedro', 'pedro']
    if n in palavras:
        palavras[n] += 1
    else: 
        palavras[n] = 1

print("Em ordem alfabética:")
alfabeto = sorted(palavras.keys())
for n in alfabeto:
    print(f"A chave é: {n} | e o número de vezes que aparece é: {palavras[n]}") #palavra['key'] devolver o VALOR da chave em específico. 

print("--------------------------------------------------------------------------------")

print("Do menor para o maior valor")
valores = sorted(palavras,key=palavras.get)
for p in valores:
    print(f"{p}: {palavras[p]}")