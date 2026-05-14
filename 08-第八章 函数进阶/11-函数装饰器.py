# 概述：装饰器是一种在【不修改原函数代码】的前提下，对函数进行【增强】的工具。 它是 Python 中非常强大的语法特性，常用于：日志、校验、计时、缓存、权限控制等。
# 核心语法： 装饰器是一种可调用对象（通常是函数），接收一个函数作为参数，并返回一个新函数。
# def say_hello(func):
#
#     def wrapper(*args, **kwargs):
#         print("hello===================")
#         return func(*args, **kwargs)
#     return wrapper
#
#
# def add(x,y):
#     res = x + y
#     print(f"{x}和{y}相加的结果是{res}")
#     return res
#
# add_pro = say_hello(add)
#
# add_pro(1,2)


# 语法糖写法

def say_hello(msg):
    def outer(func):
        def wrapper(*args, **kwargs):
            print(f"hello==================={msg}")
            return func(*args, **kwargs)
        return wrapper
    return outer

@say_hello('加法')
def add(x,y):
    res = x + y
    print(f"{x}和{y}相加的结果是{res}")
    return res
@say_hello('减法')
def sub(x, y):
    res = x - y
    print(f"{x}和{y}相减的结果是{res}")
    return res

add(10,20)
sub(10,20)


