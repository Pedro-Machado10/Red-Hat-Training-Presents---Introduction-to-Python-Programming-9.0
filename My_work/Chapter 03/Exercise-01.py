"""Exercise 1
Given the following two lists:

first = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
second = ["day", "day", "sday", "nesday", "rsday", "day", "urday"]
Concatenate the two lists by index into a new list that, when printed, looks as follows:

["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]"""

first = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
second = ["day", "day", "sday", "nesday", "rsday", "day", "urday"]
semana = []

contador = 0

while contador <= 6:
   string = first[contador] + second[contador]
   semana.append(string)
   contador = contador + 1 #também pode usar dessa outra forma contador += 1

for c in semana:
   print(c, end=" ")

