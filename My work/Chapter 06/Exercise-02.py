"""Exercise 2
Create a class called Family
The Family does not extend Person but rather must be composed of two Person objects representing the parents and a list of Person objects representing the children.
Therefore, the __init__() method must take two required parameters (the parents), followed by a variable number of arguments (the children).
The following files are available in the AD141-apps repository, within the classes/starter directory, and you can use them in the exercise:
family_test.py
#!/usr/bin/env python3
def main():
    mother = Person("Mom", 45, "F")
    father = Person("Dad", 45, "M")
    kid1 = Person("Johnie", 2, "M")
    kid2 = Person("Janie", 3, "F")
    myFamily = Family(mother, father, kid1, kid2)
    kid3 = Person("Paulie", 1, "M")
    myFamily.add(kid3)
    print(myFamily)


if __name__ == "__main__":
    main()

Note the add method in the Family class."""


class Familia():
    def __init__(self,pai,mae,*args):
        self.pai = pai
        self.mae = mae
        self.criancas = list(args)
    
    def add(self,filho):
        self.criancas.append(filho)
        
    def __str__(self):
        
        lista_filhos = ""
        
        for n in self.criancas:
            lista_filhos += f"\n{n}"
            
        return f"Estrutura Familiar:\nResponsáveis:\n{self.pai}\n{self.mae}\nFilhos:{lista_filhos}"
    
    

class Person:
    def __init__(self, nome,idade,gender):
        self.nome = nome
        self.idade = idade
        self.gender = gender
    
    def __str__(self):
        return f"Nome: {self.nome} | Idade: {self.idade} | Gênero: {self.gender}"


#PROGRAMA PRINCIPAL 

mother = Person("Mom", 45, "F")
father = Person("Dad", 45, "M")
kid1 = Person("Johnie", 2, "M")
kid2 = Person("Janie", 3, "F")
myFamily = Familia(mother, father, kid1, kid2)
kid3 = Person("Paulie", 1, "M")
myFamily.add(kid3)
print(myFamily)
