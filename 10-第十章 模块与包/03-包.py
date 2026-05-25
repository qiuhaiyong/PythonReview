
# 1. import 包名.模块名
# import trade.pay
# import trade.order
#
# trade.order.create_order()
# trade.pay.wechat_pay()


# 2. import 包名.模块名 as 别名
# import trade.pay as pp
# import trade.order as oo
#
# oo.create_order()
# pp.wechat_pay()

# ...........


# from trade import *
# order.create_order()
# pay.wechat_pay()

# ====================子包=============


# 1
# import trade.hello.hi
# trade.hello.hi.say_hello()

# 2
# import trade.hello.hi as dd
# dd.say_hello()

# 3
# from trade.hello.hi import say_hello
# say_hello()

# 4
# from trade.hello.hi import say_hello as hello
# hello()

# 5
# from trade.hello.hi import *
# say_hello()

# 6
# from trade.hello import hi
# hi.say_hello()

# 7
# from trade.hello import  hi as hello
# hello.say_hello()

# 8
# from trade.hello import *
# hi.say_hello()

# 9
import trade.hello
trade.hello.hi.say_hello()


from collections import Counter
names = ['张三','李四','王五','李四','李四']

res = Counter(names)
print(res)