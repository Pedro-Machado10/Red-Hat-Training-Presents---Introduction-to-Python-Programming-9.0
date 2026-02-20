"""Exercise 4
Implement the following class hierarchy.
Define a Worker class with a name, a salary, and number of years worked.
Provide a method called pension that returns an amount equal to the years worked times 10% of the salary.
Implement a name() method in the Worker class and have this be a default method for all derived classes.
Derive Manager from Worker.
A manager's pension is defined by the number of years worked times 20% of the salary.
Derive Executive from Manager.
An executive's pension is defined by the number of years worked times 30% of the salary.
"""

class Worker():
    def __init__(self,name,salary,numworked):
        self.name = name
        self.salary = salary
        self.numworked = numworked
        
    def pension(self):
        pension = self.numworked * (self.salary / 10)
        return pension
        
        
class Manager(Worker):
    def __init__(self,name,salary,numworked):
        super().__init__(name,salary,numworked)
    
    def pension(self):
        pension = self.numworked * (self.salary * 0.2)
        return pension
        
class Executive(Manager):
     def __init__(self,name,salary,numworked):
        super().__init__(name,salary,numworked)
     def pension(self):
        pension = self.numworked * (self.salary * 0.3)
        return pension


trabalhador = Worker("Pedro",1000,1)
posentadoria = trabalhador.pension()
print(posentadoria) 

gerente = Manager("Davi",1000,1)
pos1 = gerente.pension()
print(pos1) 

executivo = Executive("ARTHUR",1000,1)
pos2 = executivo.pension()
print(pos2) 

