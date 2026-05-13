# 使用普通函数实现计算效果
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def calculate(func, a, b):
    print(f'计算结果为：{func(a, b)}')

calculate(add, 30, 10)
calculate(sub, 30, 10)

# 使用匿名函数实现计算效果
def calculate(func, a, b):
    print(f'计算结果为：{func(a, b)}')

calculate(lambda x, y: x + y, 30, 10)
calculate(lambda x, y: x - y, 30, 10)