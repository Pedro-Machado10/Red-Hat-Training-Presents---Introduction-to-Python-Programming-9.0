"""Exercise 1
Create a program that reads books.json.
Prompt the user to enter a book title until they decide to quit.
If the title is in the JSON data, print the data for that book.
If the book is not in the JSON data, the program must indicate it.
Sample output:

Enter the title of a book (q to quit): Odyssey
Odyssey Info:
  year: 800
  pages: 374
  language: Greek
  author: Homer
  country: Greece"""
  
  
import json

with open("books.json","r") as arquivo:
  
  catalogo = json.load(arquivo)
  
while True:
    print("Digite um título de livro, se não quiser mais digite 'quit'")
    livro = input()

    if livro == 'quit':
      break
    
    if livro in catalogo:
      print("O livro está presente no catalogo:",livro)
      for chave,valor in catalogo[livro].items():
        print(f"{chave:<8}:{valor:>18}")
    else:
      print("O livro não está presente")