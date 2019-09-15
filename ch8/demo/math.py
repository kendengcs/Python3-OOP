# 模块 module


def my_sum(*args):

    result = 0
    for item in args:
        result += item

    return result
#print(my_sum(1, 2, 3, 4))

def my_max(*args):
    print('最大值')

def my_min(*args):
    print('最小值')

class People:

    def __index__(self, name, age):
        self.name = name
        self.age = age

MAX_NUM = 100

print(__name__)
if __name__ == '__main__': #程序执行的入口，被别人引用的时候 不会执行下面的。
    print('1+2+3+4=',my_sum(1,2,3,4))