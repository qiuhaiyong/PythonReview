with open('demo1.txt', 'xt+', encoding='utf-8') as file:
    file.write('你好')
    file.seek(0, 0)
    result = file.read()
    print(result)
