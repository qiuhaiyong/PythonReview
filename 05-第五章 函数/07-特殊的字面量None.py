"""例如：msg = None 的含义是 —— 我先定义一个变量 msg，但目前还不知道它会存储什么类型的值，那能不能写成 msg = 0 呢？
这要看具体情况：
如果确定 msg 之后会存放数值类型的数据，那这样写是可以的。
但如果还不确定 msg 将来会存放什么类型的数据，最好不要写成 msg = 0，否则可能会误导别人以为它一定是数值类型。
"""

# None是一个特殊的字面量，它表示：空值 / 无值 / 无意义。
msg = None

# None 的类型是 NoneType。
print(type(msg))

# None 转为布尔值是 False。
print(bool(msg))
if not msg:
    print('你好')

# 不能参与数学运算，也不能与字符串拼接。
# result1 = msg + 1
# result1 = msg + 'hello'