def test1(func):
    print('我是test1装饰器')
    def wrapper(*args, **kwargs):
        print('test1追加的逻辑')
        res = func(*args, **kwargs)
        return res
    return wrapper

def test2(func):
    print('我是test2装饰器')
    def wrapper(*args, **kwargs):
        print('test2追加的逻辑')
        res = func(*args, **kwargs)
        return res
    return wrapper

@test1
@test2
def add(x, y):
    res = x + y
    print(f'{x}和{y}相加的结果是{res}')
    return res

result = add(10, 20)
print(result)