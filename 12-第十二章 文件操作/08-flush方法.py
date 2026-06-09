import time
with open('demo.txt', 'at', encoding='utf-8') as file:
    file.write('你好1')
    file.write('你好2')
    file.flush()
    time.sleep(5)
    file.write('你好3')
    file.write('你好4')