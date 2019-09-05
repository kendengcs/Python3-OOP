class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayhi(self):
        print("Hi, my name is {}, and my age is {}".format(
            self.name, self.age
        ))

    @classmethod
    def test1(cls):
        print('这是一个类方法')
        cls.test2()

    @staticmethod #装饰器
    def test2(): #没有参数，所以不能调用其它的方法
        print('这是一个静态方法')

p1 = People(name='Jack', age= 20)
p1.sayhi()

p1.test1()

People.test1()
#People.sayhi()