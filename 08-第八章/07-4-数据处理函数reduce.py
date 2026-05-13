from functools import reduce

# 数值统计
nums = [1, 2, 3, 4, 5]
result = reduce(lambda x,y : x + y, nums, 0)
print(result)


# 字符串拼接
str_list = ['ab', 'cd', 'ef']
result = reduce(lambda a, b: a + b, str_list)
print(result)