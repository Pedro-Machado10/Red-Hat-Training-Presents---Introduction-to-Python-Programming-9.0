"""Assessment 2: High-Low Guessing Game
Goal: In the High-Low Guessing Game, the player attempts to guess an unknown number from 1 to 100. After each guess, the player is told whether their 
guess is too High (greater than the unknown number), or too Low (less than the unknown number). If they guess the number, they win.

Write a program that plays this game with the user. The program should accept guesses, rejecting any outside the range of 1 to 100 and any non-integer value. 
The program should track how many valid and invalid guesses were made, and print out both numbers at the end.

Sample Output provided in the material:
$ ./guess.py I'm thinking of a number from 1 to 100 Try to guess my number: 60 60 is too low - please guess again: 
Albuquerque Albuquerque is not a valid guess - please guess again: 90 90 is too high - please guess again: 
1776 1776 is not a valid guess - please guess again: 77 77 is correct! You guessed my number in 4 guesses and made 2 invalid guesses."""


import random

num_secreto = random.randint(1,100)
print(num_secreto)

print("Estou pensando em um numero de 0 a 100, tente acertar qual é:")

valido = 0
invalido = 0

while True:
    try: 
        num_usuario = int(input())
        
        if num_usuario < 1 or num_usuario > 100:
            print("Digitou um valor fora do combinado!")
            invalido += 1
            continue 
        
        valido += 1
        
        if num_usuario > num_secreto:
            print("Muito Alto! - Por favor tente novamente")
            valido += 1
        elif num_usuario < num_secreto:
            print("Muito Baixo! - Por favor tente novamente")
            valido += 1
        else:
            print(f"Você acertou o número em {valido} tentativas e escreveu {invalido} tentativas invalidas.")
            break
              
    except ValueError:
        print("Você digitou um valor errado")
        invalido += 1
        continue
