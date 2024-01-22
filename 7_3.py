from itertools import product
def get_pins(values):
    var = {1: [1, 2, 4], 2: [1, 2, 3, 5], 3: [2, 3, 6], 4: [1, 4, 5, 7], 5: [2, 4, 8, 6, 5], 6: [6, 5, 9], 7: [4, 7, 8], 8: [5, 7, 0, 8, 9], 9: [6, 8, 9], 0: [8, 0]}
    all_var = set()
    for i in values:
        for j in var[int(i)]:
            all_var.add(j)
    all_var = list(all_var)
    answer = list(product(all_var, repeat=len(str(values))))#нахождение всех комбинаций
    answer_list = []
    s = ''
    for i in answer:#преобразование ответа к нужному виду
        for j in i:
            s += str(j)
        answer_list.append(s)
        s = ''
    print(answer_list)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_pins(input())