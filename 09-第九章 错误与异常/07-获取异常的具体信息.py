print('欢迎使用本程序')
try:
    a = int(input('请输入第一个数：'))
    b = int(input('请输入第二个数：'))
    print(x)
    result = a / b
    print(f'{a}除以{b}的结果是：{result}')
except ZeroDivisionError:
    print('程序异常：0不能作为除数！')
except ValueError:
    print('程序异常：您输入的必须是数字！')
except Exception as e:
    print(f'⚠程序异常，异常信息：{e}')
    print(f'⚠程序异常，异常类型：{type(e)}')
    print(f'⚠程序异常，异常参数：{e.args}')
    print(f'⚠程序异常，异常的文件：{e.__traceback__.tb_frame.f_code.co_filename}')
    print(f'⚠程序异常，异常的具体行数：{e.__traceback__.tb_lineno}')
    # 通过 traceback 来回溯异常
    # import traceback
    # print(traceback.format_exc())
print('*******我是后续的其它逻辑1*******')
print('*******我是后续的其它逻辑2*******')