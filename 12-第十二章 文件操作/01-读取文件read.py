# 第一步 创建【文件对象】
file = open(file='a.txt', mode='rt', encoding='utf-8')

# 第二步 操作文件（读取）
# result = file.read()
# print(result)

# 多次调用read去逐步读取文件
# r1 = file.read(2)
# r2 = file.read(3)
# r3 = file.read(4)
# r4 = file.read()
# print(r1, end='')
# print(r2, end='')
# print(r3, end='')
# print(r4, end='')

# 用循环配合多次read（对内存友好）
while True:
    result = file.read(10)
    if result == '':
        break
    print(result, end='')

# 第三步 关闭文件
file.close()
