name = '张三'
gender = '男'
weight = 65.2
age = 12

info1 = '我叫' + name + '，我是' + gender + '生'

info2 = '我叫%s，我是%s生，我体重是%f，年龄是%d' % (name, gender, weight, age)

# 推荐方式
info3 = f'我叫{name}，我是{gender}生，我体重是{weight}，年龄是{age}'

info4 = f'我叫{name}'