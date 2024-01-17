def santa_users(name:int) -> dict:
    s = []
    nameSurnameIndex = []
    for i in range(name):#заполнение данных о пользователях
        name = str(input())
        index = str(input())
        s.append(name)
        s.append(index)
        nameSurnameIndex.append(s)
        s = []
    for i in nameSurnameIndex:
        if i[1] == '':#если вместо индекса пусто, то добавляется None
            i[1] = 'None'
    return print(dict(nameSurnameIndex))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    santa_users(int(input('Количество пользователей: ')))
