from itertools import product
global all_n
all_n = []
def unzip(m):
    mm = []
    for elements in m:
        for elementsinelement in elements:
            if elementsinelement not in mm:
                mm.append(elementsinelement)
        mm.sort()
        if mm not in all_n:
            all_n.append(mm)
        mm = []
def print_hi(name):
    finish_all = set()
    pr_set = set()
    list_l = [int(i) for i in input('Введите значения разделенные пробелом: ').split()]
    pr = []
    for i in range(len(list_l)):
        unzip(list(product(list_l, repeat = i+1)))
    for elements in all_n:
        pr_set = frozenset({i for i in elements})
        finish_all.add(pr_set)
        pr_set = set()
    return len(finish_all), finish_all


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
