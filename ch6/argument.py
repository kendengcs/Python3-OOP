# def add(*args): #可变参数
#
#     result = 0
#     for item in args:
#         result += item
#     return result
#
# print(add(1,3,5,6,20,100))

# def add(**kwargs):
# #     #print(kwargs)
# #     #a + b * c
# #     return (kwargs.get('a') + kwargs.get('b') + kwargs.get('c'))
# # print(add(a = 1, b = 2, c = 3))


def test (a, b):
    print(a + b)

def add(x, **kwargs):

    if x==2:
        test(**kwargs)

add(x=2, a=2, b=3)

#add参数的修改不需要动到函数体本身的部分，只需要针对test增减变量即可。
#如果add函数体积很大的前提下，绕开改动add是一个很聪明的手段。