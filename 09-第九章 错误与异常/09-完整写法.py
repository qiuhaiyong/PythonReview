print('欢迎使用本程序')
try:
    a = int(input('请输入第一个数：'))
    b = int(input('请输入第二个数：'))
    result = a / b
    print(f'{a}除以{b}的结果是：{result}')
except (ZeroDivisionError, ValueError, Exception) as e:
    if isinstance(e, ZeroDivisionError):
        print('程序异常：0不能作为除数！')
    elif isinstance(e, ValueError):
        print('程序异常：您输入的必须是数字！')
    else:
        print(f'程序异常：{e}')
else:
    print('挺好的，try中的代码没有任何异常！')
finally:
    print('无论有没有异常，我的计算都结束了！')
print('*******我是后续的其它逻辑1*******')
print('*******我是后续的其它逻辑2*******')
