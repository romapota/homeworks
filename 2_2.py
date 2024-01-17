def print_hi(name) -> list:
    s = str(input())
    s.lower()#все символы преобразовавывает в маленькие
    m = []
    str_n = ''
    for i in s:
        if i != ' ':
            str_n += i#отделяем слова
        else:
            if str_n != '':
                m.append(str_n.strip())#добавляем другие строки удаляем пробелы 
            str_n = ''
            if i != ' ':
                str_n += i
    m.append(str_n)
    m.reverse()#переворот слов
    n_m = ' '.join(m).capitalize()#склеивание и первое слово с большой буквы
    m = n_m.strip()
    return print(m)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
