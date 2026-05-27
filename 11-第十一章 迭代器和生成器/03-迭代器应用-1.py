class Person:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def __iter__(self):
        return PersonIterator(self)

class PersonIterator:
    def __init__(self, p):
        # 将外部传进来的数据保存好
        self.p = p
        # 设置迭代器的初始化状态（指针位置）
        self.index = 0
        # 配置好要遍历的内容
        self.attrs = [p.name, p.age, p.gender, p.address]

    # 迭代器的__iter__方法会返回迭代器自身
    def __iter__(self):
        return self

    # 每次调用__next__方法，会根据当前的状态，返回下一个元素
    def __next__(self):
        # 如果指针的位置超出范围，那就抛出StopIteration异常
        if self.index >= len(self.attrs):
            raise StopIteration
        # 获取要返回的内容
        value = self.attrs[self.index]
        # 更新迭代器状态（指针位置）
        self.index += 1
        # 返回value
        return value

# 目标：
p1 = Person('张三', 18, '男', '北京昌平')

for item in p1:
    print(item)

for item in p1:
    print(item)
