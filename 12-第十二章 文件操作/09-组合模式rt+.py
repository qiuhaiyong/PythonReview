# 1. rt+模式
# 概述：r模式可以读取，+模式可以更新（读取或写入），所以rt+模式可读可写。
# 注意：r模式打开文件后，文件指针在起始位置。
# 备注：由于t是默认值，所以rt+中的t可以省略。
with open('a.txt', 'rt+', encoding='utf-8') as file:
    for line in file:
        print(line, end='')
    # seek(offset, whence)方法：用于改变文件对象指针的位置，参数说明如下：
    #   offset：偏移量，要移动多少距离
    #   whence：参考点，从哪里开始计算偏移，有三种取值：
    #       0：从文件开头计算（默认值）
    #       1：从当前位置计算
    #       2：从文件末尾计算
    #  注意：在文本模式下，不要随意去定位中文字符位置，否则可能破坏文件编码。
    file.seek(0, 2)
    file.write('你好')



