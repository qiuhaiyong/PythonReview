# 第一步：创建『文件对象』
file = open('a.txt', 'rt', encoding='utf-8')

# 第二步：操作文件（读取）
for line in file:
    print(line, end='')

# 第三步：关闭文件
file.close()