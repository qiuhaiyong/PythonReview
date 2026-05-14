# continue跳过本次循环进入下一次循环
for day in range(1, 5):
    print(f'********第{day}天********')
    print('吃饭')
    if day == 2:
        continue
    print('睡觉')


# break停止循环
for day in range(1, 5):
    print(f'********第{day}天********')
    print('吃饭')
    if day == 2:
        break
    print('睡觉')