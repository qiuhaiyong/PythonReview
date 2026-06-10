import os
import time
from concurrent.futures import ProcessPoolExecutor


def work(n):
    print(f'work正在执行任务{n}.........{os.getpid()}')
    if n == 1:
        time.sleep(15)
    elif n == 2:
        time.sleep(10)
    else:
        time.sleep(1)
    return f'我是任务{n}的结果'

if __name__ == '__main__':
    print('---------start-------------')
    # 创建一个进程池执行器
    executor = ProcessPoolExecutor(3)
    # 通过 map 方法批量提交任务（结果按照提交的顺序来）
    results = executor.map(work, [1, 2, 3, 4, 5, 6, 7])
    # 获取 results 生成器中的内容
    print(list(results))
    # 等所有任务都完成
    executor.shutdown(wait=True)
    print('---------end-------------')