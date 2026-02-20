"""Exercise 1
    Create a class called Person.
    Each Person should have a name, an age, and a gender.
    In addition to getters and setters for the above methods, the Person class must have an __init__() method and a __str__() method.
    The __init__() and __str__() methods must be defined such that the following can be tested inside of an application.
    p1 = Person("Michael", 45, "M")
    print(p1)"""


class Person:
    def __init__(self, nome,idade,gender):
        self.nome = nome
        self.idade = idade
        self.gender = gender
    
    def __str__(self):
        return f"Nome: {self.nome} | Idade: {self.idade} | Gênero: {self.gender}"
    
#Programa principal

usuario1 = Person("Pedro","20","Masculino")
print(usuario1)