import os
import time
from concurrent.futures import ProcessPoolExecutor


def work(n):
    print(f'work正在执行任务{n}.........{os.getpid()}')
    time.sleep(1)
    return f'我是任务{n}的结果'

if __name__ == '__main__':
    print('---------start-------------')
    # 创建一个进程池执行器
    executor = ProcessPoolExecutor(3)
    # 使用 submit 方法提交任务（submit 只负责“提交任务”，不会阻塞主进程）
    # f1 = executor.submit(work, 1)
    # f2 = executor.submit(work, 2)
    # f3 = executor.submit(work, 3)
    # f4 = executor.submit(work, 4)
    # f5 = executor.submit(work, 5)
    # f6 = executor.submit(work, 6)
    # f7 = executor.submit(work, 7)
    futures = [executor.submit(work, index) for index in range(1, 8)]
    # 阻塞主进程，等待进程池中所有任务执行完毕。
    executor.shutdown(wait=True)
    # print(f1.result())
    # print(f2.result())
    # print(f3.result())
    # print(f4.result())
    # print(f5.result())
    # print(f6.result())
    # print(f7.result())
    for f in futures:
        print(f.result())
    print('---------end-------------')