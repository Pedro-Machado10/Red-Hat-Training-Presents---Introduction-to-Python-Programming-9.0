"""Exercise 4
The following API endpoint returns JSON data that contains a random trivia fact about a number sent to it: http://numbersapi.com/a_number/?json&notfound=floor.
Write a program that makes an HTTP request to the API.
The program should display the fact that was returned in the JSON data.
Another endpoint will return mathematical data about a number:
http://numbersapi.com/a_number/math/?json&notfound=floor
sending request http://numbersapi.com/42/?json&notfound=floor...
42 is the result given by the web search engines Google, Wolfram Alpha and Bing when the query \"the answer to life the universe and everything\" is entered as a search."""

import json
import requests

print("Digite um número")
num = input()
url = f"http://numbersapi.com/{num}/math/?json&notfound=floor"
print(url)

dados = requests.get(url)
dicionario_api = dados.json()
print(dicionario_api)

print("\n--- Fato Curioso ---")
print(dicionario_api["text"])

