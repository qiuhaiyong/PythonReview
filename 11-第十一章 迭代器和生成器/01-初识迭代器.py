names = ['张三', '李四', '王五']
citys = ('北京', '上海', '深圳')
msg = 'hello'
print(names)
print(citys)
print(msg)

for item in names:
    print(item)


res = names.__iter__()
print(type(res))