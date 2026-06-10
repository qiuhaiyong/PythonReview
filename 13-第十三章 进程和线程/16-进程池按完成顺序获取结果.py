import os
import time
from concurrent.futures import ProcessPoolExecutor, as_completed


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
    # 使用 submit 方法提交任务（submit 只负责“提交任务”，不会阻塞主进程）
    futures = [executor.submit(work, index) for index in range(1, 8)]
    # 准备一个 result_list 去收集任务的具体结果
    result_list = []
    # 收集每个任务的结果
    for f in as_completed(futures):
        result_list.append(f.result())
    # 阻塞主进程，等待进程池中所有任务执行完毕。
    executor.shutdown(wait=True)
    # 打印最终的结
    print(result_list)
    print('---------end-------------')
