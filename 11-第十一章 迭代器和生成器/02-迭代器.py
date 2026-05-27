names = ['张三', '李四', '王五']
it = iter(names)
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

print(next(it))
print(next(it))
print(next(it))
# print(next(it))



names = ['张三', '李四', '王五']

it = iter(names)
print(it)

result = iter(it)
print(result)

x = iter(result)
print(x)

it = iter(names)
for item in it:
    print(item)