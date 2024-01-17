def print_hi(name):
    s = str(input())
    m = []
    str_n = ''
    for i in s:
        if i not in str_n:#если буква уникальна, то добавляется
            str_n += i
        else:#иначе временный список сбрасывается и начинается новый
            m.append(str_n)
            str_n = ''
            str_n += i
    m.append(str_n)
    return print(max(m))#нахождение максимальной подстроки

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
