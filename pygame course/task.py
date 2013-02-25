'''
Write code that defines a class named Animal:
Add an attribute for the animal name.
Add an eat() method for Animal that prints “Munch munch.”
A makeNoise() method for Animal that prints “Grrr says [animal name].”
Add a constructor for the Animal class that prints “An animal has been born.”

A class named Cat:
Make Animal the parent.
A makeNoise() method for Cat that prints “Meow says [animal name].”
A constructor for Cat that prints “A cat has been born.” and it calls the parent constructor.

A class named Dog:
Make Animal the parent.
A makeNoise() method for Dog that prints “Bark says [animal name].”
A constructor for Dog that prints “A dog has been born.” and it calls the parent constructor.

A main program with:
Code that creates a cat, two dogs, and an animal.
Sets the name for each animal.
Code that calls eat() and makeNoise() for each animal.
'''
class Animal():
    name = ""

    def __init__(self):
        print("An animal has been born")

    def eat(self):
        print("munch munch")
        
    def makeNoise(self):
        print(self.name)
    

class Cat(Animal):
    def __init__(self):
        print("A cat has been born")
        Animal.__init__(self)
        
    def makeNoise(self):
        print("Meow, says " + self.name)

class Dog():
    def __init__(self):
        print("A dog has been born")
        Animal.__init__(self)

    def makeNoise(self):
        print("Bark says " + self.name)

c1 = Cat()
c2 = Cat()
c1.name = "Mew1"
c2.name = "Mew2"

d1 = Dog()
d1.name = "lola"

c2.makeNoise()
c1.eat()
c2.eat()

