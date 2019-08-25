class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayhi(self):
        print ("Hi, my name is {}, and my age is {}".format(self.name, self.age))


someone = People(name = 'Ken', age ='33')
someone.sayhi()