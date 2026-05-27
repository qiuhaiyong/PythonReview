nums = [10, 20, 30, 40]

# 列表推导式
result1 = [n * 2 for n in nums]
print(result1)

# 生成器表达式（和列表推导式很像，不要搞混）
result2 = (n * 2 for n in nums)
print(result2)

for item in result2:
    print(item)