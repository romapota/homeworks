def print_hi(name):
    s = str(input())
    s.lower()
    m = []
    str_n = ''
    for i in s:
        if i != ' ':
            str_n += i
        else:
            if str_n != '':
                m.append(str_n.strip())
            str_n = ''
            if i != ' ':
                str_n += i
    m.append(str_n)
    m.reverse()
    n_m = ' '.join(m).capitalize()
    m = n_m.strip()
    return print(m)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')