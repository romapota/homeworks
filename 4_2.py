import itertools
def print_hi(count) -> list:
    m: list
    m_all: list
    m_new: list
    m = []
    m_all = [m,]
    for i in range(count):
        r = int(input())
        m.append(r)
    m_all = list(itertools.permutations(m))#находим все перестановки
    m_new = []
    for i in m_all:
        if [x for x in i] not in m_new:#если такой перестановки нет в новом списке, то добавляем ее
            m_new.append([x for x in i])
    return print(m_new)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(int(input('Количество чисел: ')))
