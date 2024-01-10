def print_hi(name):
    def one():
        for i in m1:
            if i in m2:
                numbers.add(i)
        for i in m2:
            if i in m1:
                numbers.add(i)
        return print(len(numbers), 'элемента: ', [i for i in numbers])
    def two():
        for i in m1:
            if i not in m2:
                numbers.add(i)
        for i in m2:
            if i not in m1:
                numbers.add(i)
        return print(len(numbers), 'элемента: ', [i for i in numbers])
    def three():
        for i in m1:
            if i not in m2:
                numbers.add(i)
        return print(len(numbers), 'элемента: ', [i for i in numbers])
    def four():
        for i in m2:
            if i not in m1:
                numbers.add(i)
        print(len(numbers), 'элемента: ', [i for i in numbers])
    R = int(input('Количество элементов в первом списке '))
    R2 = int(input('Количество элементов во втором списке '))
    m1 = set()
    m2 = set()
    for i in range(R):
        r = int(input())
        m1.add(r)
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