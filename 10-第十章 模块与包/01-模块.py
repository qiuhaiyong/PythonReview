import order
import pay

print(order.max_order_amount)
order.create_order()
order.cancel_order()
order.show_info()

print('*' * 10)

print(pay.timeout)
pay.wechat_pay()
pay.ali_pay()
pay.show_info()

a = '116,117,112,111,108,107,106,101,100,99,98,97,96,95,94,93,92,91,90,88,89,87,86,85,84,83,81,79,80,78,77,76,75,74,73,72,70,71,69,68,67,66,65,64,63,62,61,60,59,58,57,56,54,55,53,52,51,50,48,49,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6'

res = a.split(',')

print(len(res))