import sys  #内置模块

if '/Users/kendeng/PycharmProjects/Python3-OOP' not in sys.path:
    sys.path.append('/Users/kendeng/PycharmProjects/Python3-OOP')
#print(sys.path)
from ch8.demo.math import my_sum

print(my_sum(1,2,3,4))