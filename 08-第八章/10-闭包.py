def outer():
    num = 10
    print(id(num)) # 140707460170952

    def inner():
        nonlocal num
        num += 1
        print(num)

    return inner

f = outer()


print(f.__closure__) # __closure__的值是一个元组，元组中保存着被inner函数所“挽救”下来的数据
print(f.__closure__[0].cell_contents) # 10
print(id(f.__closure__[0].cell_contents)) # 140707460170952


def outer():
    num = 10

    def inner():
        nonlocal num
        num += 1
        print(num)

    return inner

f1 = outer()
f1()
f1()
f1()
print(f1.__closure__[0].cell_contents,'=====') # 13
print('*****************')
f2 = outer()
f2()
print(f2.__closure__[0].cell_contents,'======') # 11
