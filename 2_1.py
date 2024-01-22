def print_hi(name)->str:
    s: str
    m: list
    max_i : str
    s = str(input())
    m = []
    str_n = ''
    for i in s:
        if str(i) not in str_n:#если такая буква не входит в строку, то она добавляется
            str_n += str(i)
        else:#если входит, то строка добавляется в массив и обнуляется
            m.append(str_n)
            str_n = ''
            str_n += i
    m.append(str_n)
    max_i = ''
    for i in m:
        if len(i) > len(max_i):#берем за самый длинный элемент пустую строку и если новый элемент длинее, то меняем значение в переменной на новое
            max_i = i
    return print(max_i)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
