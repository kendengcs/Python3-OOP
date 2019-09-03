class Animal:

    def eat(self):
        print('Animal is eating')

class Bird(Animal):
    def sing(self):
        print('Bird is singing...')

    def eat(self):
        print('Bird is eating')

class Dog(Animal):
    def eat(self):
        print('Dog is eating')

class Cat(Animal):
    # def eat(self):
    #     print('Cat is eating')
    pass
a = Animal()
# a.eat()
#
b = Bird()
# b.eat()
# b.sing()
#
d = Dog()
# d.eat()

c = Cat()

def demo_eat(a):
    a.eat()

for item in [a, b, c, d]:
    demo_eat(item)