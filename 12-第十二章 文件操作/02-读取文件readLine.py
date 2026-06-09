# 第一步：创建『文件对象』
file = open('a.txt', 'rt', encoding='utf-8')

# 第二步：操作文件（读取）
# 依次调用readline逐行读取
r1 = file.readline()
r2 = file.readline()
r3 = file.readline()
r4 = file.readline()
print(r1.strip())
print(r2.strip())
print(r3.strip())
print(r4.strip())

# 通过循环配合readline逐行读取
# while True:
#     line = file.readline()
#     if line == '':
#         break
#     # print(line.strip())
#     print(line, end='')

# 第三步：关闭文件
file.close()
