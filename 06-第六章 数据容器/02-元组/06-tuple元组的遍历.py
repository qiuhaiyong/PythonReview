# 元组的循环遍历
t1 = (23, 11, 32, 30, 17)

# while循环遍历
index = 0
while index < len(t1):
    print(t1[index])
    index += 1

# 元组的循环遍历
t1 = (23, 11, 32, 30, 17)

# for循环遍历
for item in t1:
    print(item)


for index in range(len(t1)):
    print(t1[index])

for index,item in enumerate(t1,start=1):
    print(index,item)