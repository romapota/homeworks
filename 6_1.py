def print_hi(name):
    m1: list
    m2: list
    R: int
    R2: int
    numbers: tuple
    r: int
    def one():#перебираем элементы каждого массива, если значения одного массива есть в другом, то добавляем в список
        for i in m1:
            if i in m2:
                numbers.add(i)
        for i in m2:
            if i in m1:
                numbers.add(i)
        return print(len(numbers), 'элемента: ', [i for i in numbers])
    def two():#перебираем элементы каждого массива, если значения одного массива нет в другом, то добавляем в список
        for i in m1:
            if i not in m2:
                numbers.add(i)
        for i in m2:
            if i not in m1:
                numbers.add(i)
        return print(len(numbers), 'элемента: ', [i for i in numbers])
    def three():#перебираем элементы первого массива, если значения первого массива нет во втором, то добавляем в список
        for i in m1:
            if i not in m2:
                numbers.add(i)
        return print(len(numbers), 'элемента: ', [i for i in numbers])
    def four():#перебираем элементы второго массива, если значения втрого массива нет в первом, то добавляем в список
        for i in m2:
            if i not in m1:
                numbers.add(i)
        print(len(numbers), 'элемента: ', [i for i in numbers])
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
    numbers = set()
    one()
    numbers.clear()
    two()
    numbers.clear()
    three()
    numbers.clear()
    four()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
