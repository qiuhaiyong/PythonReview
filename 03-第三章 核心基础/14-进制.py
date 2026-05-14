# 0b开头表示二进制
num1 = 0b11001
# 0o开头表示八进制
num2 = 0o1034
# 0x开头表示十六进制
num3 = 0x1cf

# 📋备注：Python 中所有的『非十进制』数字，只是代码层面的编写方式，只是给程序员看的，Python 在进行：计算、打印等操作时，会自动将这些『非十进制』数字，转为『十进制』数字。
# 0b开头表示二进制
num1 = 0b11001
# 0o开头表示八进制
num2 = 0o1034
# 0x开头表示十六进制
num3 = 0x1cf

# Python 在对上面的 num1、num2、num3进行计算、打印等操作时，会自动将其转为十进制
print(num1, num2, num3)  # 25  540  463
print(num1 + 1)  # 26
print(str(num2)) # 540
print(num3 > 400) # True

# 进制转换
# bin() 十进制转二进制字符串
print(bin(3))
# oct() 十进制转八进制字符串
print(oct(10))
# hex() 十禁止转16进制字符串
print(hex(9))

print(int('0b10',2))
print(int('0o11',8))
print(int('0x11',16))
