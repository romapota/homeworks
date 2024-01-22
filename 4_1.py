values: list
values_sum: list
values_sum_s: int
n: int
maxx:int
value_m: int
import itertools
def get_pins():
    values = []
    values_sum = []
    values_sum_s = 0
    n = int(input('N = '))
    maxx = 10000
    values_m = None
    for i in range(n):
         values.append(int(input()))
    var_values = list(itertools.combinations(values, 4))#все возможные комбинации 4 чисел
    c = int(input('C = '))
    for i in var_values:#подсчет суммы
        for j in i:
            values_sum_s += j
        values_sum.append(values_sum_s)
        values_sum_s = 0
    values_key = dict(zip(values_sum, var_values))
    for i in values_sum:
        if abs(c - i) < maxx:#нахождение максимально близкой суммы к заданной цели
            value_m = i
            maxx = abs(c-i)
    return print(values_key[value_m]), print(value_m)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_pins()
