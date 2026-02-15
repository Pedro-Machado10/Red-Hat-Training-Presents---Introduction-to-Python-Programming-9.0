"""

Exercise 1
Create a class called Person.

Each Person should have a name, an age, and a gender.

In addition to getters and setters for the above methods, the Person class must have an __init__() method and a __str__() method.

The __init__() and __str__() methods must be defined such that the following can be tested inside of an application.

p1 = Person("Michael", 45, "M")
print(p1)
Exercise 2
Create a class called Family.

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

Note the add method in the Family class.

Exercise 3
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
    print("we have fewer kids than smiths")
Exercise 4
Implement the following class hierarchy.

Define a Worker class with a name, a salary, and number of years worked.

Provide a method called pension that returns an amount equal to the years worked times 10% of the salary.

Implement a name() method in the Worker class and have this be a default method for all derived classes.

Derive Manager from Worker.

A manager's pension is defined by the number of years worked times 20% of the salary.

Derive Executive from Manager.

An executive's pension is defined by the number of years worked times 30% of the salary.


"""

