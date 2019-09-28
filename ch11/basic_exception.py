a = [10, 4, 3, 7, 11, 6, 0, 9, 22]

try:  #可能发生异常的语句，放在这里。
    b = [item for item in a if 100 % item == 0]
    print(b)
except ZeroDivisionError:
    print("zero cannot be divided.")

except TypeError:
    print("Type is wrong.")

except Exception:
    print("Anyway, something is wrong.")
print('done')