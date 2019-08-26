class People:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        #格式的规范，比如调用字符串的大写
        return self.__name.upper()
    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, name):
        #do some legal examines
        self.__name = name

    # def set_name(self, name):
    #     self.__name = name
    @age.setter
    def age(self, age):
        self.__age = age

someone = People(name = 'Ken', age=33)
print(someone.name)
print(someone.age)
someone.name = 'Huayin'
someone.age = 1
print(someone.name)
print(someone.age)