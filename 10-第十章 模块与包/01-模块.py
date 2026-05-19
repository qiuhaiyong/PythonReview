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