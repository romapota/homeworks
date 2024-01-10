def print_hi(name):
    s = str(input())
    m = []
    str_n = ''
    for i in s:
        if i not in str_n:
            str_n += i
        else:
            m.append(str_n)
            str_n = ''
            str_n += i
    m.append(str_n)
    return print(max(m))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
