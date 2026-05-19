def test1():
    print('******test1开始******')
    result = '100' + 100
    print('******test1结束******')

def test2():
    print('******test2开始******')
    try:
        test1()
    except Exception as e:
        print(f'程序异常：{e}')
    print('******test2结束******')

def test3():
    print('******test3开始******')
    test2()
    print('******test3结束******')

test3()
