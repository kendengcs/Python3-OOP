class Animal:

    def eat(self):
        print('Animal is eating')

class Bird(Animal):
    pass

b = Bird()
b.eat()