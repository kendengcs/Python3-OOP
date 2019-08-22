z = 1

def demo2(a):
    global z #变成全局变量，最终的z是看最后z值，无论在不在函数体里。
    z = z + a
    print(z)

demo2(a = 10)

print(z)