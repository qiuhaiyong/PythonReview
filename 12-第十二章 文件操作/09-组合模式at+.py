with open('a.txt', 'at+', encoding='utf-8') as file:
    file.seek(0, 0)
    result = file.read()
    file.write('\n' + result)
    print(result)
    print(type(result))

