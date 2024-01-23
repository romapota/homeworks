def print_hi(name):
    m1: set
    m2: set
    R: int
    R2: int
    r: int
    def one():#перебираем элементы каждого массива, если значения одного массива есть в другом, то добавляем в список
        return print(m1.intersection(m2))
    def two():#перебираем элементы каждого массива, если значения одного массива нет в другом, то добавляем в список
        return print(m1.symmetric_difference(m2))
    def three():#перебираем элементы первого массива, если значения первого массива нет во втором, то добавляем в список
        return print(m1.difference(m2))
    def four():#перебираем элементы второго массива, если значения втрого массива нет в первом, то добавляем в список
       print(m2.difference(m1))
    R = int(input('Количество элементов в первом списке '))
    R2 = int(input('Количество элементов во втором списке '))
    m1 = set()
    m2 = set()
    print('Заполнение первого списка')
    for i in range(R):
        r = int(input())
        m1.add(r)
    print('Заполнение второго списка')
    for i in range(R2):
        r = int(input())
        m2.add(r)
    one()
    two()
    three()
    four()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
