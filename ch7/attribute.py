class Student:

    count = 0 #类的属性

    def __init__(self, name):
        #self.name = name  #实例属性
        Student.count += 1
        self.name = name

s1 = Student('A')
s2 = Student('B')
s3 = Student('C')
print(Student.count)

# s1 = Student(name = 'A')
# print(s1.count)
# print(s1.name)
#
# s1.name = 'B'
# s1.count = 1
# print(s1.name)
# print(s1.count)
# print(Student.count)
#
# Student.count = 2
#
# print(Student.count)
# print(s1.count)