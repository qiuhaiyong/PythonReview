def demo():
    print('demo函数开始执行了')
    print(100)
    yield
    a = 200
    print(a)

d = demo()
print(d)