def welcome():
    print('你好啊')
    def show_msg(msg):
        print(msg)
    return show_msg

result = welcome()
result('尚硅谷1')
welcome()('尚硅谷2')