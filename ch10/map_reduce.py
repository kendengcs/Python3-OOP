a = [1, 2, 3, 4]

#print([item for item in map(lambda x: x* x, a)])

from functools import reduce

a = reduce(lambda x, y: x+y, a)
print(a)