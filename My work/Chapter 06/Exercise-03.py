"""Exercise 3
Implement the necessary special methods so that the <, ==, and > operators can be used with Family objects.
The criteria for the methods should be the number of children.
The following code could be used to test the methods:
myFamily = Family(mom, dad, kid1, kid2)
smiths = Family(mom, dad, kid1)
if (myFamily > smiths):
    print("we have more kids than smiths")
if (myFamily == smiths):
    print("families have same # of kids")
if (myFamily < smiths):
    print("we have fewer kids than smiths")"""


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
    
    def __gt__(self,other):
         return len(self.criancas) > len(other.criancas)
             
    def __eq__(self, other):
        return len(self.criancas) == len(other.criancas)
        
            
class Person:
    def __init__(self, nome,idade,gender):
        self.nome = nome
        self.idade = idade
        self.gender = gender
    
    def __str__(self):
        return f"Nome: {self.nome} | Idade: {self.idade} | Gênero: {self.gender}"


#PROGRAMA PRINCIPAL 

mom = Person("Mom", 45, "F")
dad = Person("Dad", 45, "M")
kid1 = Person("Johnie", 2, "M")
kid2 = Person("Janie", 3, "F")

myFamily = Familia(mom, dad, kid1, kid2)
smiths = Familia(mom, dad, kid1,kid2)

if (myFamily > smiths):
    print("we have more kids than smiths")
if (myFamily == smiths):
    print("families have same # of kids")
if (myFamily < smiths):
    print("we have fewer kids than smiths")