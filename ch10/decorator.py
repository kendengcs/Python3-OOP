import functools


def demo(f):

    @functools.wraps(f)#保护装饰完函数的属性，令其保持不变
    def f_new(*args, **kwargs):

        """
        this is f_new
        :param args:
        :param kwargs:
        :return:
        """
        print(f.__name__)
        return f(*args, **kwargs)
    return f_new

@demo
def test1(x,y):
    """
    this is test1
    :param x:
    :param y:
    :return:
    """
    print('x={}. y={}'.format(x, y))

test1(1,2)

print(test1.__name__)

print(test1.__doc__)