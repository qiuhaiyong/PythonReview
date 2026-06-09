# 第一步：创建『文件对象』
file = open('a.txt', 'rt', encoding='utf-8')
print(type(file))

# 第二步：操作文件（读取）
result = file.readlines(50)
print(result)
# result = file.readlines(1)
# print(result)


# 第三步：关闭文件
file.close()

