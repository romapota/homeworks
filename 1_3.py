from itertools import product
def get_pins():
    s = str(input('Строка: '))
    count = int(input('Количество строк: '))
    sp = []
    ss = ''
    indexRight = 0
    indexTop = -1
    flag_one = 0
    flag_two = 0
    for i in range(count):
        sp.append(['0' for _ in range(len(s))])
    for i in s:
        if flag_one == 0:
            indexTop += 1
        if indexTop == len(sp):
            flag_one = 1
            indexTop -= 1
        if flag_one == 1:
            if indexTop != 0:
                indexTop -= 1
                indexRight += 1
            else:
                flag_one = 0
                indexTop += 1
        flag_two = 0
        sp[indexTop][indexRight] = i
    for i in range(len(sp)):
        for j in range(len(sp[0])):
            if sp[i][j] != '0':
                ss += str(sp[i][j])
    return print(ss)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_pins()