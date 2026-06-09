# 1 w模式
# w模式是写入模式，写入前会先截断文件（清空文件
with open('b.txt', 'wt', encoding='utf-8' ) as file:
    file.write('你好66666666666666')


# 2 x模式
# x模式是排它性创建，如果文件已存在，则创建失败。
# with open('demo.txt', 'xt', encoding='utf-8') as file:
#     file.write('你好')

# 3 a模式
# 打开文件用于写入，如果文件存在，则在文件末尾追加内容。
with open('b.txt', 'at', encoding='utf-8') as file:
    file.write('\n你好')

