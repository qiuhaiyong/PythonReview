# 列表相加
list1 = [10, 20, 30, 40]
list2 = [50, 60, 70, 80]
list3 = list1 + list2
print(list3)  # [10, 20, 30, 40, 50, 60, 70, 80]、

# 元组相加
tuple1 = (10, 20, 30, 40)
tuple2 = (50, 60, 70, 80)
tuple3 = tuple1 + tuple2
print(tuple3)  # (10, 20, 30, 40, 50, 60, 70, 80)

# 字符换相加
str1 = 'hello'
str2 = 'atguigu'
str3 = str1 + str2
print(str3) # helloatguigu

# 错误示例
# list1 = [10, 20, 30, 40]
# str1 = 'hello'
# print(list1 + str1) # 报错