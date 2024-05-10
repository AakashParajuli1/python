# Multi level inheritance :
class Organism:           # Grandparent class

    alive = True


class Animal(Organism):     # Parent class inheriting from grandparent class

    def eat(self):
        print("This animal is eating")


class Dog(Animal):    # child class inheriting from parent class
    def bark(self):
        print("This dog barks.")


dog = Dog()               # declaring / defining objects
print(dog.alive)           # grandparent class variable is callable due to multilevel inheritance
dog.eat()                    # so is parent class method
dog.bark()                  # so is method within own class too
