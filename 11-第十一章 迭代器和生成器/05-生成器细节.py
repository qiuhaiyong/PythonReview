# 写在『生成器函数』中的代码，需要通过『生成器对象』来执行：
#
# 1. 调用『生成器对象』的__next__方法，会让『生成器函数』中的代码开始执行。
# 2. 当『生成器函数』中的代码开始执行后，遇到yield会“暂停”，并会记录“暂停”的位置。
# 3. 后续调用__next__方法时，都会从上一次“暂停”的位置，继续运行，直到再次遇到 yield。
# 4. 遇到return会抛出StopIteration异常，并将return后面的表达式，作为异常信息。
# 5. yield后面所写的表达式，会作为本次__next__方法的返回值。

def demo():
    print('demo函数开始执行了')
    print(100)
    yield '我是第1个yield所返回的数据'
    a = 200
    print(a)
    yield '我是第2个yield所返回的数据'
    b = 300
    print(b)
    return '尚硅谷'

# d = demo()
# r1 = next(d)
# print(r1)
# r2 = next(d)
# print(r2)
# try:
#     next(d)
# except StopIteration as e:
#     print(e)




def demo():
    print('demo函数开始执行了')
    print(100)
    yield '我是第1个yield所返回的数据'
    a = 200
    print(a)
    yield '我是第2个yield所返回的数据'
    b = 300
    print(b)
    return '尚硅谷'

d = demo()
# 验证：生成器对象d，和迭代器一样，也拥有：__iter__  和 __next__ 方法
# print(hasattr(d, '__iter__'))
# print(hasattr(d, '__next__'))

# 验证：生成器对象的__iter__方法，和迭代器一样，返回的也是自身
# result = iter(d)
# print(result == d)

# for循环遍历生成器
# for item in d:
#     print(item)

# for循环背后的逻辑
gen = iter(d)
while True:
    try:
        value = next(gen)
        print(value)
    except StopIteration:
        break


# yield也能写在循环里
def create_car(total):
    for index in range(1, total + 1):
        yield f'我是第{index}台车'

# cars是生成器对象
cars = create_car(5)

# 调用一次cars的__next__方法，就会得到一台车
c1 = next(cars)
print(c1)
c2 = next(cars)
print(c2)
c3 = next(cars)
print(c3)
c4 = next(cars)
print(c4)
c5 = next(cars)
print(c5)

for car in cars:
    print(car)




# yield from能把一个『可迭代对象』里的东西依次yield出去。(替代：for + yield)
def demo():
    nums = [10, 20, 30, 40]
    yield from nums

d = demo()
r1 = next(d)
print(r1)
r2 = next(d)
print(r2)
r3 = next(d)
print(r3)
r4 = next(d)
print(r4)

for item in d:
    print(item)


# 使用：生成器.send(值) 可以让生成器继续执行的同时，给上一次yield传值。
# 备注1：next只能取值，send既能取值，也能送值。
# 备注2：第一次启动生成器，不能传值！（或者说只能传 None 值）

def demo():
    print('demo函数开始执行了')
    print(100)
    a = yield '我是第1个yield所返回的数据'
    print(a)
    b = yield '我是第2个yield所返回的数据'
    print(b)
    return '尚硅谷'

d = demo()
r1 = next(d) # 此处等价于 d.send(None)
print(r1)
r2 = d.send(666)
print(r2)
try:
    d.send(888)
except StopIteration as e:
    print(e)