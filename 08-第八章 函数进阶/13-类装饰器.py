# 1 手动装饰
# class SayHello:
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print('你好，我要开始计算了')
#             return func(*args, **kwargs)
#         return wrapper
#
#
# def add(x, y):
#     res = x + y
#     print(f'{x}和{y}相加的结果是{res}')
#     return res
#
#
# say = SayHello()
# add = say(add)
# result = add(10, 20)


# 2 语法糖@
class SayHello:
    def __init__(self, msg):
        self.msg = msg

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f'你好，我要开始计算了{self.msg}')
            return func(*args, **kwargs)
        return wrapper

@SayHello('加法')
def add(x, y):
    res = x + y
    print(f'{x}和{y}相加的结果是{res}')
    return res

# 依然按照原本的方式调用，但调用的是被装饰后的新函数
result = add(10, 20)
print(result)