# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def sorted_word(word: str) -> str:
    m = [i for i in word]
    m_n = sorted(m)#сортировка массива
    new_word = ''.join(m_n)#создание строки
    return new_word
def print_hi(name: str) -> list:
    m = []
    m_n = []
    t = []
    R = int(input('Количество строк'))
    for i in range(R):
        r = str(input())
        m.append(r)
    for i in m:
        for j in m:
            if len(i) == len(j):
                n_i = sorted_word(i)#сортировка слов
                n_j = sorted_word(j)
                if n_j == n_i:#если слова равны, то добавляется в список
                    t.append(j)
        if t not in m_n:
            m_n.append(t)
        t = []
    return print(m_n)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
