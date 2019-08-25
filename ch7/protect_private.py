class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._protect_var = 10
        self.__private_var = 10

    def sayhi(self):
        print ("Hi, my name is {}, and my age is {}".format(self.name, self.age))

    def get_var(self):
        print(self.__private_var)

    def set_var(self, var):
        self.__private_var = var


someone = People(name = 'Ken', age =33)
someone.get_var()
someone.set_var(30)
someone.get_var()
someone._protect_var = 30
print(someone._protect_var)
print(dir(someone))