import time
from multiprocessing import Queue, Process

# 创建一个队列（不限制大小，即：不设置容量上限）
q1 = Queue()

# 创建一个队列（最多能保存3个元素）
q2 = Queue(3)

# 1️⃣put方法：往队列里放数据（入队）
q1.put(10)
q1.put(20)
q1.put(30)

# 2️⃣get方法：从队列里取数据（出队）
value1 = q1.get()
value2 = q1.get()
value3 = q1.get()
print(value1)
print(value2)
print(value3)

# 3️⃣empty方法：判断队列是否为空
result = q1.empty()
print(f'q1 is empty?:{result}')

# 4️⃣full方法：判断队列是否已满
q1.put(10)
q1.put(20)
q1.put(30)
result = q1.full()
print(f'q1 is full?:{result}')

q2.put(100)
q2.put(200)
q2.put(300)
result = q2.full()
print(f'q2 is full?:{result}')

# 5️⃣qsize方法：获取队列长度
q1.put(10)
q1.put(20)
q1.put(30)
result = q1.qsize()
print(f'qi Size:{result}')

# 6️⃣队列具备等待模式
# q2.put(100)
# q2.put(200)
# q2.put(300)

# (1).当队列已满，继续 put，就会进入等待模式，等别人调用get方法，取走一个元素
# q2.put(400)
# print('放入完毕')

# (2).当队列已满，执行：put(元素, timeout=秒数)，就会等待指定秒数。
# q2.put(400, timeout=3)
# print('放入完毕')

# (3).put_nowait 方法，会直接向队列中添加元素，不会进入等待模式，若队列已满，会抛出异常。
# 备注：put_nowait 等价于 put(元素, block=False)，block的默认值为 True
# q2.put_nowait(400)
# q2.put(400, block=False)

# get读多了，也会进入等待模式
q2.get()
q2.get()
q2.get()


# (1).当队列已空，继续 get，就会进入等待模式。x
# q2.get()

# (2).当队列已空，执行 get(timeout=秒数)，就会等待指定秒数。
# q2.get(timeout=3)

# (3).get_nowait 方法，会直接读取队列中的元素，不会进入等待模式，若队列已空，会抛出异常
# 备注：get_nowait 等价于 get(block=False)
# q2.get_nowait()
# q2.get(block=False)