# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(count):
    m = []
    m_all = [m,]
    for i in range(count):
        r = int(input())
        m.append(r)
    for i in m:
        for j in m:
            for s in m:
                a = [i, j, s]
                if (a not in m_all) and (i != j != s) and (i!=j) and (i!=s) and (s!=j):
                    m_all.append(a)
    return print(m_all)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(int(input('Количество чисел: ')))