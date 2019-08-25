class Dog:

    def __init__(self, brand, name):
        self.brand = brand
        self.name = name

    def wow(self):
        print("{} is a {} dog, and it says 'bow wow wow'".format(self.name, self.brand))

Peter = Dog (brand='huski', name = 'Peter')
Peter.wow()