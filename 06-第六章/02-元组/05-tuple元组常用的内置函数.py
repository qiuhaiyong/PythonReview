# 常用内置函数
# max 函数，返回元组中的最大值
t1 = (23, 11, 32, 30, 17)
result = max(t1)
print(result)  # 32

# min 函数，返回元组中的最小值
t1 = (23, 11, 32, 30, 17)
result = min(t1)
print(result)  # 11

# len 函数，返回元组中元素的个数（元组长度）
t1 = (23, 11, 32, 30, 17)
result = len(t1)
print(result)  # 5

# sorted 函数，对元组进行排序（不修改原元组，返回一个新的列表）
t1 = (23, 11, 32, 30, 17)
result = sorted(t1, reverse=True)
print(tuple(result)) # (32, 30, 23, 17, 11)

# sum 函数，统计元组中所有元素的和（元素必须是纯数字）
t1 = (23, 11, 32, 30, 17)
result = sum(t1)
print(result) # 113